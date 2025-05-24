# ==== solution: interacting with the API ====

def get_jobs_for(lat=None, lng=None, results=20):

    import requests

    if lat is None or lng is None:
        raise ValueError('Both lat and lng must be provided')

    url = f"https://api.higherme.com/classic/jobs?page=1&includes=location,location.company,location.externalServiceReferences&limit={results}&filters\\[brand.id\\]=58bd9e7f472bd&filters\\[lat\\]={lat}\\[lng\\]=-{lng}&filters\\[distance\\]=20&sort\\[distance\\]=asc"

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


print(get_jobs_for(43.6532, -79.3832, 1))


#
#
"""
== Objective ==
- Finalize the API replication workflow by:
    - Intercepting the request from the Tim Hortons careers page
    - Testing it in Postman
    - Exporting to Python
    - Wrapping it in a reusable function that takes `latitude`, `longitude`, and `results` as parameters

== Interception Recap ==
- Navigate to: **Careers → Job Opportunities → Find a Restaurant and Apply**

- Enter a postal code (e.g., `Oakville, ON CA`) and open **DevTools > Network > XHR**
- Look for requests returning job listings with:
    - Titles (e.g., Production Team Member)
    - Tags: Full-time, Part-time
    - Distance from input location
    - Optional `requirements` field

== Testing the Request ==
- Right-click → **Copy as cURL**
- Paste into **Postman**
- Confirm that the request works and returns job data
- Use the **code generation tool** to export the request to Python using the `requests` library

== Implementation in Python ==
- Use a `GET` request (not `POST`) with dynamic query parameters
- Build a function that accepts:
    - `lat`: latitude (float)
    - `lng`: longitude (float)
    - `results`: max number of job listings (int, default = 20)
- URL parameters include:
    - `latitude`, `longitude`, `limit`, `brandId`, `distance`, and sort options

== Function Template ==
```python
import requests

def get_open_positions(lat: float, lng: float, results: int = 20):
    if lat is None or lng is None:
        raise ValueError("Latitude and longitude must be provided.")

    url = (
        "https://hiremee-api.hiremee.ca/api/jobpostings/search?"
        f"brandIds=1&latitude={lat}&longitude={lng}&limit={results}"
        "&sortBy=Distance&distance=200"
    )

    headers = {
        "Accept": "application/json, text/plain, */*",
        "User-Agent": "Mozilla/5.0",
        # Additional headers from Postman export if needed
    }

    response = requests.get(url, headers=headers)
    return response.json()
    == Testing the Function ==
- Example call:
    jobs = get_open_positions(43.6532, -79.3832)

- Confirms the full data is returned correctly
- Ready to extract and filter attributes (e.g., title, employment type, requirements)

== Next ==
- Use this JSON data to build a filtered result set that includes only the job details you care about.
"""
