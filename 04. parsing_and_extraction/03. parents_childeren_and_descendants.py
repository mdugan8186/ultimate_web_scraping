# ==== parents, children, and descendants ====

import requests as r
from bs4 import BeautifulSoup
from bs4 import NavigableString

resp = r.get('https://books.toscrape.com/')

soup = BeautifulSoup(resp.content, 'html.parser')


# the tags in the html document and the parse tree are organized in a hierarchy. the top level tag is the root of the tree and it has children which in turn have their own children and so on. in this hierarchy a child refers to the tag that is nested inside another tag.
print(soup.ul)
# the li tags are children of the ul tag and those li tags have their own children which are the anchor (<a>) tags

# the prettify method gives you a better visual sense of the hierarchy of the nesting going on. this will show the indentation
print(soup.ul.prettify())

# a child is a tag directly nested inside another tag


# descendants is broader concept that includes children, grandchildren, great grandchildren, and so on. in other words it's all the tags nested inside another tag no matter how deep the nesting goes
# the anchor tag is a descendant of the ul tag, but it's not a direct child it


# parents is a tag that contains another tag
# the ul tag is the parent of the li tag and the li are the parents of the anchor (<a>) tags

# all of these concepts are available to us from the parse tree and the tags we get from it


# find all children
print(soup.ul.children)
# this gives us an iterator which is a special ttype of object in python that we can use to iterate over a collection of elements. this evaluates lazily (which means it only when we ask for the next element in the iterator will it actually be computed)
# <list_iterator object at 0x100f6e710>

# to get all the children in a list we must wrap it in a list constructor
print(list(soup.ul.children))

# the output looks like strings, but it's actually a type of object called a navigable string which is a fancy name for a string that can be navigated because it has a sense of where in the document it appears
# we can filter the new lines ('\n') with NavigableString
# if the type in not equal to a navigable string then it returns true and there for be included
navig_str = list(filter(lambda x: type(
    x) != NavigableString, soup.ul.children))
print(navig_str)


# for readability we can wrap the filter logic as a stand alone function instead of just using a lambda function
def no_nav_string(iterable):
    return list(filter(lambda x: type(
        x) != NavigableString, iterable))


print(no_nav_string(soup.ul.children))


# we have access to descendants much like the same way as children
print(soup.ul.descendants)
# lazily evaluate
print(list(soup.ul.descendants))
# traverse
desc = no_nav_string(soup.ul.descendants)
print(desc)

# to get the first descendant
print(desc[0])


# we can get the parents from the list item
print(desc[0].parent)
