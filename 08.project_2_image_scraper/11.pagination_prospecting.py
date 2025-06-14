# ==== pagination prospecting ====

from httpx import get


def get_response_for(keyword, results_per_page, page=1):
    # url = f'https://unsplash.com/napi/search/photos?page=1&per_page={results_per_page}&query={keyword}'
    url = f'https://unsplash.com/napi/search/photos?page={page}&per_page={results_per_page}&query={keyword}'

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
- Understand and implement pagination in the Unsplash API-based image scraper.
- Allow users to request a specific number of images, which may span multiple API pages.
- Refactor the API URL to directly access the `/photos` endpoint for cleaner JSON responses.
- Prepare the scraper to loop through paginated responses to accumulate enough valid image URLs.

== SECTION ==
- GOAL: Users should be able to request a fixed number of images (e.g. 50) for a given search term.
    - The scraper should return that exact number of **non-premium**, high-resolution image URLs.
    - This cannot be guaranteed from a single API page because:
        • Pages may contain premium images (which are filtered out).
        • Pages may not have enough results to satisfy the total count.

- INVESTIGATION:
    - Revisited the Unsplash website, opened DevTools, and observed what happens when clicking “Load more photos”.
    - Captured a new API request that includes:
        • Path: `/napi/search/photos`
        • Query params:
            - `query=...` (search term)
            - `per_page=...` (max 30)
            - `page=...` (pagination index)

- DISCOVERY:
    - The URL format includes the word `photos` in the path:
        https://unsplash.com/napi/search/photos?query=skyscraper&per_page=10&page=2
    - This changes two things:
        1. The API response JSON **now starts at `results`** instead of being nested under `"photos" → "results"`.
        2. All irrelevant root-level metadata is excluded, streamlining response parsing.

- IMPLEMENTATION:
    - Refactored `get_api_results()` to include:
        • `page` parameter with a default value of 1.
        • Updated endpoint to include `/photos` in the path.
    - Simplified JSON parsing:
        • Previously: `data.get("photos", {}).get("results", [])`
        • Now: `data.get("results", [])`

- RESULT:
    - We can now build paginated requests like:
        page 1 → results 1-10  
        page 2 → results 11-20  
        and so on.
    - This enables us to loop until we collect enough valid (non-premium) image URLs.

== CODE EXAMPLE ==
    def get_api_results(keyword: str, results_per_page: int = 10, page: int = 1):
        
Sends a GET request to the Unsplash API using pagination.
Returns JSON data with search results for the given page.

        url = (
            f"https://unsplash.com/napi/search/photos"
            f"?query={keyword}&per_page={results_per_page}&page={page}"
        )
        response = httpx.get(url)
        if response.status_code == 200:
            return response.json()
        return None

    def get_image_urls_from_results(results: list[dict]) -> list[str]:
        
Extracts cleaned, non-premium high-resolution image URLs from a page of results.

        image_urls = []
        for x in results:
            if not x.get("premium", False):
                raw_url = x.get("urls", {}).get("raw", "")
                if raw_url:
                    clean_url = raw_url.split("?")[0]
                    image_urls.append(clean_url)
        return image_urls

    if __name__ == "__main__":
        data = get_api_results("spider", results_per_page=5, page=1)
        if data:
            results = data.get("results", [])
            urls = get_image_urls_from_results(results)
            for url in urls:
                print(url)

== SUMMARY ==
- Pagination is necessary to ensure we collect a user-defined number of valid images.
- DevTools showed that Unsplash uses `page=...` in the query string and `/photos` in the path.
- Refactored the API function to accept a `page` argument and directly return JSON from `/photos`.
- Switched to a flatter JSON structure — now results are accessed via `data["results"]`.
- Next step: implement pagination logic to loop through pages and aggregate valid image URLs until the desired count is reached.
"""
