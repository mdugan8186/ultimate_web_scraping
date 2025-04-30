# ==== search ====

import requests as r
from bs4 import BeautifulSoup
from bs4 import NavigableString

resp = r.get('https://books.toscrape.com/')
soup = BeautifulSoup(resp.content, 'html.parser')

# the most efficient way to extract data from a document is to construct more powerful search recipes that target specific elements with more precision. in beautifulsoup we use .find() and .find_all() methods
# .find() - can be thought of a more specific case of .find_all() that returns only the first match
# .find_all() -returns a list of all the elements in a document that match the search criteria

# ==.find_all() search criteria ==

# - no criteria -
# this will return a list of all the elements in the document
# print(soup.find_all())
print(len(soup.find_all()))

# - tag name -
# print(soup.find_all('a'))
print(len(soup.find_all('a')))

# - multiple tags -
# we do this by passing in a list of strings rather than a single string
# print(soup.find_all(['a', 'p']))
print(len(soup.find_all(['a', 'p'])))


# == more complex criteria ==

# - combining tag names with the attribute values -
# tag_name: p
# attr: class="price_color"

# - use find_all with the attrs attribute -
price_tags = soup.find_all('p', attrs={'class': 'price_color'})

prices = []
for price in price_tags:
    prices.append(price.get_text())
print(prices)

# or

print([price.get_text() for price in price_tags])


# - using the class attribute -
# this is a more convenient method
price_tags2 = soup.find_all('p', class_='price_color')

print([price.get_text() for price in price_tags2])


# - more examples with attrs -
add_buttons = soup.find_all(
    'button', attrs={'data-loading-text': 'Adding...'})

print(len(add_buttons))


# - making the two dimensional search more powerful by making the attr value dynamic -

# instead of a string literal with 'Adding...' we can throw in a function that is evaluated at runtime

# target all the buttons who's data-loading-text attribute includes the word add por remove but isn't necessarily equal to either of those strings
# contains: 'add', 'remove', case-insensitive
# we'll express this using a lambda. instead of the string literal we're passing in an anonymous function that gets evaluated

add_buttons2 = soup.find_all('button', attrs={
                             'data-loading-text': lambda x: 'add' in x.lower() or 'remove' in x.lower()})

print(len(add_buttons2))
