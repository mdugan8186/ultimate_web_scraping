# ==== text search ====

import requests as r
from bs4 import BeautifulSoup
import re

resp = r.get('https://books.toscrape.com/')
soup = BeautifulSoup(resp.content, 'html.parser')


# == search by text ==
# we'll use the the word text and the text that we're looking for. it must be an exact match
print(soup.find_all(text='Fiction'))

# to find a partial match
# we'll combine regular expressions and functional search attrs
# for the functional expression import re
# re.compile('Fiction', re.I)
# I stands for ignore case
print(soup.find_all(text=re.compile('Fiction', re.I)))

# clean up the data with the strip method
text_matches = soup.find_all(text=re.compile('Fiction', re.I))

print([text.strip() for text in text_matches])


# using stripped_strings to clean up the data
# this the preferred way
all_text = list(soup.stripped_strings)
print([text for text in all_text if 'fiction' in text.lower()])


# getting text and an attribute
anchor_text_matches = soup.find_all('a', text=re.compile('Fiction', re.I))

print(anchor_text_matches)


# strings
navigable_strings_all_text = list(soup.strings)

print([text.parent for text in navigable_strings_all_text if 'fiction' in text.lower(
) and text.parent.name == 'a'])
