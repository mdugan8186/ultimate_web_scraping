# ==== extracting high-res image urls ====

from selectolax.parser import HTMLParser
from httpx import get


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

    # for u in url_res:
    #     print(u)

    if not url_res:
        return None

    return url_res[0][0].split('?')[0]

    # return url_res


if __name__ == '__main__':
    img_nodes = get_img_tags_for('galaxy')
    all_img_urls = [get_high_res_img_url(i) for i in img_nodes]
    img_urls = [u for u in all_img_urls if u]

    print(img_urls)

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
- Extract the highest resolution image URL from each image node using the `srcset` attribute.
- Remove unnecessary query parameters from the URL to ensure we retrieve the full image.
- Integrate the high-resolution extractor into the main HTML scraping pipeline.

== SECTION ==
- Previously, we extracted image URLs from the `src` attribute, but they were low resolution.
- Now we define a new utility function `get_high_res_image_url()`:
    - It accepts a single image node.
    - It accesses the `srcset` attribute.
    - It splits the `srcset` by commas to extract multiple URLs with associated widths.
    - Any one of these URLs can be used — but all include query parameters.

- Discovery:
    - If we remove the query parameters (everything after `?`), even the low-resolution version returns the full-resolution image.
    - So we don't need to determine the largest width from `srcset`.
    - Instead, we:
        - Pick any entry from `srcset`
        - Remove the query string using `.split("?")[0]`

- To prevent failures:
    - If `srcset` is missing, return `None`
    - Filter out unwanted entries using the `image_filter()` utility

- Final list of image URLs is built using a list comprehension:
    - Apply `get_high_res_image_url()` to each image node
    - Skip `None` entries

== CODE EXAMPLE ==
    def get_high_res_image_url(img_node):
        srcset = img_node.attrs.get("srcset", "")
        if not srcset:
            return None

        entries = [item.strip() for item in srcset.split(",")]
        if not entries:
            return None

        # Extract the first URL from srcset and remove query params
        url = entries[0].split(" ")[0]
        if image_filter(url, ["plus", "profile", "premium"]):
            return url.split("?")[0]
        return None

    # Integration with the main scraping flow
    image_nodes = get_image_tags("galaxy")
    all_image_urls = [get_high_res_image_url(img) for img in image_nodes]
    image_urls = [url for url in all_image_urls if url]

    for url in image_urls:
        print(url)

== SUMMARY ==
- Defined `get_high_res_image_url()` to extract a usable image from `srcset`.
- Removed query parameters to ensure clean URLs that point to full-resolution images.
- Incorporated filtering logic to discard irrelevant images (premium/profile).
- Final output is a clean list of high-resolution image URLs.
- Next: implement the download functionality to save these images locally.
"""
