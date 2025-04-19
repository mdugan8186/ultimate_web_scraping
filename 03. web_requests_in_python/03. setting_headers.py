# ==== setting headers ====

import requests
url = 'https://quotes.toscrape.com/'
resp = requests.get(url)

print(resp)

# this is a response object
print(type(resp))

# == response headers ==
# these are the response headers. they look and behave like a dictionary, but these are a special type of dictionary where the keys are case insensitive
print(resp.headers)

print(resp.headers['Content-Type'])
# case insensitive, this will access the same header with alternate casing
print(resp.headers['conTEnt-tYpe'])


# == request headers ==
# in order to send request headers we use the header parameter when making the request

# = User-Agent =
# one way is to set the user-agent header
# there are servers that try to block requests that originate from bots or scripts and in those cases setting the user-agent in the header to something else might help get around that filter
resp2 = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})

print(resp2.headers)


# using JSON to obtain the response content as a dictionary
url2 = 'https://httpbin.org/headers'
resp3 = requests.get(url2)
print(resp3)
print(resp3.json())

# we can seed the user agent is different in this response
resp4 = requests.get(url2, headers={'User-Agent': 'Mozilla/5.0'})
print(resp4)
print(resp4.json())


# == request attribute ==
# we can access the request object from the response to confirm what the requests library is sending. basically we will obtain the request that resulted in the response
print(resp3.request)

# we can obtain the data structure containing a dictionary like data structure containing the headers that went out in the request
print(resp3.request.headers)
