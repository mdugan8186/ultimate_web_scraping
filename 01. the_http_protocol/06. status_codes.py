# ==== status codes ====

# http verbs communicate the type of action that the client wants to perform on the server. the client could send a lot of requests to the server which it is clearly not obligated to honor

# an example could be that the server receives a request to modify a resource that the client is not authorized to do so

# the client communicates intent through http verbs the sever. one of the most succinct ways the server communicates back whether it respects that request is the use of http status codes

# a status code is a 3 digit number that is sent back to the client with each response
# the first digit indicates the general category of the response (this carries the most amount of information)
# the second and third digits indicate a increasingly specific categories

# 100's
# these are known as informational. these are provisional statuses meant to provide additional information to the client about requests. these are rare in practice
# 101 switching protocols

# 200's
# this indicates success. when visiting google we got 200. when creating a new user account we might get 201 (crated). when we successfully delete a resource we typically get back a 204 (no content)

# 300's
# these are redirection responses. for instance if we try to access a resource that has been moved to a different location the server will send back a 301 (moved permanently) or 307 (temporary redirect)

# 400's
# these are client errors. a common example is 404 (not found), a 403 (forbidden), or a 405 (method not allowed)

# 500's
# these are server errors. the most common is 500 (internal server error). another is 502 (bad category)


# typically http responses will be accompanied by a short descriptive phrase
# 301 moved permanently
# 404 not found
# 200 ok
