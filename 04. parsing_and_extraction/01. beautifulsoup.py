# ==== beautifulsoup ====

# in a nutshell beautifulsoup is a python library for pulling data out of html and xml documents

# using beautifulsoup we'll easily be able to traverse the html document and extract the data that we need

# it is not part of the standard library so it must be installed

from bs4 import BeautifulSoup
import requests as r

resp = r.get('https://books.toscrape.com/')

soup = BeautifulSoup(resp.content, 'html.parser')
# we will explicit about the parser. html parser is the default in python. there are some other alternatives like lxml (since it is implemented in C that library offers significant performance boosts)

# this is the beautifulsoup object with a bunch of methods and attributes
print(type(soup))

# get the title. it returns the entire title tag from the html document
print(soup.title)

# get just the text
print(soup.title.text)

# get the html source of the page
# print(soup.prettify())

# use the html attribute to view the top level tree object. this is probably easier to see
# print(soup.html)


# the important thing ti note is that by parsing the html document into this beautifulsoup object we unlocked a new way of seeing the and manipulating the document. the big blob of text that we got from the server has been brought to life. under the hood beautiful soup has actually built a full tree of python objects that represent the html document. it's those objects that drive the behavior and attributes that we will benefit from. what we mean by document is the top level object that is at the root of the tree. it is conventionally called the document.

# viewing the document
print(soup.name)
