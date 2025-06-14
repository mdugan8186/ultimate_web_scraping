# ==== Note: quick correction to css selector ====

#
#
"""
Hey folks,

The HTML of the site has changed slightly since the lecture was recorded.

Now the img tags we want are nested within another div that is a sibling of the img we incorrectly end up selecting. This will make a lot more sense in a bit.

But in short, in our code, where we specify our root css, instead of

imgs = tree.css("figure a img")
We need to go for that second img for e.g. by using the adjacent sibling combinator:

imgs = tree.css("figure a img + div img")
The rest should work the same!

Best,

Andy

== as of 6-2-2025==
- this is the correct path to use:
img = tree.css('figure > div > div > a > img')

"""
