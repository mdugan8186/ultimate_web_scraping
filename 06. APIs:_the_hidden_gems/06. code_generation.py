# ==== code generation ====

# == using httpie ==

import json
import requests

url = "https://use1-prod-th.rbictg.com/graphql"

payload = [
    {
        "operationName": "GetRestaurants",
        "variables": {"input": {
            "filter": "NEARBY",
            "coordinates": {
                "userLat": 43.6447708,
                "userLng": -79.37330639999999,
                "searchRadius": 8000
            },
            "first": 2,
            "status": "OPEN"
        }},
        "query": """query GetRestaurants($input: RestaurantsInput) {
  restaurants(input: $input) {
    pageInfo {
      hasNextPage
      endCursor
      __typename
    }
    totalCount
    nodes {
      ...RestaurantNodeFragment
      __typename
    }
    __typename
  }
}

fragment RestaurantNodeFragment on RestaurantNode {
  _id
  storeId
  isAvailable
  posVendor
  chaseMerchantId
  cateringHours {
    ...OperatingHoursFragment
    ...OperatingHoursFragment
    __typename
  }
  curbsideHours {
    ...OperatingHoursFragment
    __typename
  }
  cateringHours {
    ...OperatingHoursFragment
    __typename
  }
  timezone
  deliveryHours {
    ...OperatingHoursFragment
    __typename
  }
  diningRoomHours {
    ...OperatingHoursFragment
    __typename
  }
  distanceInMiles
  drinkStationType
  driveThruHours {
    ...OperatingHoursFragment
    __typename
  }
  driveThruLaneType
  email
  environment
  franchiseGroupId
  franchiseGroupName
  frontCounterClosed
  hasBreakfast
  hasBurgersForBreakfast
  hasCatering
  hasCurbside
  hasDelivery
  hasDineIn
  hasDriveThru
  hasTableService
  hasMobileOrdering
  hasLateNightMenu
  hasParking
  hasPlayground
  hasTakeOut
  hasWifi
  hasLoyalty
  id
  isDarkKitchen
  isFavorite
  isHalal
  isRecent
  latitude
  longitude
  mobileOrderingStatus
  name
  number
  parkingType
  phoneNumber
  physicalAddress {
    address1
    address2
    city
    country
    postalCode
    stateProvince
    stateProvinceShort
    __typename
  }
  playgroundType
  pos {
    vendor
    __typename
  }
  posRestaurantId
  restaurantImage {
    asset {
      _id
      metadata {
        lqip
        palette {
          dominant {
            background
            foreground
            __typename
          }
          __typename
        }
        __typename
      }
      __typename
    }
    crop {
      top
      bottom
      left
      right
      __typename
    }
    hotspot {
      height
      width
      x
      y
      __typename
    }
    __typename
  }
  restaurantPosData {
    _id
    __typename
  }
  status
  vatNumber
  timezone
  __typename
}

fragment OperatingHoursFragment on OperatingHours {
  friClose
  friOpen
  monClose
  monOpen
  satClose
  satOpen
  sunClose
  sunOpen
  thrClose
  thrOpen
  tueClose
  tueOpen
  wedClose
  wedOpen
  __typename
}
"""
    }
]
headers = {
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.9",
    "apollographql-client-name": "wl-web",
    "apollographql-client-version": "4c6f26b",
    "dnt": "1",
    "origin": "https://www.timhortons.ca",
    "priority": "u=1, i",
    "sec-ch-ua": '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"macOS"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
    "x-forter-token": "2f0beb93b75241879637dc8177c19bc5_1747097135734__UDF43-m4_13ck__tt",
    "x-session-id": "90e0d4f9-07df-4a8a-a64b-6e8dcc8f6f60",
    "x-ui-language": "en",
    "x-ui-platform": "web",
    "x-ui-region": "CA",
    "x-user-datetime": "2025-05-12T20:46:22-04:00",
    "Content-Type": "application/json"
}

# response = requests.request("POST", url, json=payload, headers=headers)
# the above can be changed to the below
response = requests.post(url, json=payload, headers=headers)

# print(response.text)


# == using postman ==
# this also imports json along with requests

url = "https://use1-prod-th.rbictg.com/graphql"

