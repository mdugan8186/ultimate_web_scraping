# ==== but, this website remembers me ====

# if http is truly stateless how can websites remember us as we browser from one page to the next (think about a shopping cart in an online store or a login profile)

# == state ==
# the condition of a system at a given point in time, which in turn is the result of it's history as well as the current inputs


# even though http as a protocol is stateless the entirety of the client server data interchange does not need to be stateless. the web is just a collection of interconnected resources that are accessed through http

# in the context of a client server communication state is or could be the information that is stored on the server that is associated with a given client. this state is what allows a server to remember the client. in practicer this often takes the place in the form of browser cookies that is generated by the server and stored on the clients browser or user agent. the cookies is sent back to the server with each request that the client makes which enables the server to then use the cookies to identify where the request came from and retrieve and process the state information associated with that user and then determine whether what it should do next
