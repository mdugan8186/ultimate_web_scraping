# ==== filtering canonical URLs ====

from httpx import get


def get_response_for(keyword, results_per_page):
    url = f'https://unsplash.com/napi/search/photos?page=1&per_page={results_per_page}&query={keyword}'

    resp = get(url)

    if resp.status_code == 200:
        return resp.json()


def get_image_urls(data):
    results = data['results']

    img_urls = [x['urls']['raw'] for x in results if x['premium'] is False]
    img_urls = [x.split('?')[0] for x in img_urls]

    return img_urls


if __name__ == '__main__':
    # download x imgs under this term
    # x = 2, page 1 suffices
    # if x = 200, page 1 most definitely does not suffice

    data = get_response_for('skyscraper', 3)
    print(get_image_urls(data))

#
#
"""
== OBJECTIVE ==
- Extract high-resolution image URLs from the JSON response returned by Unsplash's search API.
- Filter out premium (watermarked) images using the `premium` flag present in the API response.
- Clean the image URLs by removing query parameters, ensuring canonical high-resolution download links.

== SECTION ==
- This step assumes we've already called the API using:
    https://unsplash.com/napi/search/photos?query=KEYWORD&per_page=N
  and received a JSON payload.

- Step-by-step plan to extract and filter URLs:
    1. From the JSON root, access the `photos` key.
    2. From `photos`, access `results`, which is a list of photo objects.
    3. For each photo object:
        - Check if the `premium` flag is `False`.
        - Access the `urls` dictionary.
        - Extract the `raw` field from that dictionary.
    4. Clean the resulting URL:
        - Use `.split("?")[0]` to remove query parameters.
        - This gives a canonical URL pointing to the full-resolution image.

- Why `.split("?")[0]` is important:
    - Unsplash adds query strings (e.g. auto=compress&fit=crop) to its image URLs.
    - These alter the rendering (crop, size, format) but not the actual resource ID.
    - Removing them ensures we're getting the unmodified original image.

- Filtering premium images:
    - The API response contains a boolean field `"premium"` in each photo object.
    - If `premium` is `True`, the image is a watermarked paid image.
    - If `premium` is `False`, the image is free and usable.
    - This simplifies our earlier approach, which relied on detecting "plus" or "profile" in the URL string.

== CODE EXAMPLE ==
    def get_image_urls_from_data(data: dict) -> list[str]:
        '''
        Extracts a list of high-resolution, non-premium image URLs
        from the API JSON response.
        '''
        image_urls = []

        # Step 1: Navigate into nested JSON structure
        results = data.get("photos", {}).get("results", [])

        for x in results:
            if not x.get("premium", False):
                raw_url = x.get("urls", {}).get("raw", "")
                if raw_url:
                    clean_url = raw_url.split("?")[0]
                    image_urls.append(clean_url)

        return image_urls

    # Example usage:
    if __name__ == "__main__":
        data = get_api_results("galaxy", results_per_page=3)
        image_urls = get_image_urls_from_data(data)
        for url in image_urls:
            print(url)

== SUMMARY ==
- The JSON response has a nested structure:
    Root > "photos" > "results" > [photo objects]
- Each photo object contains:
    - A boolean `premium` flag
    - A `urls` dictionary with variants like `raw`, `full`, `regular`, etc.
- We only accept photos where `premium == False`.
- We use the `raw` URL as the highest-quality version, then strip query parameters for a clean result.
- This API-based method is faster and cleaner than the HTML parsing approach, requiring no structural selectors or `srcset` parsing.
- Output is now a clean list of canonical, non-premium, full-resolution image URLs.
- Next: handle pagination so that large batches (e.g. 50+ images) are supported seamlessly.
"""
