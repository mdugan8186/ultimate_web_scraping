# ==== behavior ====

# == JavaScript ==

# javascript gives us control over the behavior of the webpage and is instrumental in building interactive webpages

# = html =
# <button id="btn">Hide link</button>

# = css =
# #btn {
#   background-color: white;
#   padding: 10px;
# }

# with javascript we can control the html and css on the page
# = js =
# const link = document.getElementsByTagName('a')[0]
# const btn - document.getElementById('btn')

# const hideLink = () => {
#   link.style.display = 'none'
# }

# btn.addEventListener('click', hideLink)


# in the javascript we are getting the button and the link. then we have the link disappear when the button is clicked
