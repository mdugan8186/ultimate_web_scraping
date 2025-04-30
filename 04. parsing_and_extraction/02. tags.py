# ==== tags ====

# tags are the most common type of object in the parsed tree in the soup object of ours. tags are the html elements we are familiar with.

import requests as r
from bs4 import BeautifulSoup

resp = r.get('https://books.toscrape.com/')

soup = BeautifulSoup(resp.content, 'html.parser')


# the easiest way to select a tag is to treat it if it's an attribute of the parse tree

# title tag
print(soup.title)

# h1 (this will only return the first h1 tag)
print(soup.h1)

# div (this will only return the first div tag together with it's children)
first_div = soup.div
print(first_div)

# the type returned will be tag
print(type(first_div))

# get all the attributes
print(first_div.attrs)
# {'class': ['page_inner']}
# this shows a class attribute. class followed by a list. this is because a class can have multiple attributes

# select a child in the first div. form the tree object. this is like working your way through a file tree
print(first_div.div.div.attrs)
# {'class': ['col-sm-8', 'h1']}

# append another class to first div (this is something we wouldn't normally do)
first_div.attrs['class'].append('some-other-class')
print(first_div.attrs)
