# ==== selector types ====

import requests as r
from selectolax.parser import HTMLParser

url = 'https://en.wikipedia.org/wiki/Rare-earth_element'

resp = r.get(url)
print(resp.status_code)

tree = HTMLParser(resp.text)
print(tree)

# simple selectors
print(len(tree.css('span')))
print(len(tree.css('.mw-editsection-bracket')))
print(len(tree.css('#firstHeading')))


# compound selector
print(tree.css('p.some_class'))
print(tree.css('p[class]'))


# complex
print(tree.css('a > img[src*="upload.wikimedia.org"]'))


# selector lists
print(len(tree.css('a > img[src*="upload.wikimedia.org"], p')))


#
#
"""
== Objective ==
- Review the four types of CSS selectors: simple, compound, complex, and selector lists.
- Understand how selectors can be combined with combinators to target elements more precisely.
- Summarize all CSS combinators seen so far.

== Selector Types ==

1. **Simple Selectors**
- Contain a single component.
- Match elements by:
    - Tag name (e.g. `span`)
    - Class (e.g. `.some-class`)
    - ID (e.g. `#first-heading`)
    - Attribute (e.g. `[href]`)
- Example:
    tree.css("span")  # selects all <span> tags

2. **Compound Selectors**
- Combine multiple conditions without a combinator.
- Element must satisfy **all** specified conditions.
- Examples:
    tree.css("p.some-class")  # <p> with class "some-class"
    tree.css("p[class]")      # <p> elements that have a "class" attribute

3. **Complex Selectors**
- Combine simple or compound selectors using **combinators**:
    - Descendant (` `)
    - Child (`>`)
    - Adjacent sibling (`+`)
    - General sibling (`~`)
- Example:
    tree.css("a > img[src*='upload.wikimedia.org']")
    # Select <img> tags that are direct children of <a> tags, where src contains a specific string

4. **Selector Lists**
- Use commas to target multiple selectors at once.
- Combine any mix of simple, compound, or complex selectors.
- Example:
    tree.css("a > img[src*='upload.wikimedia.org'], p")
    # Select matching <img> elements and all <p> elements in one go

== CSS Combinators Summary ==

- **Descendant (`space`)**:
    - Selects elements that are **descendants** of another.
    - Example: `"h2 a"` selects all `<a>` inside `<h2>`, at any depth.
    - Easy to use accidentally by including a space.

- **Child (`>`)**:
    - Selects **direct children** of another element.
    - Example: `"h2 > a"`

- **General Sibling (`~`)**:
    - Selects all **siblings** that follow a given element.
    - Example: `"div ~ p"`

- **Adjacent Sibling (`+`)**:
    - Selects the **next immediate sibling** only.
    - Example: `"div + p"`

== Summary ==
- **Simple**: Single component 'p'
- **Compound**: Multiple conditions, no combinator 'p.class'
- **Complex**: Joined by combinators p.class > article
- **Selector List**: Comma-separated selectors a, p.class > article
- These tools allow flexible and precise targeting of HTML elements during scraping
"""
