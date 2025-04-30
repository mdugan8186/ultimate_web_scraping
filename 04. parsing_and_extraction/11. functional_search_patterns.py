# ==== functional search patterns ====

import requests as r
from bs4 import BeautifulSoup
import pandas as pd

resp = r.get('https://books.toscrape.com/')
soup = BeautifulSoup(resp.content, 'html.parser')


# searching with ID
print(soup.find_all(id='messages'))

# with attrs with ID
print(soup.find_all(attrs={'id': 'messages'}))

# target all ID attributes with a lambda
# print(soup.find_all(attrs={'id': lambda x: x is not None}))

# these are different wys to get the same thing
print(len(soup.find_all(attrs={'id': lambda x: x is not None})))
print(len(soup.find_all(id=lambda x: x is not None)))
print(len(soup.find_all(lambda x: x.has_attr('id'))))


def fiction_category_anchor(tag):
    return tag.name == 'a' and 'category' in tag['href'] and 'Fiction' in tag.text


print(soup.find_all(fiction_category_anchor))
