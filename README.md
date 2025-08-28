# 🎙️ Twitter Critique Podcast Generator

[![Python](https://img.shields.io/badge/Python-3.7+-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4-412991?style=for-the-badge&logo=openai&logoColor=white)](https://openai.com/)
[![Twitter API](https://img.shields.io/badge/Twitter-API%20v2-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://developer.twitter.com/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

> 🐦 **Transform Twitter profiles into engaging AI-powered critique podcasts!**

A Python application that fetches recent tweets from any Twitter profile and generates an entertaining podcast featuring four AI panelists who analyze, critique, and rate the user's Twitter presence with distinct expert perspectives.

## ✨ Features

- 🐦 **Twitter API Integration** - Fetches recent tweets from any public Twitter profile
- 🤖 **Multi-Panelist AI Analysis** - Four distinct AI experts with unique perspectives:
  - **Alex Rivera** - Social Media Strategist (analytics & growth focused)
  - **Dr. Maya Chen** - Digital Communications Expert (academic & thoughtful)
  - **Jordan Blake** - Content Creator (creative & trend-focused)
  - **Sam Martinez** - Brand Consultant (business & reputation focused)
- 🎙️ **Natural Podcast Format** - Generates conversational critique with ratings and suggestions
- 🔊 **Text-to-Speech Conversion** - Creates high-quality audio podcasts
- 📊 **Engagement Analysis** - Analyzes likes, retweets, replies, and content patterns
- 💾 **File Management** - Saves both scripts and audio files with timestamps
- 🎵 **Instant Playback** - Plays generated podcasts automatically

## 🎧 Sample Podcast Flow

Your generated critique podcast will include:
1. **Host Introduction** - Sets up the episode and introduces panelists
2. **Profile Overview** - User stats, bio, and recent activity summary
3. **Tweet-by-Tweet Analysis** - Detailed discussion of top recent tweets
4. **Multi-Perspective Critique** - Each panelist offers their unique viewpoint
5. **Numerical Ratings** - Scored evaluations on different criteria
6. **Constructive Suggestions** - Practical advice for improvement
7. **Final Thoughts** - Wrap-up with key takeaways

## 🚀 Quick Start

### Prerequisites

- **Python 3.7+** - [Download here](https://www.python.org/downloads/)
- **OpenAI API Key** - [Get yours here](https://platform.openai.com/api-keys)
- **Twitter Bearer Token** - [Get from Twitter Developer Portal](https://developer.twitter.com/en/portal/dashboard)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/twitter-critique-podcast.git
   cd twitter-critique-podcast
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your API keys**
   
   **Option 1 - Environment Variables:**
   ```bash
   export OPENAI_API_KEY='your-openai-api-key-here'
   export TWITTER_BEARER_TOKEN='your-twitter-bearer-token-here'
   ```
   
   **Option 2 - .env file:**
   ```
   OPENAI_API_KEY=your-openai-api-key-here
   TWITTER_BEARER_TOKEN=your-twitter-bearer-token-here
   ```
   
$headers = @{
  "Authorization" = "Bearer AAAAAAAAAAAAAAAAAAAAABfs9gAAAAAACHWGgVxHNtnUmpqUMi%2Bh2gbF74E%3D9GOvXQ8VSgrRkmJakMMZkselutTfIpYj6oxFjb2siKwb8IZuWs"
}

Invoke-WebRequest -Uri "https://api.twitter.com/2/users/by/username/williek" -Headers $headers


### Getting Twitter API Access

1. Apply for a Twitter Developer account at [developer.twitter.com](https://developer.twitter.com/)
2. Create a new project/app in the Developer Portal
3. Generate your Bearer Token from the "Keys and tokens" section
4. No additional permissions needed - the app only reads public tweets

### Usage

Run the script and follow the prompts:

```bash
python3 twitter_critique_podcast.py
```

**Example interaction:**
```
🎙️ Twitter Critique Podcast Generator
========================================
Enter Twitter username (without @): elonmusk
Number of recent tweets to analyze (default 10): 5

📱 Fetching recent tweets from @elonmusk...
✅ Found 5 tweets from Elon Musk (150,234,567 followers)
🤖 Generating podcast critique script...
📄 Script saved to: twitter_critique_elonmusk_20240128_143022.txt
🎙️ Converting to audio...
Audio saved to: twitter_critique_elonmusk_20240128_143022.mp3
🎧 Playing podcast... Press Enter to stop.
```

## 📁 Output Files

Generated files are saved with timestamps:

- **`twitter_critique_[username]_YYYYMMDD_HHMMSS.txt`** - Full podcast script with speaker labels
- **`twitter_critique_[username]_YYYYMMDD_HHMMSS.mp3`** - High-quality audio podcast file

## 🎭 Meet the Panelists

### Alex Rivera - Social Media Strategist
- **Focus**: Engagement metrics, audience growth, posting strategy
- **Style**: Data-driven analysis with practical insights
- **Ratings**: Engagement rate, growth potential, timing strategy

### Dr. Maya Chen - Digital Communications Expert  
- **Focus**: Communication effectiveness, message clarity, audience connection
- **Style**: Academic perspective with research-backed observations
- **Ratings**: Message clarity, communication impact, authenticity

### Jordan Blake - Content Creator & Influencer
- **Focus**: Entertainment value, viral potential, creative content
- **Style**: Energetic and trend-focused commentary
- **Ratings**: Creativity, entertainment factor, trend awareness

### Sam Martinez - Brand Consultant
- **Focus**: Brand reputation, business impact, risk assessment
- **Style**: Business-minded with reputation considerations
- **Ratings**: Brand consistency, professional image, business value

## 🛠️ Technical Details

### Dependencies

| Package | Purpose | Version |
|---------|---------|---------|
| `openai` | AI script generation | >=1.0.0 |
| `requests` | HTTP requests for Twitter API | >=2.31.0 |
| `gTTS` | Google Text-to-Speech | >=2.4.0 |
| `pygame` | Audio playback | >=2.5.0 |
| `python-dotenv` | Environment variable management | >=1.0.0 |

### APIs Used

- **🐦 [Twitter API v2](https://developer.twitter.com/)** - Tweet fetching and user data
  - Recent tweets endpoint
  - User lookup by username
  - Public metrics (likes, retweets, replies)
- **🤖 [OpenAI GPT-4](https://openai.com/)** - Multi-panelist script generation
- **🔊 [Google Text-to-Speech](https://gtts.readthedocs.io/)** - Audio conversion

## 📊 Analysis Features

### Tweet Metrics Analyzed
- **Engagement**: Likes, retweets, replies per tweet
- **Content**: Tweet length, topics, sentiment
- **Performance**: Average engagement, top performing tweets
- **Timing**: Posting patterns and frequency

### Critique Categories
- **Content Quality**: Clarity, value, entertainment
- **Engagement Strategy**: Audience interaction, call-to-actions
- **Brand Consistency**: Voice, messaging, professional image  
- **Growth Potential**: Viral capability, audience expansion
- **Technical Execution**: Hashtag usage, multimedia, formatting

## 🎨 Customization

### Modify Panelist Personalities

Edit the `panelists` dictionary in the main class:

```python
self.panelists = {
    "alex": {
        "name": "Your Panelist Name",
        "role": "Their Expertise Area",
        "personality": "Their analysis style and focus",
        "voice_style": "How they speak"
    }
}
```

### Adjust Critique Focus

Modify the `generate_podcast_script()` method to:
- Change critique criteria
- Adjust script length (currently 800-1000 words)
- Modify conversation style
- Add/remove analysis categories

### Audio Customization

Edit `text_to_speech_multispeaker()` to:
- Use different TTS voices
- Adjust speech speed
- Change voice mapping per panelist
- Add audio effects or music

## 🔧 Advanced Features

### Batch Processing
Process multiple Twitter accounts:

```python
usernames = ['user1', 'user2', 'user3']
for username in usernames:
    generator.generate_critique_podcast(username, tweet_count=15)
```

### Extended Analysis
Analyze more tweets for deeper insights:

```python
# Analyze up to 100 recent tweets
generator.generate_critique_podcast('username', tweet_count=50)
```

### Custom Rating Systems
Implement specialized rating criteria for different industries or niches.

## ⚠️ Rate Limits & Best Practices

### Twitter API Limits
- **Free Tier**: 500,000 tweets per month
- **Rate Limits**: 300 requests per 15-minute window
- **Best Practice**: Don't exceed 10-20 requests per minute

### OpenAI API Costs
- **GPT-4**: ~$0.03-0.06 per podcast (varies by length)
- **Estimate**: 1000-1500 tokens per critique
- **Optimization**: Use GPT-3.5-turbo for cost savings

## 🤝 Contributing

We welcome contributions! Areas for enhancement:

- 🔊 **Multi-voice TTS** - Different voices for each panelist
- 🎵 **Audio Production** - Background music, professional mixing
- 📊 **Advanced Analytics** - Sentiment analysis, topic modeling
- 🌐 **Web Interface** - User-friendly web app
- 📱 **Mobile App** - Native mobile application
- 🤖 **More Platforms** - Instagram, LinkedIn, TikTok analysis

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚖️ Legal & Ethical Considerations

- **Public Data Only**: Only analyzes publicly available tweets
- **Fair Use**: Critiques are transformative commentary
- **No Personal Attacks**: Focuses on content, not personal characteristics
- **Educational Purpose**: Designed for constructive feedback
- **Respect Privacy**: Never stores or shares personal data

## 🙏 Acknowledgments

- [Twitter API](https://developer.twitter.com/) for providing access to tweet data
- [OpenAI](https://openai.com/) for GPT-4 language model
- [gTTS](https://gtts.readthedocs.io/) for text-to-speech conversion
- The original Weather Podcast Generator project for inspiration

## 📞 Support

**Common Issues:**

**Twitter API Access:**
- Ensure your Bearer Token is valid and has read permissions
- Check rate limits if requests are failing
- Verify the username exists and account is public

**Audio Issues:**
- Ensure system has audio output capabilities
- Try installing pygame separately: `pip install pygame`
- Check file permissions for audio file creation

**Script Generation:**
- Verify OpenAI API key is valid and has credits
- Try reducing tweet count if hitting token limits
- Check internet connectivity for API calls

---

<div align="center">

**⭐ If this project helped you analyze Twitter content, please give it a star! ⭐**

Made with ❤️ for social media enthusiasts and podcast lovers

</div>