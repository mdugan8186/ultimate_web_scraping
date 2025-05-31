# ==== what is selectolax ====

import requests as r
from selectolax.parser import HTMLParser
from random import choice

url = 'https://en.wikipedia.org/wiki/Rare-earth_element'

resp = r.get(url)

print(resp.status_code)
# print(resp.text)

tree = HTMLParser(resp.text)
print(tree)
print(type(tree))

# .css() replaces .find_all()
# print(tree.css('p'))

print(type(tree.css('p')))
print(tree.css('p')[0])

random_node = choice(tree.css('img'))
print(random_node)

print(random_node.attributes)

print(random_node.html)

print(tree.css('p')[2].text())
print(tree.css('p')[2].text(deep=False))
print(tree.css('p')[2].html)


#
#
"""
== Objective ==
- Learn how to install and use the `selectolax` parser for working with HTML content.
- Understand the basic usage of `HTMLParser`, CSS-based querying, and working with node attributes and text.
- Compare node handling in Selectolax vs. BeautifulSoup.

== Installation ==
- Selectolax is not included in the standard library.
- Install it with:
    pip install selectolax==0.3.12

== Getting Started ==
- Use `requests` to fetch a web page's HTML (e.g. Wikipedia page on rare earth elements).

    import requests
    from selectolax.parser import HTMLParser

    response = requests.get("https://en.wikipedia.org/wiki/Rare-earth_element")
    html = response.text
    tree = HTMLParser(html)

== Tree Object ==
- `tree` is the parsed HTML object (similar to BeautifulSoup's soup).
- However, it exposes a different set of methods.
- There is no `find_all()` — instead, use `.css()` for CSS selector queries.

== Basic Node Selection ==
    # Select all paragraph nodes
    paragraphs = tree.css("p")  # returns a list of Node objects

    # Select a random image node
    from random import choice
    random_node = choice(tree.css("img"))

== Node Attributes ==
    # Dictionary of attributes (like src, alt, class, etc.)
    random_node.attributes

    # Full HTML representation of the node
    random_node.html

    # Text content (recursive by default)
    paragraphs[0].text()

    # Non-recursive (only immediate node's text)
    paragraphs[0].text(deep=False)

== Full Page Text ==
    # Get all text content from the page (like .stripped_strings in BeautifulSoup)
    tree.text()

== Notes ==
- `.css()` replaces `.find_all()` from BeautifulSoup and uses true CSS selectors.
- Node objects are similar to Tag objects in BeautifulSoup but faster and simpler.
- `.text()` extracts text deeply unless `deep=False` is set.
- `selectolax` uses Lexbor (C-based parser), making it much faster than BeautifulSoup.
- Ideal for performance-intensive scraping or when working with complex CSS selectors.

== Coming Up ==
- Dive deeper into advanced CSS selectors for precise data extraction using Selectolax.
"""
