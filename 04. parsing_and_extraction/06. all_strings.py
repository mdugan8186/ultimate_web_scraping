# ==== all strings ====

import requests as r
from bs4 import BeautifulSoup
from bs4 import NavigableString

resp = r.get('https://books.toscrape.com/')
soup = BeautifulSoup(resp.content, 'html.parser')

# the need to extract all string content from an html document is so common that the beautifulsoup library provides a shortcut to do it at scale
# if we wanted to extract all the strings from all the elements of a given tree we could use the stripped strings attribute

print(soup.stripped_strings)
# this returns a generator object that we can then iterate over
# <generator object PageElement.stripped_strings at 0x1044e7850>

# to do this we'll wrap this is a list constructor to exhaustively evaluate it all at once
all_strings = list(soup.stripped_strings)
print(all_strings)

# to see how many strings there are
print(len(all_strings))

# remember this will giver you the stripped version of the strings meaning that we're discarding all the leading and trailing white space characters

# if we need to retain the white spaces there's also a .strings attribute that does the same things minus the white space stripping
print(soup.strings)
# <generator object Tag._all_strings at 0x106372020>

all_strings2 = list(soup.strings)
print(all_strings2)
print(len(all_strings2))


# you can see by the number of both all_strings that the stripped_strings returns much less. (147 compared to 852). this is because much of the parsed content with the .strings attribute is in the form of navigable strings consisting of nothing but white space characters

print(list(soup.strings)[:10])
# we can see that in the first 10 spaces only one of them has a string, the rest is white space with navigable strings
