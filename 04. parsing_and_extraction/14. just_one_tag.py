# ==== just one tag ====

import requests as r
from bs4 import BeautifulSoup

resp = r.get('https://books.toscrape.com/')
soup = BeautifulSoup(resp.content, 'html.parser')


# == find_all() vs find() ==
#
# find_all() returns a python list of all matches
# find() returns only the first match

# returns all in a list regardless of the number of matches
print(soup.find_all('a', limit=2))

# returns a single tag if it finds one and None is there is not a tag
print(soup.find('a'))


# == select() vs select_one() ==
#
# select() returns a python list of all the elements
# select_one() returns only the first match

print(soup.select('a', limit=2))

print(soup.select_one('a'))
