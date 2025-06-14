# ==== filtering relevant urls ====

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


# img_filter(src, ['premium', 'profile'])


if __name__ == '__main__':
    img_nodes = get_img_tags_for('galaxy')

    img_urls = [i.attrs['src'] for i in img_nodes]
    relevant_urls = [i for i in img_urls if img_filter_out(
        i, ['plus', 'premium', 'profile'])]

    for u in relevant_urls:
        print(u)

    # print(len(img_nodes))
    # print(img_nodes)


#
#
"""
== OBJECTIVE ==
- Identify which images from the HTML results are relevant (i.e., non-premium, full-resolution photos).
- Filter out unwanted images such as thumbnails, profile pictures, and premium "Unsplash Plus" images.
- Prepare to isolate the highest resolution images from the `srcset` attribute in a future step.

== SECTION ==
- Updated the `get_image_tags()` function to make the `term` argument required.
    - Instead of setting a default search term, we now raise an exception if `term` is not provided.
    - This provides more control and clearer error messages.

- After extracting image nodes using "figure a img", we examined the `src` values being returned.
    - Many image URLs contain unwanted keywords like:
        - "plus" (premium/paid)
        - "profile" (user avatars)
    - These are not useful for our image scraper.

- Key discovery:
    - The `src` attribute often points to lower-resolution or cropped versions.
    - The `srcset` attribute contains multiple versions of the image with increasing resolution.
    - We'll need to extract the **last URL** from the `srcset` for the full-resolution image.

- To clean up irrelevant results, a utility function `image_filter()` was added:
    - It accepts a string URL and a list of disqualifying substrings.
    - It returns `False` if any of the substrings appear in the URL.
    - This is used to exclude premium and profile images.

== CODE EXAMPLE ==
    def image_filter(url: str, keywords: list[str]) -> bool:
        return not any(x in url for x in keywords)

    # Step 1: Collect image URLs
    image_urls = [img.attrs.get("src", "") for img in image_nodes]

    # Step 2: Filter out irrelevant ones
    excluded_terms = ["plus", "profile", "premium"]
    relevant_urls = [url for url in image_urls if image_filter(url, excluded_terms)]

    # Step 3: Print or use the filtered results
    for url in relevant_urls:
        print(url)

== SUMMARY ==
- Switched to a required search term to improve input validation.
- Confirmed that `src` contains only lower-quality versions.
- Built a filtering utility to discard image URLs that include "plus", "profile", or "premium".
- Still need to extract from `srcset` for the actual high-resolution files.
- Next: write a utility to parse and return the last URL in the `srcset` for final download.
"""
