# ==== challenge ====

# extract the following from the 1st page  of https://books.toscrape.com/:
# - full book title
# - price as a float
# - rating as an int


# data should be stored as a python list of dictionaries, where each book is a dictionary:
# e.g.
# {
#     'title': 'Mesaerion: The Best Science Fiction Stories 1800-1849',
#     'price': 37.59
#     'rating': 1
# }

import requests as r
from bs4 import BeautifulSoup

resp = r.get('https://books.toscrape.com/')
soup = BeautifulSoup(resp.content, 'html.parser')

book_tags = soup.find_all('article', attrs={'class': 'product_pod'})

print(len(book_tags))
print(book_tags[0])


def extract_book_data(book_tag):
    title = book_tag.find('h3').find('a')['title']
    price = book_tag.find('p', attrs={'class': 'price_color'}).get_text()
    rating = book_tag.find('p', attrs={'class', 'star-rating'})['class'][-1]

    return title, price, rating


print(extract_book_data(book_tags[0]))
