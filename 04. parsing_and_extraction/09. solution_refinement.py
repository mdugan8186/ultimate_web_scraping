# ==== solution refinement ===

# ==== challenge ====

# extract the following from the 1st page  of https://books.toscrape.com/:
# - full book title
# - price as a float
# - rating as an int


# data should be stored as a python list of dictionaries, where each book is a dictionary:
# e.g.
# {
#     'title': 'Mesaerion: The Best Science Fiction Stories 1800-1849',
#     'price': 37.59,
#     'rating': 1
# }

import requests as r
from bs4 import BeautifulSoup
import re
from random import choice

resp = r.get('https://books.toscrape.com/')
soup = BeautifulSoup(resp.content, 'html.parser')

book_tags = soup.find_all('article', attrs={'class': 'product_pod'})

# print(len(book_tags))
# print(book_tags[0])


# helper function
def clean_price(price):
    return float(''.join([char for char in price if char.isdigit() or char == '.']))


# using regex101 - import re -
def clean_price_reg(price):
    return float(re.sub("[^1-9.]", '', price))


# convert ratings
def map_ratings(rating):
    rating_map = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
    }
    return rating_map[rating]


def extract_book_data(book_tag):
    title = book_tag.find('h3').find('a')['title']
    price = book_tag.find('p', attrs={'class': 'price_color'}).get_text()
    rating = book_tag.find('p', attrs={'class': 'star-rating'})['class'][-1]

    # return title, price, rating
    return {
        'title': title,
        'price': clean_price(price),
        'rating': map_ratings(rating)
    }


# a = extract_book_data(book_tags[0])
# print(a)
# print(clean_price(a[1]))
# print(clean_price_reg(a[1]))
# print(extract_book_data(book_tags[0]))

# random choice - from random import choice
# print(extract_book_data(choice(book_tags)))

# get all the data
book_data = [extract_book_data(book_tag) for book_tag in book_tags]

print(book_data)
