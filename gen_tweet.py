import os
from random import choice
import tweepy
from utils import csv_to_dict

# read data files
books = csv_to_dict('csv/books.csv')
characters = csv_to_dict('csv/characters.csv')
places = csv_to_dict('csv/places.csv')
verbs = csv_to_dict('csv/verbs.csv')
parts = csv_to_dict('csv/parts.csv')
adjectives = csv_to_dict('csv/adjectives.csv')

# construct base tweet
base_tweet = "%s %s %s's %s %s %s. #shipwrecksf"


# function to generate tweets
def gen_tweet(book_id):

    # filter places and characters by book
    book_characters = list(filter(lambda c: c['book'] == book_id, characters))
    book_places = list(filter(lambda p: p['book'] == book_id, places))

    # make random selections
    char1 = choice(book_characters)
    char2 = choice(book_characters)
    verb = choice(verbs)
    place = choice(book_places)
    part = choice(parts)
    adjective = choice(adjectives)

    # exclude duplicate characters
    while (char1['name'] == char2['name']):
        char2 = choice(book_characters)

    # exclude impossible body parts
    while (char2['gender'] not in part['gender']) or (False):
        part = choice(parts)

    # populate tweet
    tweet = base_tweet % \
        (char1['name'], verb['name'],
         char2['name'], adjective['name'],
         part['name'], place['name'])

    return tweet


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


if __name__ == "__main__":
    for book in books:
        tweet = gen_tweet(str(book['id']))
        # send_tweet(tweet)
