# ==== javascript in web scraping ====

# javascript is heavily used in modern webpages

# when the overall flow of a webpage is controlled through javascript and we get a high degree of interactivity without needing to reload the page the resulting site is called a single page application (SPA). when the user navigates to page like this the browser loads the html, css, and javascript the regular way, but then javascript takes over and controls the page


# implications for web scraping:

# what you see is not what you get
# when a page is dynamically controlled by javascript the html and css we see in the browser is not the same as the html and css that the browser first received from the server. to successfully scrap a page like this we will need a way to execute the javascript code and then scrap the resulting html.

# headless browser
# there are several ways to scrap a page like that, but the most effective is to use a headless browser. a headless browser is essentially a programmatic user-agent that executes the javascript and renders the page just as a regular page would, but obviously for a different purpose


# ways to tell if a website is using javascript:
# look at the network tab in our developer tools. refresh the page and see if there are a lot of script or js resources coming back it's  fairly good indicator that a lot of this data was not available in the initial html, but was requested and injected by the javascript code

# a better way is to check the page source and confirm that what you see is what you get. copy something from the page, then go to view page source, once there use find to try to locate what you copied from the page. if it's not there the initial pager source that the browser works with obtained from the server is not what the user sees after the page is rendered


# another way to check is to go to inspect, click on the setting (the gear in the top right corner), find the debugger, click on the box to disable javascript, then refresh the page. if the page doesn't load it is controlled by javascript
