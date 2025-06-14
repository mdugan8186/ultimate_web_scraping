# ==== wrapping up ====

from httpx import get
import os


def get_response_for(keyword, results_per_page, page=1):
    url = f'https://unsplash.com/napi/search/photos?page={page}&per_page={results_per_page}&query={keyword}'

    resp = get(url)

    if resp.status_code == 200:
        return resp.json()


def get_image_urls(data):
    results = data['results']

    img_urls = [x['urls']['raw'] for x in results if x['premium'] is False]
    img_urls = [x.split('?')[0] for x in img_urls]

    return img_urls


def download_images(img_urls, max_download, dest_dir='images', tag=''):
    successfully_downloaded = 0
    for url in img_urls:
        if successfully_downloaded < max_download:
            resp = get(url)
            file_name = url.split('/')[-1]

            if not os.path.exists(dest_dir):
                os.makedirs(dest_dir)

            with open(f'{dest_dir}/{tag}{file_name}.jpeg', 'wb') as f:
                f.write(resp.content)
                successfully_downloaded += 1
        else:
            break

    return successfully_downloaded


def scrape(keyword, num_of_results):
    start_page = 1
    success_count = 0

    while success_count < num_of_results:
        data = get_response_for(keyword, results_per_page=20, page=start_page)

        max_downloads = num_of_results - success_count

        if data:
            img_urls = get_image_urls(data)
            success_downloads = download_images(
                img_urls, max_downloads, tag=keyword)
            success_count += success_downloads
            start_page += 1

        else:
            print('Error: no data returned')
            break


if __name__ == '__main__':
    # download x imgs under this term
    # x = 2, page 1 suffices
    # if x = 200, page 1 most definitely does not suffice

    # data = get_response_for('skyscraper', 3)
    # print(get_image_urls(data))

    scrape('skyscraper', 3)


#
#
"""
== OBJECTIVE ==
- Complete the API-based image scraper by integrating all utility functions into an orchestrated workflow.
- Implement pagination logic to download an exact number of non-premium, high-resolution images for a given search term.
- Build the final `scrape()` function to dynamically request additional pages as needed and stop early if the target count is reached.
- Add a `download_images()` function with an optional `max_downloads` limit for flexible usage across multiple pages.

== SECTION ==
- GOAL: Allow users to request an exact number of images using:
      scrape(keyword="snowboarding", num_results=3)

- CHALLENGES:
    - Unsplash API returns a mix of premium and non-premium images.
    - Premium images must be filtered out, so any given page may return fewer usable results than requested.
    - Pagination is required to gather enough valid URLs.
    - Need to avoid downloading more images than requested (e.g. stop early if 3 out of 5 are usable).

- IMPLEMENTED COMPONENTS:

1. **download_images()**
    - Parameters:
        - image_urls (list)
        - max_downloads (int): how many images to actually save from the list
        - dest_dir (str): default = "images"
        - tag (str): used to prefix saved filenames
    - Logic:
        - Creates destination directory if it doesn’t exist using `os.makedirs()`
        - For each URL:
            - Sends GET request using HTTPX
            - Extracts filename from the final component of the URL
            - Saves the content as a `.jpg` with write-binary mode
            - Prefixes filename with `tag`
        - Stops downloading if `max_downloads` is reached early
        - Returns the count of successfully saved images

2. **scrape()**
    - Parameters:
        - keyword (str): search term
        - num_results (int): total number of images requested
    - Variables:
        - `page = 1`: start from the first API page
        - `success_count = 0`: track successful downloads
    - Loop:
        - While `success_count < num_results`:
            - Send a paginated request using `get_api_results()`
            - If no response, print and break
            - Extract valid image URLs using `get_image_urls_from_results()`
            - Determine how many more images are still needed
            - Download up to that many images from this page
            - Increment `success_count` by the actual count saved
            - Increment `page` to move to the next set of results

- NOTES:
    - The function avoids downloading more images than necessary.
    - The keyword argument `tag=keyword` is explicitly named to avoid argument order confusion.
    - In a real-world scraper, logging would be used here to track:
        - Current page number
        - URLs being processed
        - Number of images saved
        - File sizes and errors
    - You can re-use the logging setup from the HTML scraper section.

== CODE EXAMPLE ==
    import os
    import httpx

    def download_images(image_urls, max_downloads, dest_dir="images", tag="img"):
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)

        success_count = 0
        for url in image_urls:
            if success_count >= max_downloads:
                break

            try:
                response = httpx.get(url)
                filename = url.split("/")[-1]
                filepath = f"{dest_dir}/{tag}_{filename}.jpg"

                with open(filepath, "wb") as f:
                    f.write(response.content)

                success_count += 1
            except Exception as e:
                print(f"Error saving {url}: {e}")

        return success_count

    def scrape(keyword: str, num_results: int):
        page = 1
        success_count = 0

        while success_count < num_results:
            data = get_api_results(keyword, results_per_page=20, page=page)
            if not data:
                print("No data returned from API.")
                break

            results = data.get("results", [])
            image_urls = get_image_urls_from_results(results)

            remaining = num_results - success_count
            downloaded = download_images(image_urls, max_downloads=remaining, tag=keyword)
            success_count += downloaded
            page += 1

    if __name__ == "__main__":
        scrape(keyword="snowboarding", num_results=3)

== SUMMARY ==
- Finalized the API-based Unsplash scraper with full support for pagination and early termination.
- `download_images()` saves a bounded number of files from a given URL list and handles directory setup.
- `scrape()` orchestrates the process end-to-end:
    - Requests paginated API data
    - Filters non-premium URLs
    - Avoids over-downloading
    - Stops once the target count is reached
- The structure mirrors the HTML-based pipeline but is significantly more reliable and scalable.
- Optional: Add `logging` for page progress, file sizes, errors, and real-time visibility.
"""