payload = json.dumps([
    {
        "operationName": "GetRestaurants",
        "variables": {
            "input": {
                "filter": "NEARBY",
                "coordinates": {
                    "userLat": 43.6447708,
                    "userLng": -79.37330639999999,
                    "searchRadius": 8000
                },
                "first": 2,
                "status": "OPEN"
            }
        },
        "query": "query GetRestaurants($input: RestaurantsInput) {\n  restaurants(input: $input) {\n    pageInfo {\n      hasNextPage\n      endCursor\n      __typename\n    }\n    totalCount\n    nodes {\n      ...RestaurantNodeFragment\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment RestaurantNodeFragment on RestaurantNode {\n  _id\n  storeId\n  isAvailable\n  posVendor\n  chaseMerchantId\n  cateringHours {\n    ...OperatingHoursFragment\n    ...OperatingHoursFragment\n    __typename\n  }\n  curbsideHours {\n    ...OperatingHoursFragment\n    __typename\n  }\n  cateringHours {\n    ...OperatingHoursFragment\n    __typename\n  }\n  timezone\n  deliveryHours {\n    ...OperatingHoursFragment\n    __typename\n  }\n  diningRoomHours {\n    ...OperatingHoursFragment\n    __typename\n  }\n  distanceInMiles\n  drinkStationType\n  driveThruHours {\n    ...OperatingHoursFragment\n    __typename\n  }\n  driveThruLaneType\n  email\n  environment\n  franchiseGroupId\n  franchiseGroupName\n  frontCounterClosed\n  hasBreakfast\n  hasBurgersForBreakfast\n  hasCatering\n  hasCurbside\n  hasDelivery\n  hasDineIn\n  hasDriveThru\n  hasTableService\n  hasMobileOrdering\n  hasLateNightMenu\n  hasParking\n  hasPlayground\n  hasTakeOut\n  hasWifi\n  hasLoyalty\n  id\n  isDarkKitchen\n  isFavorite\n  isHalal\n  isRecent\n  latitude\n  longitude\n  mobileOrderingStatus\n  name\n  number\n  parkingType\n  phoneNumber\n  physicalAddress {\n    address1\n    address2\n    city\n    country\n    postalCode\n    stateProvince\n    stateProvinceShort\n    __typename\n  }\n  playgroundType\n  pos {\n    vendor\n    __typename\n  }\n  posRestaurantId\n  restaurantImage {\n    asset {\n      _id\n      metadata {\n        lqip\n        palette {\n          dominant {\n            background\n            foreground\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    crop {\n      top\n      bottom\n      left\n      right\n      __typename\n    }\n    hotspot {\n      height\n      width\n      x\n      y\n      __typename\n    }\n    __typename\n  }\n  restaurantPosData {\n    _id\n    __typename\n  }\n  status\n  vatNumber\n  timezone\n  __typename\n}\n\nfragment OperatingHoursFragment on OperatingHours {\n  friClose\n  friOpen\n  monClose\n  monOpen\n  satClose\n  satOpen\n  sunClose\n  sunOpen\n  thrClose\n  thrOpen\n  tueClose\n  tueOpen\n  wedClose\n  wedOpen\n  __typename\n}\n"
    }
])
headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'apollographql-client-name': 'wl-web',
    'apollographql-client-version': '4c6f26b',
    'content-type': 'application/json',
    'dnt': '1',
    'origin': 'https://www.timhortons.ca',
    'priority': 'u=1, i',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
    'x-forter-token': '2f0beb93b75241879637dc8177c19bc5_1747097135734__UDF43-m4_13ck__tt',
    'x-session-id': '90e0d4f9-07df-4a8a-a64b-6e8dcc8f6f60',
    'x-ui-language': 'en',
    'x-ui-platform': 'web',
    'x-ui-region': 'CA',
    'x-user-datetime': '2025-05-12T20:46:22-04:00'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)


#
#
"""
== Objective ==
- Convert a fully constructed API request (headers + body) into runnable Python code using Postman or HTTPie.
- Automate the request directly in Python using the `requests` library without manually copying headers or payload.

== Why Automate the Transition to Python? ==
- Manually building the headers and payload dictionary is time-consuming and error-prone.
- Exporting from the HTTP client avoids mistakes, ensures accuracy, and saves time.
- Both **HTTPie** and **Postman** can generate Python code from imported requests.

== How to Export to Python (HTTPie / Hoppscotch / Postman) ==
1. After importing the request (from `Copy as cURL`):
2. Click the **code generation icon** (looks like `</>`)
3. Choose:
    - Language: **Python**
    - Library: **requests**
4. Copy the auto-generated code block
5. Paste it into your Python script or notebook

== Example Output (Postman or HTTPie) ==
- Produces Python code like:
```python
import requests

url = "https://example.com/graphql"
payload = {
    "query": "...",
    "variables": {...}
}
headers = {
    "Content-Type": "application/json",
    "User-Agent": "..."
}

response = requests.request("POST", url, headers=headers, json=payload)
print(response.text)

== Common Adjustments ==
- If the GraphQL query is long and multi-line:
    - Wrap it in triple quotes (`'''`)
    - Watch for indentation or escape characters
    -also there may me double quotes ("") that may need to be adjusted to a single and double quote ('")

    -ex. 
    from:
    "sec-ch-ua": ""Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"",

    to:
    "sec-ch-ua": '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',

- The `.request("POST", ...)` syntax can be changed to `.post(...)` for readability:
    response = requests.post(url, headers=headers, json=payload)

== Comparison Between HTTPie vs Postman Export ==
- **HTTPie export**:
    - Sometimes formats the GraphQL query as a multiline string, which may require manual fixes
- **Postman export**:
    - Usually uses a clean single-line string for queries
    - Includes `import json` and serializes payload using `json.dumps()`
    
    - there was no adjusting the single line string with doc strings or adjusting other double quotes with this method

== Final Workflow Recap ==
1. Network tab: Identify the API request and copy it as `cURL`
2. HTTP client: Import `cURL` into HTTPie or Postman and verify the request works
3. Export to Python: Use the built-in code generator to produce a full Python `requests` script
4. Customize: Tweak query parameters, headers, or payload shape as needed

== Result ==
- You now have an end-to-end scraping strategy:
    - Discover hidden APIs
    - Test them visually
    - Export them into Python
    - Automate the process for reuse and scale
"""
