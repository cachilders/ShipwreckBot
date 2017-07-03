import os
from random import choice
import tweepy
from utils import csv_to_dict


class Bot:
    def __init__(self):
        self.base_tweet = "%s %s %s's %s %s %s"
        self.init_tables()
        self.init_api()

    def init_tables(self):
        # read data files
        self.books = csv_to_dict('csv/books.csv')
        self.characters = csv_to_dict('csv/characters.csv')
        self.places = csv_to_dict('csv/places.csv')
        self.verbs = csv_to_dict('csv/verbs.csv')
        self.parts = csv_to_dict('csv/parts.csv')
        self.adjectives = csv_to_dict('csv/adjectives.csv')

    def init_api(self):
        consumer_key = os.getenv("TWITTER_CONSUMER_TOKEN")
        consumer_secret = os.getenv("TWITTER_CONSUMER_SECRET")
        access_token = os.getenv("TWITTER_ACCESS_TOKEN")
        access_token_secret = os.getenv("TWITTER_ACCESS_SECRET")

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)

    def random_tweet(self, tags=[], send=False):
        # make random selections
        book = choice(self.books)
        book_id = book['id']

        # filter places and characters by book
        book_characters = list(
            filter(lambda c: c['book'] == book_id, self.characters))
        book_places = list(
            filter(lambda p: p['book'] == book_id, self.places))

        # make random selections
        char1 = choice(book_characters)
        char2 = choice(book_characters)
        verb = choice(self.verbs)
        place = choice(book_places)
        part = choice(self.parts)
        adjective = choice(self.adjectives)

        # exclude duplicate characters
        while (char1['name'] == char2['name']):
            char2 = choice(book_characters)

        # exclude impossible body parts
        while (char2['gender'] not in part['gender']) or (False):
            part = choice(self.parts)

        # populate tweet
        tweet = self.base_tweet % \
            (char1['name'].title(), verb['name'],
             char2['name'].title(), adjective['name'],
             part['name'], place['name'])

        # add tags
        for tag in tags:
            tweet += " %s" % tag

        if send:
            status = self.api.update_status(tweet)
        else:
            status = tweepy.models.Status()
            status.text = tweet

        return status


if __name__ == "__main__":
    bot = Bot()
    tweet = bot.random_tweet()
    print(tweet.text)
