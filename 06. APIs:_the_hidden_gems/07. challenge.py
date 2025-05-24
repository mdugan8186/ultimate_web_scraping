# ==== challenge ====

import requests

url = "https://api.higherme.com/classic/jobs?page=1&includes=location,location.company,location.externalServiceReferences&limit=24&filters\\[brand.id\\]=58bd9e7f472bd"

payload = {}
headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'dnt': '1',
    'higherme-client-version': '2025.05.07_17.0',
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

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)


#
#
"""
== Objective ==
- Create a Python method to scrape **open job positions** from the Tim Hortons (HireMe.com) careers API.
- Practice intercepting, analyzing, and replicating real-time API requests with location-based filtering.

== Challenge Overview ==
- Navigate to: **Tim Hortons → More → Careers → Job Opportunities → Find a Restaurant and Apply**
- This redirects to **hireme.com**, which loads job listings dynamically via an API call.
- we'll use Oakville, ON CA for the location and remove any preset filters 

- Your task is to:
    - Intercept that API request
    - Rebuild and send the request in Python
    - Extract and return structured job data

== Method Requirements ==
- Function signature:
    ```python
    def get_open_positions(location: str, results: int = 10) -> List[Dict]:
    ```
- Parameters:
    - `location`: either a **latitude/longitude pair** or (optionally) a **postal code** that you geocode
    - `results`: number of job listings to return (e.g. 10, 20)

== Return Structure ==
- For each job position, return a dictionary with the following:
    - `title`: job title
    - `employment_type`: "Full-time", "Part-time", or both
    - `distance`: relative to the input location
    - `requirements`: optional field listing any posted requirements (if available)

== Bonus (Optional) ==
- Accept **postal code input** and convert it to coordinates via:
    - Google Maps API
    - Open-source alternatives (e.g. Nominatim / OpenStreetMap)

== Skills Practiced ==
- API request interception via DevTools
- Working with location-based filters (lat/lng, radius)
- Parsing JSON response data
- Optional: Geocoding postal codes to lat/lng using external APIs

== What's Next ==
- Attempt the challenge and build your method.
- In the following lecture, we'll walk through a working solution step by step.
"""
