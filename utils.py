import os
import tweepy


def csv_to_dict(filename):
    fid = open(filename)
    lines = fid.readlines()

    keys = lines[0].rstrip('\n').split(',')
    out = list(
        map(lambda l: dict(zip(keys, l.rstrip('\n').split(','))), lines[1:]))
    return out


def send_tweet(tweet):

    consumer_key = os.getenv("TWITTER_CONSUMER_TOKEN")
    consumer_secret = os.getenv("TWITTER_CONSUMER_SECRET")
    access_token = os.getenv("TWITTER_ACCESS_TOKEN")
    access_token_secret = os.getenv("TWITTER_ACCESS_SECRET")

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    api.update_status(tweet)
    return
