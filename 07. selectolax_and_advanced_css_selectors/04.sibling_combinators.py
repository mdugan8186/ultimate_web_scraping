# ==== sibling combinators ====

import requests as r
from selectolax.parser import HTMLParser

url = 'https://en.wikipedia.org/wiki/Rare-earth_element'

resp = r.get(url)

print(resp.status_code)

tree = HTMLParser(resp.text)
print(tree)

# == adjacent sibling ==
all_edits = tree.css('.mw-editsection-bracket + a')
print(all_edits)
print(len(all_edits))

tag_headings = [e.parent.parent.tag for e in all_edits]
print(tag_headings)

# == general sibling ==
all_edits_gen = tree.css('.mw-editsection-bracket ~ a')
print(all_edits_gen)
print(len(all_edits_gen))


#
#
"""
== Objective ==
- Learn how to use sibling combinators in CSS selectors: **adjacent sibling** (`+`) and **general sibling** (`~`).
- Apply these in Selectolax to extract elements that are next to or related to others at the same tree level.

== Adjacent Sibling Combinator (`+`) ==
- Selects elements that are **immediately after** a given sibling element.
- Syntax:
    selector1 + selector2
- `selector2` must be directly after `selector1` as a sibling.

Use Case:
- Extracting all "edit" links next to bracket elements in Wikipedia headings.

    all_edits = tree.css(".mw-editsection-bracket + a")

- This captures all anchor tags that are immediately preceded by an element with the class `.mw-editsection-bracket`.

Validation:
- Confirming that edit links appear across different heading levels:

    set([
        node.parent.parent.tag
        for node in all_edits
    ])

- Output:
    {'h2', 'h3', 'h4'}

== General Sibling Combinator (`~`) ==
- Selects elements that are **any sibling after** the specified element, not just the one immediately after.
- Syntax:
    selector1 ~ selector2

Use Case:
- Works similarly to the adjacent sibling example above, but may return more nodes in less strict scenarios.

    all_edits_general = tree.css(".mw-editsection-bracket ~ a")

Comparison:
- `.mw-editsection-bracket + a` is more precise.
- `.mw-editsection-bracket ~ a` is more flexible but may overmatch.

== Notes ==
- Adjacent sibling (`+`) is a stricter version of general sibling (`~`).
- Use adjacent when exact positioning is required.
- Use general when flexibility is acceptable or necessary.
- Both selectors return the same results in this case, but knowing the difference is important for future scraping work.

== Summary ==
- `+` (adjacent): one sibling directly after
- `~` (general): any following siblings
- In practice, prefer the strictest selector that gets the job done to reduce risk of overmatching
"""
