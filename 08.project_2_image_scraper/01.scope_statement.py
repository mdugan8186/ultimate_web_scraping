# ==== scope statement ====

# if __name__ == '__main__':
#     scrape('water', 10)


#
#
"""
== OBJECTIVE ==
- Build a Python script to download high-resolution images from Unsplash.
- Exclude premium (watermarked) images from the results.
- Retrieve full-resolution image files, not thumbnails.
- Use both HTML scraping and API-based approaches.
- Handle pagination in the API-based approach to fulfill large result counts.

== SECTION ==
- Unsplash is a website where users upload high-quality, searchable images.
- Search results display smaller previews — these are not the full-resolution files.
- Premium images are often watermarked and should be skipped.
- The utility should accept:
    - A search keyword (e.g. "water", "skyscraper")
    - The number of images to download
- Example interface:
    scrape(keyword="water", num_results=10)

== CODE EXAMPLE ==
    def scrape(keyword: str, num_results: int) -> None:
        
        Downloads `num_results` high-resolution images from Unsplash
        that match the given `keyword`. Skips premium/watermarked images.
        Saves all valid images to the local directory.
        
        pass  # Implementation to be added separately for HTML and API methods

== SUMMARY ==
- HTML method:
    - Use requests and a parser like Selectolax or BeautifulSoup.
    - Pagination is not practical without using tools like Selenium or Playwright.
- API method:
    - More efficient and supports pagination via parameters like `page` and `per_page`.
    - Easier to retrieve full-resolution URLs and avoid watermarked content.
- Always inspect how Unsplash structures its image URLs to retrieve the correct file version.
"""
