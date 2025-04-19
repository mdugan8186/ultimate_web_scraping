# ==== requests ====

# requests is high level library that provides a much more convenient api for working with http in python. for this reason it's the most popular library for that purpose in python

# because requests is not part of the standard library we do need to install it separately. this can easily be done using pip


import requests

url = 'https://quotes.toscrape.com/'

# In Python's requests library, response.get() is a method used to send a GET request to a specified URL. It returns a Response object, which contains the server's response to the HTTP request. The get() method is a convenient way to retrieve data from a web server.
resp = requests.get(url)

print(resp)

# get the status code
print(resp.status_code)

# the response object also has a content attribute which returns the response payload in a byte string
# print(resp.content)

# decoding the byte string
# print(resp.content.decode('utf-8'))


# use the text attribute to get the response content as a string directly so we don't have to walk through all the previous steps
# when using the text attribute we let it handle the decoding for us using an educated guess on the response headers
# print(resp.text)


# to access the headers we can access them with the headers attribute which returns a dictionary (remember these are the response headers not the requests ones)
print(resp.headers)


# with requests there is no need to close the response because the request library handles that for us, unless there are special circumstances like making streaming requests
