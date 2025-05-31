# ==== css combinators ====

import requests as r
from selectolax.parser import HTMLParser

url = 'https://en.wikipedia.org/wiki/Rare-earth_element'

resp = r.get(url)

print(resp.status_code)

tree = HTMLParser(resp.text)
print(tree)

site_reference = tree.css('sup a')
# print(site_reference)

links_site_ref = [n.attrs['href'] for n in site_reference]
# print(links_site_ref)


# == edit tags ==
child_ex = tree.css('div > span > a')

links_child_ex = [n.attrs['href'] for n in child_ex]
print(links_child_ex)


#
#
"""
== Objective ==
- Learn how to use **combinators** in CSS selectors to define relationships between elements.
- Understand how to use descendant (`A B`) and child (`A > B`) combinators in Selectolax.
- Practice extracting nested elements precisely using advanced selectors.

== CSS Combinators Overview ==
- Combinators let us select elements based on their relationship to others.
- Adds expressive power to CSS selectors.

== Descendant Combinator ==
- Syntax:
    selector1 selector2
- Selects all elements matching `selector2` that are **any descendant** of `selector1`.

Example:
    not a combinator (no space between):
    "p.some-class"

    combinator (space between):
    "p .some-class"
    # Selects any element with class "some-class" that is a descendant of a <p> tag.

Use Case:
    from the wikipedia page:
    https://en.wikipedia.org/wiki/Rare-earth_element
    
    # Extracting edit links that are nested inside <h2> headings

    edit_anchors = tree.css("h2 a")

    # Extract hrefs using list comprehension
    links = [node.attributes.get("href") for node in edit_anchors]

Notes:
- Easy to misuse: adding an unintended space between selectors turns it into a descendant selector.
- Powerful but may overmatch — selects all levels deep.

== Child Combinator ==
these are represented by the greater than sign (>)

- Syntax:
    selector1 > selector2
- Selects elements matching `selector2` that are **direct children** of `selector1`.

Example:
    "h2 > a"
    # Selects <a> elements that are direct children of <h2>

Observation:
- The "edit" anchor tags are not direct children of <h2>, but are wrapped in a <span>.
- Therefore, "h2 > a" returns nothing.

Fix:
    # Use a more specific selector:
    "h2 > span > a"

    precise_edit_anchors = tree.css("h2 > span > a")

== Selector Specificity Advice ==
- Both "h2 a" and "h2 > span > a" match the same nodes in this case.
- Specific selectors are:
    - Less likely to extract unrelated elements
    - More likely to break if the page structure changes, which is actually helpful
    - Preferable for maintainable and accurate scraping

== Summary ==
- Use **descendant combinator** (space) to find nested elements
- Use **child combinator** (>) for stricter one-level relationships
- In production scraping, **favor specific selectors** to avoid silent failures
"""
