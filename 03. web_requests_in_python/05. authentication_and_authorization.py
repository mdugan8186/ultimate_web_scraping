# ==== authentication and authorization ====

# quite frequently we will have to interact with APIs that are not public and they will require us to authenticate with the server before we can make requests

# authentication - who we are
# authorization - what we can do, given who we are


# == API key ==
# the most common way to authenticate with a server is to use an API key
# an API key is a string that is unique to us and that the server recognizes and uses to verify our identity
# it would look like this:
import requests as r
API_KEY = 'YOUR_API_KEY_HERE'

# to use an API key with the request library we pass it into the header when we're invoking the http method


url = 'https://api.exchange.coinbase.com/fills'

headers = {
    'Authorization': f'Bearer {API_KEY}',
    'Content-Type': 'application/json'
}

resp = r.get(url, headers=headers)

# this will not work because we are using a made up header, but it does demonstrate the structure the request would take


# this is no different then what we did with headers. its just a regular header that takes special significance server side


# == basic auth ==
# another popular method is know as basic auth
# basic auth -> username, password

# to handle this in requests we use the auth argument. the auth argument takes a tuple of the username and password
auth = ('user1', 'pass2')

# in a real world scenario the username and password wouldn't be displayed in the url
auth_url = 'https://httpbin.org/basic-auth/user1/pass2'

auth_resp = r.get(auth_url, auth=auth)
