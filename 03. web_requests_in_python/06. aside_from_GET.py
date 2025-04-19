# ==== aside from GET ====

# the request library supports other http methods besides GET. like POST, PUT, DELETE, PATH, and others. the API remains fundamentally similar we just use the appropriate method name instead of GET.


# httpbin
# we'll use httpbin which is a good tool for testing http requests. it echos back the request that you made to it. you will see that the only thing we need to change is the http verb

import requests as r

# GET
print(r.get('https://httpbin.org/'))

# DELETE
print(r.delete('https://httpbin.org/delete').json())

# PATCH
print(r.patch('https://httpbin.org/patch'))

# PUT
print(r.put('https://httpbin.org/put'))

# POST
print(r.post('https://httpbin.org/post'))

# patch, put, and post are usually accompanied by a body of information sending some data to the server


# requests also supports HEAD and OPTIONS
# HEAD is used to retrieve the head of the resource without the body
# OPTIONS is used to retrieve the allowed methods for a given resource
