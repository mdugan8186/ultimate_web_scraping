# ==== headers do lie ====

# in web scraping headers are of special importance because they can be used to send additional information that the server uses to identify the client. often times web servers are configured in a way that discriminates against certain clients. for example a web server might be configured to disallow requests from certain programmatic user-agents such as web scrapers. it might be configured to look for signs of popular browsers being used by humans, so it might be tracking mouse movements or page interaction just to determine the user is not a bot and oly allow those requests be allowed to be processed by the server.

# we can get around some of those controls to by manually setting the headers so as to appear to the server as a different client than we actually are

# headers do play a big role in the identification process.

# a striking example of this is to pretend we are a google crawling bot. google has a vast network of web servers that are constantly crawling the web. it's function is important to their search business because it allows them to index the web and provide search results to their users. this function is also important to website owners because it allows them to be picked put by google and included in their search results (which drives a lot of traffic). there is a symbiotic relationship where google benefits from crawling the web and the websites benefit from being crawled by google. a lot of web servers are configured to make exceptions to requests that originate from googles web crawlers. this presents an opportunity for us

# == an example ==
# this site, the financial times is behind a paywall
# https://www.ft.com/

# since financial times wants google bots to get though and read and index the article and include it in the search results. so if we pretend to be google bots we can get through the paywall

# in httpie add the website to the send bar

# go to headers and enter:
# Referer       https://www.google.com/

# then click send

# this may not work any longer
