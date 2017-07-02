from random import choice
from utils import csv_to_dict, send_tweet


class Bot:

    def __init__(self):
        self.base_tweet = "%s %s %s's %s %s %s"
        self.init_tables()

    def init_tables(self):
        # read data files
        self.books = csv_to_dict('csv/books.csv')
        self.characters = csv_to_dict('csv/characters.csv')
        self.places = csv_to_dict('csv/places.csv')
        self.verbs = csv_to_dict('csv/verbs.csv')
        self.parts = csv_to_dict('csv/parts.csv')
        self.adjectives = csv_to_dict('csv/adjectives.csv')

    def random_tweet(self, tags=[]):
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
            (char1['name'], verb['name'],
             char2['name'], adjective['name'],
             part['name'], place['name'])

        # add tags
        for tag in tags:
            tweet += " %s" % tag

        return tweet


if __name__ == "__main__":
    bot = Bot()
    for n in range(10):
        tweet = bot.random_tweet()
        print(tweet)
