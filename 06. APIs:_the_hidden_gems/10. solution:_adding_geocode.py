# ==== solution: adding geocode ====

import pandas as pd
import pgeocode

nomi = pgeocode.Nominatim('ca')

union_stat = nomi.query_location('union station')
# print(union_stat)
postal = nomi.query_postal_code('m5e')
# print(postal)


def get_jobs_for(lat=None, lng=None, postal_code=None, results=20):

    import requests
    from pgeocode import Nominatim

    if (lat is None or lng is None) and postal_code is None:
        raise ValueError('Both lat and lng must be provided')

    if postal_code is not None:
        nomi = Nominatim('ca')

        geo = nomi.query_postal_code(postal_code)
        lat = geo.latitude
        lng = geo.longitude

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

    response = requests.get(url, headers=headers).json()

    df = pd.DataFrame(
        data=[r.get('attributes') for r in response.get('data')],
        columns=['title', 'full_time', 'part_time', 'requirements', 'distance']
    )

    return df


# print(get_jobs_for(43.6532, -79.3832, results=10))

print(get_jobs_for(postal_code='m5e', results=10))
print(get_jobs_for(postal_code='m2m', results=10))


#
#
"""
== Objective ==
- Improve the job scraping function to support **postal code input** (not just latitude and longitude).
- Use the `pgeocode` library to convert postal codes to coordinates.
- Return a cleaned Pandas DataFrame with job information from any Canadian location.

== Motivation ==
- Current function interface requires latitude and longitude.
- Real-world users typically input postal codes or city names.
- Solution: integrate a lightweight geocoding library for automatic coordinate resolution.

== New Dependency: pgeocode ==
- Install with:
    ```bash
    pip install pgeocode==0.4.0
    ```
- Offline geocoding tool (no API key required)
- Compatible with OpenStreetMap data

== Example Usage ==
```python
import pgeocode

nomi = pgeocode.Nominatim("CA")  # CA = Canada
location = nomi.query_postal_code("M5E")
lat = location.latitude
lng = location.longitude


== Updated Function Signature ==
def get_open_positions(postal_code=None, lat=None, lng=None, results=10):

== Logic Updates ==
- If postal code is provided:
    - Use `pgeocode.Nominatim("CA")` to convert it to lat/lng
- If lat/lng not provided and postal code is missing:
    - Raise a `ValueError`
- URL query is dynamically constructed using the coordinates
- Result is a Pandas DataFrame, not raw JSON

== Output Enhancement ==
- Extract key fields into a DataFrame:
    - `title`, `full_time`, `part_time`, `requirements`, `distance`
- Return the DataFrame directly instead of raw data

== Example Calls ==
# Using postal code only
get_open_positions(postal_code="M5E")

# Using coordinates
get_open_positions(lat=43.6532, lng=-79.3832, results=14)

== Error Handling ==
- If geocoding fails (e.g., typo or unsupported region), returns NaN
- Validate that latitude and longitude are present before continuing
- Raises helpful errors when inputs are incomplete or invalid

== Result ==
- A flexible scraping function that works with either coordinates or postal code
- Usable as a backend for GUI tools or command-line interfaces
- Enhances usability without changing core scraping logic

== Next ==
- Wrap up with optional enhancements:
    - Add CSV export toggle
    - Allow column filtering
    - Convert to CLI tool or web backend
"""
