# ==== back to the API ====

from httpx import get


def get_response_for(keyword, results_per_page):
    url = f'https://unsplash.com/napi/search/photos?page=1&per_page={results_per_page}&query={keyword}'

    resp = get(url)

    if resp.status_code == 200:
        return resp.json()


if __name__ == '__main__':
    # download x imgs under this term
    # x = 2, page 1 suffices
    # if x = 200, page 1 most definitely does not suffice

    print(get_response_for('skyscraper', 3))


#
#
"""
== OBJECTIVE ==
- Begin building the API-based Unsplash image scraper.
- Use direct HTTP GET requests to Unsplash's documented search API endpoint.
- Retrieve JSON data for a given keyword and number of results per page.
- Extract the API structure and endpoints using browser DevTools (Network tab).
- Lay the foundation for implementing pagination in a future step.

== SECTION ==
- Created a new script file named `main_api.py`.
- Included Python's boilerplate condition:
    if __name__ == "__main__": ...
  This ensures code runs only when executed directly and not when imported.

- HTTP Client:
    - Using `httpx.get()` for all network operations.
    - Only GET requests are required, so no other verbs (POST, PUT, etc.) are needed.

- API Reverse Engineering:
    - Opened DevTools > Network tab > searched for a term like "skyscraper" or "spider".
    - Enabled the "XHR" filter to isolate relevant JavaScript requests.
    - Identified the request:
        https://unsplash.com/napi/search/photos?query=skyscraper&per_page=10
    - Key attributes in the response:
        - JSON structure includes:
            - `photos.results`: an array of photo objects
            - Each object contains a `urls` dictionary with keys:
                - "raw", "full", "regular", "small", "thumb"

- Implemented a function to send search requests via the API:
    - Parameters:
        - `keyword`: search term
        - `results_per_page`: number of results to request (Unsplash supports up to 30 per page)
    - Constructs the API URL using an f-string
    - Sends GET request via HTTPX
    - Returns `response.json()` on status 200, otherwise `None`

- Notes:
    - No API key required (at this stage)
    - No authentication or user-agent headers needed
    - No cookies required (browser includes analytics cookies, but they're not needed by our scraper)
    - API is publicly accessible for basic scraping use

- Pagination:
    - Not implemented yet, but planning ahead:
        - Unsplash API uses a `page` parameter in addition to `per_page`.
        - If user requests more than one page's worth of data (e.g. 100 results), we will:
            • Loop through pages
            • Accumulate results
        - Will implement this logic once the core retrieval function is complete.

== CODE EXAMPLE ==
    import httpx

    def get_api_results(keyword: str, results_per_page: int = 10):
        url = f"https://unsplash.com/napi/search/photos?query={keyword}&per_page={results_per_page}"
        response = httpx.get(url)

        if response.status_code == 200:
            return response.json()
        return None

    if __name__ == "__main__":
        data = get_api_results("dolphin", results_per_page=3)
        print(data)

== SUMMARY ==
- Initialized a new API-based scraper using Unsplash's public search endpoint.
- Extracted real API structure and parameters using browser DevTools.
- Built a minimal working function that fetches image search JSON.
- Confirmed no auth headers, cookies, or browser emulation required.
- Ready to extract image URLs from the JSON and prepare for pagination in the next step.
"""
