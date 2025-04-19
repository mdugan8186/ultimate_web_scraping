# ==== query parameters ====

# books.com?author=JKRowling&title=HarryPotter&price=10

# everything following the question mark is known as a query parameter. it's a list of attributes separated by ampersands (&). query parameters are used to pass additional information to the server when making a request. this information usually offers some filters or provides more details about the request


# to build urls with the request library we do not have to manually add the query parameters to the url by hand
# use the params argument and then pass in the query parameters as a dictionary

import requests as r

# this is the old fashioned way with the query parameters are imbedded in the url
url = 'https://api.coinbase.com/v2/exchange-rates?currency=BTC'

resp = r.get(url)
print(resp)

# this will be the entire list
# print(resp.json())

# narrow it down by using the keys we saw in the json output
print(resp.json()['data']['rates']['USD'])


# the proper way to use query parameters with requests and http
# use the base url and the parameters would be factored in externally
base_url = 'https://api.coinbase.com/v2/exchange-rates'

params = {'currency': 'BTC'}

# make the request by passing in the base url and the parameters separately

resp2 = r.get(base_url, params=params)

print(resp2)
print(resp2.json()['data']['rates']['USD'])

# there are two advantages to doing it this way
# 1. we don't have to worry about properly encoding the query parameter values
# 2. if we start passing in multiple parameters at once the readability of the url quickly deteriorates


# an example of multiple parameters
sun_url = 'https://api.sunrisesunset.io/json'

sun_params = {
    'lat': 43.6532,
    'lng': -79.3832,
    'timezone': 'EST',
    'date': 'today',
}

# just like params we'll create a headers dictionary
sun_headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
}

sun_resp = r.get(sun_url, params=sun_params, headers=sun_headers)
print(sun_resp)

# get the response code
print(sun_resp.status_code)

# this is what the url would look like with all the parameters
print(sun_resp.request.url)

# get the request headers
# the user-agent would be this if the header was not changed
# 'User-Agent': 'python-requests/2.32.3' potentially blocking us for bot activity
print(sun_resp.request.headers)


# get the json output
print(sun_resp.json())
