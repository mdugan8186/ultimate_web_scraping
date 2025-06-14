# ==== prospecting ====


#
#
"""
== OBJECTIVE ==
- Understand how Unsplash search results are structured in the HTML and via the API.
- Identify and avoid unwanted content such as ads, premium images, and related collections.
- Extract the full-resolution image URL either by parsing the HTML or using the API.
- Compare the pros and cons of HTML-based and API-based approaches.

== SECTION ==
- Start by performing a search on Unsplash, e.g., "stars" or "galaxy".
- Three types of unwanted elements appear in the results:
    - Ads
    - Premium images (with "Unsplash Plus" watermark)
    - Related collections
- Desired targets are the clean, high-resolution images shown in a grid.

- Inspecting the HTML:
    - search using stars in sky

    - Images are deeply nested inside divs and anchor tags.
    - A good selector pattern: figure a img (descendant combinator).
    - Images use the `srcset` attribute which contains multiple URLs at various resolutions.
    - The last item in the `srcset` is typically the highest resolution version.
    - The `src` attribute usually contains a lower-resolution fallback.
    - To get the best quality: parse the `srcset` and extract the final URL.

- API-based inspection using DevTools (Network tab with "XHR" filter):
    - search using galaxy

    - Typing in the search box sends background XHR requests for query suggestions.
    - Main data payload includes a JSON response with:
        - Total image count
        - Number of pages
        - List of image metadata
    - Each result contains a `urls` object with:
        - full, raw, regular, small, and thumb versions
    - The `full` URL provides an uncropped high-resolution image.

- Comparison:
    - `src` (HTML): cropped or limited resolution
    - Last entry in `srcset` (HTML): full resolution
    - `urls.full` (API): same as `srcset` final entry, often easier to access

== CODE EXAMPLE ==
    # Using a descendant combinator to select deeply nested images
    tree.css("figure a img")

    # Example: extracting the highest resolution from srcset
    srcset = element.attrs.get("srcset", "")
    url = srcset.split(",")[-1].split()[0] if srcset else None

    # Example: API JSON structure
    {
        "results": [
            {
                "urls": {
                    "raw": "...",
                    "full": "https://images.unsplash.com/photo-12345",
                    "regular": "...",
                    "small": "...",
                    "thumb": "..."
                }
            },
            ...
        ]
    }

== SUMMARY ==
- HTML method requires:
    - Skipping premium and ad elements
    - Using combinators like figure a img
    - Parsing the `srcset` string to get full-resolution URLs

- API method offers:
    - Cleaner access to image metadata in JSON
    - Direct access to full-resolution images via `urls.full`
    - Built-in support for pagination and result filtering

- Next steps:
    - Start by implementing the HTML-based scraper
    - Then build the API-based scraper as a more robust solution
"""
