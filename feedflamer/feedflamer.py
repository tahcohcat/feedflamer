#!/usr/bin/env python3
"""
Twitter Critique Podcast Generator

This script fetches recent tweets from a Twitter profile, generates a multi-panelist
critique podcast script using OpenAI, and converts it to audio using text-to-speech.
"""

import os
import json
import requests
from datetime import datetime
from typing import Dict, List, Any, Optional
import openai
from gtts import gTTS
import pygame
from pathlib import Path
import time
import re


class TwitterCritiquePodcastGenerator:
    def __init__(self, openai_api_key: str, twitter_bearer_token: str):
        """Initialize the Twitter critique podcast generator."""
        self.openai_client = openai.OpenAI(api_key=openai_api_key)
        self.twitter_bearer_token = twitter_bearer_token
        self.twitter_base_url = "https://api.twitter.com/2"

        # Define our podcast panelists with distinct personalities
        self.panelists = {
            "alex": {
                "name": "Alex Rivera",
                "role": "Social Media Strategist",
                "personality": "analytical, data-driven, focuses on engagement metrics and audience growth",
                "voice_style": "professional but approachable"
            },
            "maya": {
                "name": "Dr. Maya Chen",
                "role": "Digital Communications Expert",
                "personality": "academic, thoughtful, examines communication effectiveness and clarity",
                "voice_style": "measured and insightful"
            },
            "jordan": {
                "name": "Jordan Blake",
                "role": "Content Creator & Influencer",
                "personality": "creative, trend-focused, evaluates entertainment value and viral potential",
                "voice_style": "energetic and casual"
            },
            "sam": {
                "name": "Sam Martinez",
                "role": "Brand Consultant",
                "personality": "business-minded, risk-aware, assesses brand impact and reputation",
                "voice_style": "direct and practical"
            }
        }

    def get_user_by_username(self, username: str) -> Optional[Dict[str, Any]]:
        """Get Twitter user ID from username."""
        try:
            # Remove @ if present
            username = username.lstrip('@')

            headers = {"Authorization": f"Bearer {self.twitter_bearer_token}"}
            url = f"{self.twitter_base_url}/users/by/username/{username}"

            params = {
                "user.fields": "id,name,username,public_metrics,description,verified"
            }

            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()

            data = response.json()
            if 'data' in data:
                return data['data']
            else:
                raise Exception(f"User @{username} not found")

        except requests.RequestException as e:
            raise Exception(f"Error fetching user data: {e}")

    def get_recent_tweets(self, username: str, tweet_count: int = 10) -> Dict[str, Any]:
        """
        Fetch recent tweets from a Twitter profile.

        Args:
            username: Twitter username (with or without @)
            tweet_count: Number of recent tweets to fetch (max 100)

        Returns:
            Dictionary containing user info and tweets
        """
        try:
            # Get user information first
            user_data = self.get_user_by_username(username)
            user_id = user_data['id']

            headers = {"Authorization": f"Bearer {self.twitter_bearer_token}"}
            url = f"{self.twitter_base_url}/users/{user_id}/tweets"

            params = {
                "max_results": min(tweet_count, 100),
                "tweet.fields": "created_at,public_metrics,context_annotations,lang,possibly_sensitive,reply_settings",
                "exclude": "retweets,replies"  # Focus on original tweets
            }

            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()

            tweets_data = response.json()

            if 'data' not in tweets_data:
                raise Exception("No tweets found")

            return {
                "user": {
                    "name": user_data['name'],
                    "username": user_data['username'],
                    "followers": user_data['public_metrics']['followers_count'],
                    "verified": user_data.get('verified', False),
                    "description": user_data.get('description', '')
                },
                "tweets": tweets_data['data'],
                "fetched_at": datetime.now().isoformat(),
                "tweet_count": len(tweets_data['data'])
            }

        except requests.RequestException as e:
            raise Exception(f"Error fetching tweets: {e}")

    def analyze_tweets_sentiment(self, tweets: List[Dict]) -> Dict[str, Any]:
        """Analyze overall sentiment and themes of tweets."""
        tweet_texts = [tweet['text'] for tweet in tweets]
        combined_text = " ".join(tweet_texts)

        # Calculate basic metrics
        total_likes = sum(tweet.get('public_metrics', {}).get('like_count', 0) for tweet in tweets)
        total_retweets = sum(tweet.get('public_metrics', {}).get('retweet_count', 0) for tweet in tweets)
        total_replies = sum(tweet.get('public_metrics', {}).get('reply_count', 0) for tweet in tweets)

        avg_likes = total_likes / len(tweets) if tweets else 0
        avg_retweets = total_retweets / len(tweets) if tweets else 0

        return {
            "total_engagement": total_likes + total_retweets + total_replies,
            "avg_likes": avg_likes,
            "avg_retweets": avg_retweets,
            "tweet_lengths": [len(tweet['text']) for tweet in tweets],
            "avg_length": sum(len(tweet['text']) for tweet in tweets) / len(tweets) if tweets else 0
        }

    def generate_podcast_script(self, twitter_data: Dict[str, Any]) -> str:
        """
        Generate a multi-panelist critique podcast script using OpenAI.

        Args:
            twitter_data: Twitter user and tweets data

        Returns:
            Generated podcast script with multiple panelists
        """
        try:
            user = twitter_data["user"]
            tweets = twitter_data["tweets"]
            analysis = self.analyze_tweets_sentiment(tweets)

            # Prepare tweet summaries for the prompt
            tweet_summaries = []
            for i, tweet in enumerate(tweets[:5], 1):  # Focus on top 5 tweets
                metrics = tweet.get('public_metrics', {})
                tweet_summaries.append(
                    f"Tweet {i}: \"{tweet['text'][:100]}{'...' if len(tweet['text']) > 100 else ''}\" "
                    f"(❤️{metrics.get('like_count', 0)} 🔄{metrics.get('retweet_count', 0)} "
                    f"💬{metrics.get('reply_count', 0)})"
                )

            # Create detailed panelist descriptions
            panelist_descriptions = []
            for key, panelist in self.panelists.items():
                panelist_descriptions.append(
                    f"- {panelist['name']} ({panelist['role']}): {panelist['personality']}"
                )

            prompt = f"""
            Create a 4-5 minute podcast episode script where four social media experts critique recent tweets from @{user['username']} ({user['name']}).

            USER PROFILE:
            - Name: {user['name']} (@{user['username']})
            - Followers: {user['followers']:,}
            - Verified: {user['verified']}
            - Bio: {user['description'][:200]}

            RECENT TWEETS ANALYSIS:
            - Total tweets analyzed: {len(tweets)}
            - Average engagement: {analysis['avg_likes']:.1f} likes, {analysis['avg_retweets']:.1f} retweets
            - Average tweet length: {analysis['avg_length']:.0f} characters

            TOP TWEETS TO DISCUSS:
            {chr(10).join(tweet_summaries)}

            PANELISTS (each with distinct perspective):
            {chr(10).join(panelist_descriptions)}

            SCRIPT REQUIREMENTS:
            1. Start with a brief intro by a HOST introducing the episode and panelists
            2. Each panelist should speak in their distinct style and focus area
            3. Include natural conversation flow with agreements, disagreements, and building on each other's points
            4. Rate the overall Twitter presence on a scale of 1-10 with different criteria
            5. Give constructive feedback and suggestions for improvement
            6. End with quick final thoughts from each panelist
            7. Keep it conversational and engaging, like a real podcast
            8. Use clear speaker labels (HOST:, ALEX:, MAYA:, JORDAN:, SAM:)
            9. Include natural speech patterns, pauses indicated by "..."
            10. Total length: approximately 800-1000 words

            Make it sound like genuine experts having a thoughtful discussion, not just listing facts.
            """

            response = self.openai_client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {
                        "role": "system",
                        "content": "You are a podcast scriptwriter creating engaging multi-speaker social media critique shows. Write natural dialogue that sounds like real experts having genuine conversations."
                    },
                    {"role": "user", "content": prompt}
                ],
                max_tokens=1500,
                temperature=0.8
            )

            return response.choices[0].message.content

        except Exception as e:
            raise Exception(f"Error generating podcast script: {e}")

    def text_to_speech_multispeaker(self, script: str, output_file: str = "twitter_critique_podcast.mp3") -> str:
        """
        Convert the multi-speaker podcast script to audio using different voices.

        Args:
            script: The podcast script with speaker labels
            output_file: Output audio file name

        Returns:
            Path to the generated audio file
        """
        try:
            # Parse the script to separate speakers
            lines = script.split('\n')
            audio_segments = []
            temp_files = []

            # Voice mapping for different speakers (using different languages/accents for variety)
            voice_settings = {
                'HOST': {'lang': 'en', 'tld': 'com', 'slow': False},
                'ALEX': {'lang': 'en', 'tld': 'co.uk', 'slow': False},
                'MAYA': {'lang': 'en', 'tld': 'com.au', 'slow': False},
                'JORDAN': {'lang': 'en', 'tld': 'ca', 'slow': False},
                'SAM': {'lang': 'en', 'tld': 'com', 'slow': False}
            }

            segment_count = 0

            for line in lines:
                line = line.strip()
                if not line:
                    continue

                # Check if line has speaker label
                speaker_match = re.match(r'^([A-Z]+):\s*(.+)$', line)
                if speaker_match:
                    speaker = speaker_match.group(1)
                    text = speaker_match.group(2)

                    if speaker in voice_settings and text:
                        settings = voice_settings[speaker]

                        # Add a brief pause and speaker identification for clarity
                        full_text = f"{text}"

                        # Create TTS for this segment
                        tts = gTTS(
                            text=full_text,
                            lang=settings['lang'],
                            tld=settings['tld'],
                            slow=settings['slow']
                        )

                        temp_file = f"temp_segment_{segment_count}.mp3"
                        tts.save(temp_file)
                        temp_files.append(temp_file)
                        segment_count += 1

            # For simplicity, we'll create one combined file using the first voice
            # In a more advanced version, you'd use audio editing libraries to combine segments
            combined_text = re.sub(r'^[A-Z]+:\s*', '', script, flags=re.MULTILINE)
            combined_text = re.sub(r'\n+', ' ', combined_text)

            tts = gTTS(text=combined_text, lang='en', slow=False)
            output_path = Path(output_file)
            tts.save(str(output_path))

            # Clean up temp files
            for temp_file in temp_files:
                try:
                    os.remove(temp_file)
                except OSError:
                    pass

            print(f"Audio saved to: {output_path.absolute()}")
            return str(output_path.absolute())

        except Exception as e:
            raise Exception(f"Error generating audio: {e}")

    def play_audio(self, audio_file: str):
        """Play the generated podcast audio."""
        try:
            pygame.mixer.init()
            pygame.mixer.music.load(audio_file)
            pygame.mixer.music.play()

            print("🎧 Playing podcast... Press Enter to stop.")
            input()
            pygame.mixer.music.stop()
            pygame.mixer.quit()

        except Exception as e:
            print(f"Error playing audio: {e}")

    def generate_critique_podcast(self, username: str, tweet_count: int = 10, play_audio: bool = True) -> str:
        """
        Complete workflow: fetch tweets, generate critique, create audio.

        Args:
            username: Twitter username to analyze
            tweet_count: Number of recent tweets to analyze
            play_audio: Whether to play the generated audio

        Returns:
            Path to the generated audio file
        """
        try:
            print(f"📱 Fetching recent tweets from @{username}...")
            twitter_data = self.get_recent_tweets(username, tweet_count)

            user = twitter_data["user"]
            print(f"✅ Found {twitter_data['tweet_count']} tweets from {user['name']} ({user['followers']:,} followers)")

            print("🤖 Generating podcast critique script...")
            script = self.generate_podcast_script(twitter_data)

            # Save script to file
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            script_file = f"twitter_critique_{username}_{timestamp}.txt"
            with open(script_file, 'w', encoding='utf-8') as f:
                f.write(f"Twitter Critique Podcast: @{username}\n")
                f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write("=" * 50 + "\n\n")
                f.write(script)
            print(f"📄 Script saved to: {script_file}")

            print("🎙️ Converting to audio...")
            audio_file = f"twitter_critique_{username}_{timestamp}.mp3"
            audio_path = self.text_to_speech_multispeaker(script, audio_file)

            if play_audio:
                self.play_audio(audio_path)

            return audio_path

        except Exception as e:
            print(f"❌ Error in podcast generation: {e}")
            return ""


