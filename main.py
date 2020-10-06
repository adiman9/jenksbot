import sys
import random
import logging
import logging.handlers
import os

from dotenv import load_dotenv
import tweepy

load_dotenv()

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))

handler = logging.handlers.WatchedFileHandler(
        os.environ.get("LOGFILE", "./jenks.log"))
formatter = logging.Formatter(logging.BASIC_FORMAT)
handler.setFormatter(formatter)

logger = logging.getLogger(__name__)
logger.addHandler(handler)

consumer_key = os.environ.get("CONSUMER_KEY")
consumer_secret = os.environ.get("CONSUMER_SECRET")
access_token = os.environ.get("ACCESS_TOKEN")
access_secret = os.environ.get("ACCESS_SECRET")

# Authenticate to Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, 
                 wait_on_rate_limit_notify=True)

try:
    api.verify_credentials()
    logger.info("Authentication OK")
except Exception:
    logger.error("Error during authentication")
    sys.exit()

tweet_options = [
    "Hey, @tallguyjenks I was wondering... How tall are you?",
    "How tall is @tallguyjenks",
    "I wonder how tall @tallguyjenks is really?",
    "How tall are you? @tallguyjenks",
    "I really would like to know how tall @tallguyjenks is",
    "Is there anywhere I can find out how tall @tallguyjenks is?",
    "On a scale of 1-10 I think @tallguyjenks is probably 12 tall",
    "Is @tallguyjenks the tallest man on YouTube?",
    "Does anyone know how tall @tallguyjenks is?",
    "I have a fever. The only cure is knowing how tall @tallguyjenks is."
]

status = random.choice(tweet_options)
logger.info(f"Tweeting - {status}")

api.update_status(status)
