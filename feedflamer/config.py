"""
Configuration settings for Twitter Critique Podcast Generator
"""

# Podcast Settings
DEFAULT_TWEET_COUNT = 10
MAX_TWEET_COUNT = 100
MIN_TWEET_COUNT = 1

# OpenAI Settings
OPENAI_MODEL = "gpt-4"
MAX_TOKENS = 1500
TEMPERATURE = 0.8

# Audio Settings
DEFAULT_LANGUAGE = 'en'
SPEECH_SPEED = False  # False = normal speed, True = slower

# File Settings
SCRIPT_PREFIX = "twitter_critique"