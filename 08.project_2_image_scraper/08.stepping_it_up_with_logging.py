# ==== stepping it up with logging ====

from selectolax.parser import HTMLParser
from httpx import get
import os
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s'
                    )


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
        logging.info(f'Downloading {url}...')

        file_name = url.split('/')[-1]

        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)

        with open(f'{dest_dir}/{tag}{file_name}.jpeg', 'wb') as f:
            f.write(resp.content)
            logging.info(
                f'Saved {file_name}, with size {round(len(resp.content)/1024/1024, 2)} MB.')


if __name__ == '__main__':
    search_tag = 'moon'
    dest_dir = 'moon'

    img_nodes = get_img_tags_for(search_tag)
    all_img_urls = [get_high_res_img_url(i) for i in img_nodes]
    img_urls = [u for u in all_img_urls if u]

    save_images(img_urls[:5], dest_dir, search_tag)

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
- Add logging to the scraper to monitor download progress and gain visibility during execution.
- Use Python's built-in `logging` module to provide feedback while images are being saved.
- Include useful info such as timestamps, log level, file size, and URL.

== SECTION ==
- Previously, we had no indication of progress during downloads.
- Added logging using the built-in `logging` module.
    - Set log level to `DEBUG` to capture maximum output.
    - Configured log message format to show:
        - Timestamp
        - Log level
        - Message content
- Logging was added to the `save_images()` function:
    - Before downloading: log the target URL.
    - After saving: log the file name and size (converted from bytes to megabytes).
- Used rounding to improve readability of file size data.
- Additional improvements:
    - Refactored search tag and directory name into variables.
    - Demonstrated with a search tag like `"dolphin"` and printed clean logs for 3 images.

== CODE EXAMPLE ==
    import os
    import httpx
    import logging

    # Setup logging
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s | %(levelname)s | %(message)s"
    )

    def save_images(image_urls, dest_dir="images", tag="img"):
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)

        for url in image_urls:
            try:
                logging.info(f"Downloading: {url}")
                response = httpx.get(url)

                filename = url.split("/")[-1]
                filepath = f"{dest_dir}/{tag}_{filename}.jpg"
                size_mb = round(len(response.content) / (1024 ** 2), 2)

                with open(filepath, "wb") as f:
                    f.write(response.content)

                logging.info(f"Saved: {filepath} ({size_mb} MB)")
            except Exception as e:
                logging.error(f"Failed to save {url}: {e}")

    # Example run with a new search tag
    search_tag = "dolphin"
    dest_dir = "dolphins"

    image_nodes = get_image_tags(search_tag)
    all_image_urls = [get_high_res_image_url(img) for img in image_nodes]
    image_urls = [url for url in all_image_urls if url]

    # Limit to 3 images for testing
    save_images(image_urls[:3], dest_dir=dest_dir, tag=search_tag)

== SUMMARY ==
- Logging is now built into the image scraper to track download status.
- Timestamps, image file names, and file sizes are shown during execution.
- This improves user experience and helps monitor scraper behavior.
- Next: switch to the API-based method, which provides cleaner and more efficient scraping.
"""
