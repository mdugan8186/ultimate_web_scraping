# ==== scraping the html ====

from selectolax.parser import HTMLParser
from httpx import get


def get_img_tags_for(term='galaxy'):
    url = f'https://unsplash.com/s/photos/{term}'
    resp = get(url)

    if resp.status_code != 200:
        raise Exception('Error getting response')

    tree = HTMLParser(resp.text)
    imgs = tree.css('figure > div > div > a > img')
    return imgs


if __name__ == '__main__':
    img_nodes = get_img_tags_for('python')
    print(len(img_nodes))
    print(img_nodes)


#
#
"""
== OBJECTIVE ==
- Set up the HTML-based image scraper using Selectolax and HTTPX instead of BeautifulSoup and Requests.
- Build a helper function that sends a search request to Unsplash and extracts all image nodes using CSS selectors.
- Prepare to filter out unwanted image nodes in the next step by understanding the HTML structure first.

== SECTION ==
- A virtual environment was created and activated for this project.
- A single Python file was created with a placeholder function `get_image_tags`.
- Included the Python module check:
    if __name__ == "__main__": 
  This ensures the block runs only when the script is executed directly.
- Explanation:
    - `__name__` is a built-in variable in Python.
    - When a file is executed directly, `__name__` is set to `"__main__"`.
    - When a file is imported as a module, `__name__` is set to the module name.

- For this scraper, Selectolax and HTTPX were used instead of BeautifulSoup and Requests.
    - Advantages: HTTPX supports async; Selectolax is fast and lightweight.
    - Installed via terminal:
        pip install httpx==0.23.3
        pip install selectolax==0.3.12

- The scraping process:
    - Send an HTTP GET request to: https://unsplash.com/s/photos/{term}
    - Parse the HTML response with Selectolax's HTMLParser.
    - Use the CSS selector:
        "figure a img"
      to capture images nested within anchor tags inside figure tags.

- Observations:
    - The selector returned many image nodes, indicating successful scraping.
    - There may be extra, unwanted images (ads, avatars, icons) mixed in.
    - This will be refined in the next step to only return relevant, full-resolution URLs.

== CODE EXAMPLE ==
    import httpx
    from selectolax.parser import HTMLParser

    def get_image_tags(term="galaxy"):
        url = f"https://unsplash.com/s/photos/{term}"
        response = httpx.get(url)

        if response.status_code != 200:
            raise Exception("Error getting response")

        tree = HTMLParser(response.text)
        image_nodes = tree.css("figure a img")
        return image_nodes

    if __name__ == "__main__":
        images = get_image_tags()
        print(f"Found {len(images)} image nodes.")
        for img in images[:5]:
            print(img)

== SUMMARY ==
- Project initialized with a simple script and virtual environment.
- HTML scraping implemented using Selectolax and HTTPX for improved performance.
- Successfully extracted image nodes using the selector "figure a img".
- Ready to refine the results to isolate full-resolution image URLs in the next step.
"""
