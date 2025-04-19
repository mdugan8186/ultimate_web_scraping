# ==== urllib ====

# the most basic way to make a request in python is to use the built in urllib library which is part of the standard library

# this module will give us a number of functions for making requests. the most basic is the urlopen function which takes the url as an argument and returns a response object

from urllib.request import urlopen

url = 'https://quotes.toscrape.com/'

resp = urlopen(url)

print(resp)

# to confirm the response was successful
print(resp.status)


# to retrieve the content
# this will return a byte string. you can tell this by the (b) in front of the string
content = resp.read()
# print(content)

# decode the byte string into a string with decode and provide the unicode of utf-8. by printing this you the indentation wil be correct
# print(content.decode('utf-8'))


# a more succinct way to do all of this is to use the urlopen function as a content manager.
with urlopen(url) as resp:
    content = resp.read()
    print(content.decode('utf-8'))

# we achieve what we did earlier but its a lot more concise. in addition to being more concise so we're writing less code this is also more robust because the context manager will automatically close the response object for us and will also handle any exceptions that may occur during the request.
# overall though using the urllib library is not very convenient for most use cases. the module offers an api that is too low level and at times a bit awkward. in modern python there are better alternatives like the request library. even in the documentation for urllib it gives a message to use the requests package
