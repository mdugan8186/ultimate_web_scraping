# === solution: processing the data ====

import pandas as pd


def get_jobs_for(lat=None, lng=None, results=20):

    import requests

    if lat is None or lng is None:
        raise ValueError('Both lat and lng must be provided')

    # adjust the url to proper syntax. notes at the bottom
    url = (
        f"https://api.higherme.com/classic/jobs?page=1"
        f"&includes=location,location.company,location.externalServiceReferences"
        f"&limit={results}"
        f"&filters[brand.id]=58bd9e7f472bd"
        f"&filters[lat]={lat}"
        f"&filters[lng]={lng}"
        f"&filters[distance]=20"
        f"&sort[distance]=asc"
    )

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'dnt': '1',
        'higherme-client-version': '2025.05.15_17.2',
        'origin': 'https://app.higherme.com',
        'priority': 'u=1, i',
        'sec-ch-ua': '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36'
    }

    response = requests.get(url, headers=headers)

    return response.json()


response_data = (get_jobs_for(43.6532, -79.3832, results=10))

# print(response_data)

# print(response_data.get('data'))

# print([r.get('attributes') for r in response_data.get('data')])

df = pd.DataFrame(
    data=[r.get('attributes') for r in response_data.get('data')],
    columns=['title', 'full_time', 'part_time', 'requirements', 'distance']
)

df.to_csv('open_positions.csv', index=False)


#
#
"""
== Objective ==
- Parse and clean the job listing JSON response returned from the careers API.
- Use Pandas to extract the key attributes and export the structured data to a CSV file.

== Response Data Structure ==
- Top-level key: `"data"` → contains a list of job position objects.
- Each object includes:
    - `"id"`: job posting identifier
    - `"attributes"`: dictionary with actual job details:
        - `"title"`: job title
        - `"full_time"`: boolean or tag
        - `"part_time"`: boolean or tag
        - `"requirements"`: string (optional)
        - `"distance"`: numeric value relative to queried coordinates

== Data Extraction Plan ==
1. Extract the top-level `"data"` list:
    ```python
    positions = response_data.get("data", [])
    ```
2. Pull only the `.get("attributes")` from each item:
    ```python
    attributes_list = [pos.get("attributes", {}) for pos in positions]
    ```

== Use of Pandas ==
- Import pandas:
    ```python
    import pandas as pd
    ```
- Create a DataFrame:
    ```python
    df = pd.DataFrame(attributes_list)
    ```

== Column Filtering ==
- Reduce to essential columns:
    ```python
    df = df[["title", "full_time", "part_time", "requirements", "distance"]]
    ```

== Export to CSV ==
- Export to file (without row index):
    ```python
    df.to_csv("open_positions.csv", index=False)
    ```

- `index=False` removes the default row numbering column (0, 1, 2, …).

== Result ==
- `open_positions.csv` is created with only the cleaned and structured job listing information.
- Ready for downstream analysis or review.

== Next ==
- Optionally enrich the script:
    - Add CSV filename as an argument
    - Handle empty/missing fields more gracefully
    - Integrate into a larger scraping pipeline
"""

"""
== adjusting the url to proper format ==

Original issue:
-------------
# Malformed query parameters:
filters\\[lat\\]={lat}\\[lng\\]=-{lng}

# The backslashes broke the query string format.
# The API could not parse the latitude and longitude correctly.
# Result: The API either returned null for 'distance' or excluded it,
# leading to NaN values in the DataFrame.

Bad example:
------------
https://api.higherme.com/classic/jobs?filters\[lat\]=43.65\[lng\]=-79.38

→ API doesn't recognize these as valid parameters.


Fix:
----
# Replaced with properly formatted parameters using correct square brackets:
filters[lat]={lat}&filters[lng]={lng}

# This lets the API:
  ✅ Parse coordinates
  ✅ Calculate distance to each job from that point
  ✅ Return the 'distance' field in the response JSON

Good example:
-------------
https://api.higherme.com/classic/jobs?filters[lat]=43.65&filters[lng]=-79.38


Conclusion:
-----------
→ Proper query parameter formatting is essential.
→ A clean URL → correct API behavior → accurate 'distance' values in your DataFrame.
"""
