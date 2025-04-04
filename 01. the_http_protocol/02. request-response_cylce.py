# ==== the request-response cycle ====

# use https://httpie.io/ to send http requests to a server and see the response that we get back


# go to google.com
# the client sent the request to the google server and the google server responded back with some content that was later rendered to look like the page we're used to seeing by the browser
# information retrieved from the server is plain text that represents an html document


# in the http protocol client and server communicate by exchanging individual messages, what the client sends is called a request and what the server sends back is called the response. each request-response cycle is in itself stateless (meaning a given request in http is by default independent of any other request)
