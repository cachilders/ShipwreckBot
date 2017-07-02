from random import choice
from utils import csv_to_dict

# read data files
books = csv_to_dict('books.csv')
characters = csv_to_dict('characters.csv')
places = csv_to_dict('places.csv')
verbs = csv_to_dict('verbs.csv')
parts = csv_to_dict('parts.csv')
adjectives = csv_to_dict('adjectives.csv')

# construct base tweet
base_tweet = "%s %s %s's %s %s %s. #shipwrecksf"

# function to generate tweets
def gen_tweet(book_id):

	# filter places and characters by book
	book_characters = filter(lambda c: c['book'] == book_id, characters)
	book_places = filter(lambda p: p['book'] == book_id, places)

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

if __name__ == "__main__":
	for book in books:
		for m in range(10):
			tweet = gen_tweet(str(book['id']))
			print(book['name'], tweet, len(tweet))
