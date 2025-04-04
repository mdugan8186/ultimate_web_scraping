# ==== headers ====

# we mentioned that http is extensible. this means that the protocol allows for the addition of other information to the request and response message.

# one of the key ways that http is extensible is through the use of headers
# headers are a key value pairs that are sent along with each request and response message

# an example is when we went to google.com the server responded not only with the html document and a 200 OK status code, but also with a bunch of headers. some of them look cryptic and some look straight forward like a date. what we see is that the google server is sending a cookie which is a piece of information that will be stored in our browser or user-agent and sent back to the server which each subsequent request which how we will maintain a session with a server. we also see response headers. similarly we can also send request headers from the client to the server. for example we could send a header that specifies the type of content that we're expecting back from the server.

# example header:
# name:                 value:
# Accept-Language       es-MX or en-us

# so ultimately whether the header triggers sone spatial behavior or not is up to the server. the server can choose to ignore the header or interpret it in some special way
# the extensibility of http is dependant on a mutual understanding between the client and the server