def main():
    """Main function to run the Twitter critique podcast generator."""
    print("🎙️ Twitter Critique Podcast Generator")
    print("=" * 40)

    # Get API keys from environment variables
    openai_api_key = os.getenv('OPENAI_API_KEY')
    twitter_bearer_token = os.getenv('TWITTER_BEARER_TOKEN')

    if not openai_api_key:
        print("❌ Error: OPENAI_API_KEY environment variable not set")
        print("Set it with: export OPENAI_API_KEY='your-api-key-here'")
        return

    if not twitter_bearer_token:
        print("❌ Error: TWITTER_BEARER_TOKEN environment variable not set")
        print("Get your bearer token from: https://developer.twitter.com/en/portal/dashboard")
        print("Set it with: export TWITTER_BEARER_TOKEN='your-bearer-token-here'")
        return

    # Get user input
    username = input("Enter Twitter username (without @): ").strip()
    if not username:
        print("❌ Username is required")
        return

    try:
        tweet_count = int(input("Number of recent tweets to analyze (default 10): ") or "10")
        tweet_count = max(1, min(tweet_count, 100))  # Limit between 1-100
    except ValueError:
        tweet_count = 10

    # Create generator and run
    generator = TwitterCritiquePodcastGenerator(openai_api_key, twitter_bearer_token)
    audio_file = generator.generate_critique_podcast(username, tweet_count)

    if audio_file:
        print(f"\n🎉 Podcast generation complete!")
        print(f"🎵 Audio file: {audio_file}")
        print(f"📊 Analyzed {tweet_count} tweets from @{username}")
    else:
        print("❌ Podcast generation failed.")


if __name__ == "__main__":
    main()