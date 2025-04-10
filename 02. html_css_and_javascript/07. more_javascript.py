# ==== more javascript ====

# this code grabs the button and the link and using. javascript it toggles the the link is hidden when the button is clicked, the text in the button will then change to show link. and when the button is clicked again again it will display the link and change the button text to hide link

# = html =
# <button id="btn">Hide link</button>

# = css =
# #btn {
#   background-color: white;
#   padding: 10px;
# }

# = js =
# const link = document.getElementsByTagName('a')[0]
# const btn - document.getElementById('btn')

# const hideLink = () => {
#   link.style.display = 'none'
# }

# const toggleLink = () => {
#   if (link.style.display === 'none') {
#       link.style.display = 'inline';
#       btn.textContent = 'Hide Link';
#   } else{
#       link.style.display = 'none';
#       btn.textContent = 'Show Link';
#   }
# }

# btn.addEventListener('click', toggleLink)
