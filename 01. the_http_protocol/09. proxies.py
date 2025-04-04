# ==== proxies ====

# so far http has been described as a stateless communication protocol between a client and a server. in practice however, due to the layered nature of the internet our request and response messages will pass through multiple intermediaries before they reach their destination. when they operate at an application layer these intermediaries are called proxies
# proxies are just another server that sits between the client making the request and the end server that will provide the response. and this server acts as an intermediary, typically doing something very specific, functional oriented thing.

# an example could be in a corporate setting a proxy server is used to control access to the internet.
#
# a caching proxy is another example. this is a server that stores a copy of the response message locally so if we make a request to a server the cache proxy will first see if it has a copy of the response message and if it does it will send that back to the client, if it doesn't it will actually make the request or forward the request to the server to sync up and store that copy locally so that the next time we make the request the proxy will see that it has a copy and serve that back to us which will be much faster and will not involve the server at all

# a load balancer is a third example. this is just a server that distributes the load of incoming requests across multiple servers

# in web scraping specifically proxies are also of special importance when we want to obfuscate our identity. if we are scraping lots of information from a given website we would want to make sure we are cycling through different IP addresses so that we don't get recognized and blocked by the server.
# the use of proxy servers is a convenient way to do that
# we would make the request from our scraping client, we'd use a residential proxy that transforms this request from a single IP to something that seems like it came from another IP. the server would see one request from many different IPs. instead of many requests from a single client. this makes it more difficult for the server to identify our scraping client
