import os
from dotenv import load_dotenv
import tweepy
# from pprint import pprint

# Load credentials from .env
load_dotenv()
TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET")
TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")


# Create authenticator
auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
print("AUTH", auth)

# Create Twitter API connection object
api = tweepy.API(auth)
print("API", api)


# Run script to test connection:
if __name__ == "__main__":
    # Input twitter username as a test user
    screen_name = input("Please input a twitter user name:  ")

    # Get data about the test user
    # Create user class and get attributes
    user = api.get_user(screen_name)
    # pprint(user._json)
    print(user.id)
    print(user.screen_name)
    print(user.friends_count)
    print(user.followers_count)

    # Get tweets from the test user
    # statuses = api.user_timeline(screen_name)
    statuses = api.user_timeline(screen_name, tweet_mode="extended", count=150,
                                 exclude_replies=True, include_rts=False)
    # status = statuses[0]
    # pprint(dir(status))
    for status in statuses:
        print("----")
        print(status.full_text)
