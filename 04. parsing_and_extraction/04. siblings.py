# ==== siblings ====

import requests as r
from bs4 import BeautifulSoup
from bs4 import NavigableString

resp = r.get('https://books.toscrape.com/')
soup = BeautifulSoup(resp.content, 'html.parser')

# in the previous lecture we explored the beautifulsoup navigation api as it pertains to the vertical transitions (moving up and down the hierarchy described in the tree). sometimes it is useful to navigate horizontally. if starting with a tag your not interested in its children, descendants, or parents, but rather it's siblings. as the name suggests, siblings are on the same level on the tree, they share the same paren.

print(soup.ul)
print('break')
print(soup.ul.li)

# to get the next sibling since beautifulsoup only returns the first of a tag
print(soup.ul.li.next_sibling)
# this is the navigable so it won't show up or be displayed as '\n'

# chain another next_sibling to get the sibling
print(soup.ul.li.next_sibling.next_sibling)

# we can even use previous sibling to navigate backwards
print(soup.ul.li.next_sibling.next_sibling.previous_sibling.previous_sibling)
