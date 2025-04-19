# ==== POSTing data ====

# with verbs like POST, PUT, and PATCH the client is typically expected to send some data to the server and according to the http spec the data that goes with these verbs should be sent in the body of the request

# we've already sent data to the server through request headers and query parameters. the requests library makes it easy to send data through the body of the request. we just have to pass in the data as a dictionary to the data argument of the respected method

import requests as r


resp = r.post('http://www.httpbin.org/post', data={'key1': 'value1', })

print(resp.json())

# form is the default value for data sent with POST requests. it's known as form encoding. it takes the key value pairs and encodes them as strings. in the end it means the data is encoded as a query string. the key value pairs we send are separated by an ampersand and the key and the value are separated by a equals sign.

# we can see the output of the encoding from our request body
print(resp.request.body)


# we also get non alphanumeric characters encoded as well without needing to do anything extra here
resp2 = r.post('http://www.httpbin.org/post', data={
    'key1': 'value1',
    'key2': "a value with spaces and an apostrophe ' ",
})
print(resp2.json())

print(resp2.request.body)


# we can also send the data as plain text instead of the dictionaries we've been using
resp3 = r.post('http://www.httpbin.org/post', data='just some text')
print(resp3.json())

print(resp3.request.body)


# the most commonly in modern web applications  we'll be sending data as JSON. in the request library we do that by passing in a dictionary to the JSON parameter instead of data

resp4 = r.post('http://www.httpbin.org/post',
               json={
                   "key1": "value1",
                   "key2": "a value with spaces and an apostrophe ' "
               })

print(resp4.json())
print(resp4.request.body)

# with this there is a different content type and the data is no longer under form but the dat is under data. the resulting request body now contains a JSON byte string


# JSON stand for javascript object notation. JSON is no longer bound to javascript, we can work with JSON in python, java, and all programming languages. it is a lightweight data format the is commonly used for interchanging data in the web. it's similar to the dictionary data structure we use in python although there are some fine differences.
