# ==== an extra: pandas ====
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
import pandas as pd

resp = r.get('https://books.toscrape.com/')
soup = BeautifulSoup(resp.content, 'html.parser')

book_tags = soup.find_all('article', attrs={'class': 'product_pod'})


#  convert price
def clean_price(price):
    return float(''.join([char for char in price if char.isdigit() or char == '.']))


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

    return {
        'title': title,
        'price': clean_price(price),
        'rating': map_ratings(rating)
    }


# get all the data
book_data = [extract_book_data(book_tag) for book_tag in book_tags]

# print(book_data)


# find the average price of all the books
book_average_price = sum([book['price']
                         for book in book_data]) / len(book_data)

# print(book_average_price)


# books with a price under $20
books_under_20 = [book['title'] for book in book_data if book['price'] < 20]

# print(books_under_20)


# when working with a lot of data the way we were working with it above becomes cumbersome and inefficient. to be more efficient use pandas to work with it


# == pandas ==
# this is not part of the python standard library so it must be installed
# import pandas as pd

# from the list of dictionaries we can create a pandas dataframe which is a two dimensional data structure that is very similar to a spreadsheet

df = pd.DataFrame(book_data)
print(df)

# the two dimensions are the rows and columns. the rows are the individual books and the columns are the attributes
# the data is stored differently has a lot of built in functionality that makes it easier to work with

# average price of all books
pandas_average_price = df.price.mean()
print(pandas_average_price)

# books under $20
pandas_boolean_mask = df.price < 20
print(pandas_boolean_mask)
# this produces a boolean mask, each row will be true or false depending on the condition is met.

# by using square brackets on our main dataframe we can use the boolean mask to indicate to pandas which records we want to be returned back. pandas will return the records that are true
pandas_book_under_20 = df[df.price < 20]
print(pandas_book_under_20)

# to get just the titles
titles_under_20 = df[df.price < 20].title
print(titles_under_20)


# == exporting data with pandas ==

# exporting our book data to a csv file
# remember to go to your current working directory (with cd)

# df.to_csv('book.csv')

# get rid of the index with False
# df.to_csv('book.csv', index=False)

# exporting to a json file
# df.to_json('book.json', index=False)
