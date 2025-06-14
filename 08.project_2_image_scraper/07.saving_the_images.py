# ==== saving the images ====

from selectolax.parser import HTMLParser
from httpx import get
import os


def get_img_tags_for(term=None):
    if not term:
        raise Exception('No search term provided')

    url = f'https://unsplash.com/s/photos/{term}'
    resp = get(url)

    if resp.status_code != 200:
        raise Exception('Error getting response')

    tree = HTMLParser(resp.text)
    imgs = tree.css('figure > div > div > a > img')
    return imgs


def img_filter_out(url: str, keywords: list) -> bool:
    return not any(x in url for x in keywords)


def get_high_res_img_url(img_node):
    srcset = img_node.attrs['srcset']
    srcset_list = srcset.split(', ')

    url_res = [src.split(' ') for src in srcset_list if img_filter_out(
        src, ['plus', 'premium', 'profile'])]

    if not url_res:
        return None

    return url_res[0][0].split('?')[0]


def save_images(img_urls, dest_dir='images', tag=''):
    for url in img_urls:
        resp = get(url)

        file_name = url.split('/')[-1]

        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)

        with open(f'{dest_dir}/{tag}{file_name}.jpeg', 'wb') as f:
            f.write(resp.content)


if __name__ == '__main__':
    img_nodes = get_img_tags_for('galaxy')
    all_img_urls = [get_high_res_img_url(i) for i in img_nodes]
    img_urls = [u for u in all_img_urls if u]

    save_images(img_urls, 'images', 'galaxy')

    # [print(get_high_res_img_url(i)) for i in img_nodes[:4]]

    # img_urls = [i.attrs['src'] for i in img_nodes]
    # relevant_urls = [i for i in img_urls if img_filter_out(
    #     i, ['plus', 'premium', 'profile'])]

    # for u in relevant_urls:
    #     print(u)

    # print(len(img_nodes))
    # print(img_nodes)

#
#
"""
== OBJECTIVE ==
- Finalize the HTML-based scraper by downloading the high-resolution images to a local directory.
- Create a utility function that takes image URLs and saves them as JPEG files using the original file names.
- Ensure the directory exists before writing files, and allow optional tagging of saved filenames.

== SECTION ==
- Define a utility function `save_images()`:
    - Accepts:
        - A list of image URLs
        - A destination directory (default = "images")
        - A tag to prepend to each saved file name
    - For each image URL:
        - Sends a GET request using HTTPX
        - Extracts a filename from the last part of the URL (using `url.split("/")[-1]`)
        - Prepends the tag to the filename
        - Writes the response content to disk in binary mode
    - If the target folder doesn't exist, it is created with `os.makedirs()`.

- This completes the functional scraping pipeline:
    1. Get image nodes
    2. Filter for relevant ones
    3. Extract high-resolution URLs
    4. Download and save to disk

- Extras:
    - Using `wb` (write binary) mode is important for non-text file I/O
    - Added a progress indicator (basic print logging) for better feedback during downloads

== CODE EXAMPLE ==
    import os
    import httpx

    def save_images(image_urls, dest_dir="images", tag="img"):
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)

        for url in image_urls:
            try:
                response = httpx.get(url)
                filename = url.split("/")[-1]
                filepath = f"{dest_dir}/{tag}_{filename}.jpg"

                with open(filepath, "wb") as f:
                    f.write(response.content)
                print(f"Saved {filepath}")
            except Exception as e:
                print(f"Failed to save {url}: {e}")

    # Integration with previous steps
    image_nodes = get_image_tags("galaxy")
    all_image_urls = [get_high_res_image_url(img) for img in image_nodes]
    image_urls = [url for url in all_image_urls if url]

    save_images(image_urls, dest_dir="images", tag="galaxy")

== SUMMARY ==
- Implemented `save_images()` to write high-resolution image content to disk.
- Created files using the last segment of the image URL, with an optional tag prepended.
- Ensured image directory exists before saving.
- Used write-binary mode to store images correctly.
- Added logging to indicate download progress.
- The HTML scraping pipeline is now complete.
"""
