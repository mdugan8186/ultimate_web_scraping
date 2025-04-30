# ==== extracting text ====

import requests as r
from bs4 import BeautifulSoup
from bs4 import NavigableString

resp = r.get('https://books.toscrape.com/')
soup = BeautifulSoup(resp.content, 'html.parser')


# once we isolate a tag we can extract the text from it
print(soup.a)

# one way to do this is the .get_text() method
print(soup.a.get_text())

# similar functionality is available with the text and string attribute available on the tag element directly
print(soup.a.text)
print(soup.a.string)

# all three of these appear to have the same output but there are some fine differences
# .get_text() - if we have a tag with multiple children this will return the text content of all them

# .text - this will behave the same way as the .get_text() method

# .string - if there are multiple children this will not return anything

print(soup.ul.get_text())
print(soup.ul.text)

# this returns None because the unordered list itself doesn't have any text \, it just contains other elements that may or may not contain text
print(soup.ul.string)


# also take note that .string returns a navigable strings rather than a python string
print(soup.a.get_text(), ' of type ', type(soup.a.get_text()))
print(soup.a.text, ' of type ', type(soup.a.text))
print(soup.a.string, ' of type ', type(soup.a.string))


# .text is the most common, but the .get_text() method has some added convenience features that may be useful on occasion
# pass in a string argument that will be used as a separator between the text content of all the children
print(soup.ul.text)
# default return the same thing
print(soup.ul.get_text())
# the functional form can be extended to  give us a more nuanced output
# using a separator
print(soup.ul.get_text(separator=', '))
# strip all the white space
print(soup.ul.get_text(strip=True))
