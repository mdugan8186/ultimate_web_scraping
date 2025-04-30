# ==== searching by css ====

import requests as r
from bs4 import BeautifulSoup

resp = r.get('https://books.toscrape.com/')
soup = BeautifulSoup(resp.content, 'html.parser')


# == using find_all and attrs with class ==

book_tags = soup.find_all('article', attrs={'class': 'product_pod'})

titles = []
for tag in book_tags:
    title = tag.find('h3').find('a')['title']
    titles.append(title)

print(titles)


# == using css ==
# this will use the select method

title_tags = soup.select('article.product_pod > h3 > a')
titles_with_css = [tag['title'] for tag in title_tags]

print(titles_with_css)


# == css to search by attributes ==
attribute_with_css = soup.select('[title]')


# filtered attribute title that contains the word human
human_title = soup.select('[title*=Human]')
print(human_title)


# attributes and tag names
buttons = soup.select('button.btn-primary[data-loading-text][class*=primary]')

print(len(buttons))
