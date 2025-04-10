# ==== embedded ====

# in the previous videos we explored html, css, and javascript in isolation, each building on the previous one. it is also possible to embed css and javascript directly into the html

# == css ==

# = using the tag element in the head tag =
# <style>
# p {
#   color: red;
#   text-transform: uppercase;
# }
# </style>

# = use the style attribute (inline css) =
# <p style="color: red; text-transform: uppercase;">this is a paragraph</p>


# == javascript ==

# = use a script tag in the head tag or just above the closing of the bottom of the body tag (this is more common because it gives the browser time to load html and css first) =

# <script>
# const link = document.getElementsByTagName('a')[0]
# const btn - document.getElementById('btn')
# const hideLink = () => {
#   link.style.display = 'none'
# }
# btn.addEventListener('click', hideLink)
# </script>
