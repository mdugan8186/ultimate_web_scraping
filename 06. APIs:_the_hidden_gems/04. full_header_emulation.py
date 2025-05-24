# ==== full header emulation ====


#
#
"""
== Objective ==
- Learn how to replicate browser-based HTTP requests by exporting them as `curl` commands.
- Understand how to easily import full request headers and body into HTTP clients without manual copying.

== Why This Matters ==
- While some APIs (like the Tim Hortons GraphQL example) don't require headers, **many sites do**.
- Headers like `User-Agent`, `Accept`, `Referer`, and `Origin` can be required for:
    - Authentication
    - CSRF protection
    - Mimicking a browser environment
- Copying headers manually is tedious and error-prone — especially when there are 10-50+ headers.

== Efficient Method: Copy as cURL ==
- In the browser DevTools Network tab:
    1. Right-click on a request ex. graphql response
    2. Select **Copy > Copy as cURL**
- This copies the **entire HTTP request** (method, URL, headers, body) as a ready-to-run `curl` command.
- scroll to bottom to see what the curl looks like 

== What is cURL? ==
- `curl` is a command-line tool to send requests over various network protocols.
- Syntax:
    ```bash
    curl -X POST 'https://example.com/api' \
         -H 'Content-Type: application/json' \
         -H 'User-Agent: ...' \
         --data-raw '{"query": "..."}'
    ```
- All headers appear as `-H` arguments; the request body appears after `--data-raw`.

== How to Use the Exported cURL ==
- Paste the copied `curl` into:
    - A terminal (to test it)
    - An HTTP client like **HTTPie**, **Hoppscotch**, or **Postman**

== HTTP Client Integration ==
- Many modern HTTP clients allow **cURL import**:
    - Paste the copied `curl` command
    -paste it at the end of the of the request url ex. https://use1-prod-th.rbictg.com/graphql
    - The tool auto-populates:
        - Method (GET/POST)
        - Headers
        - Body
        - URL
- In most tools:
    - `Ctrl+V` or `Cmd+V` → triggers an **Import from cURL** prompt
    - Click **Import** or **Update Request**

== Benefits ==
- Saves time: no need to retype headers one by one
- Ensures accuracy: copied headers match real browser requests
- Simplifies debugging: you can test exactly what the browser sent

== Practical Summary ==
- Even if headers aren't needed in a specific case, you should know how to replicate them when they are.
- The "Copy as cURL" → "Paste to Import" workflow is:
    - Fast
    - Accurate
    - Scalable

== Next ==
- In the next lecture, you'll use **Postman**, a more advanced HTTP client, to do the same and more.
"""


"""
== curl output ==
this is from the copied curl from the graphql response


curl 'https://use1-prod-th.rbictg.com/graphql' \
  -H 'accept: */*' \
  -H 'accept-language: en-US,en;q=0.9' \
  -H 'apollographql-client-name: wl-web' \
  -H 'apollographql-client-version: 4c6f26b' \
  -H 'content-type: application/json' \
  -H 'dnt: 1' \
  -H 'origin: https://www.timhortons.ca' \
  -H 'priority: u=1, i' \
  -H 'sec-ch-ua: "Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "macOS"' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: cross-site' \
  -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36' \
  -H 'x-forter-token: 2f0beb93b75241879637dc8177c19bc5_1747097135734__UDF43-m4_13ck__tt' \
  -H 'x-session-id: 90e0d4f9-07df-4a8a-a64b-6e8dcc8f6f60' \
  -H 'x-ui-language: en' \
  -H 'x-ui-platform: web' \
  -H 'x-ui-region: CA' \
  -H 'x-user-datetime: 2025-05-12T20:46:22-04:00' \
  --data-raw '[{"operationName":"GetRestaurants","variables":{"input":{"filter":"NEARBY","coordinates":{"userLat":43.6447708,"userLng":-79.37330639999999,"searchRadius":8000},"first":20,"status":"OPEN"}},"query":"query GetRestaurants($input: RestaurantsInput) {\n  restaurants(input: $input) {\n    pageInfo {\n      hasNextPage\n      endCursor\n      __typename\n    }\n    totalCount\n    nodes {\n      ...RestaurantNodeFragment\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment RestaurantNodeFragment on RestaurantNode {\n  _id\n  storeId\n  isAvailable\n  posVendor\n  chaseMerchantId\n  cateringHours {\n    ...OperatingHoursFragment\n    ...OperatingHoursFragment\n    __typename\n  }\n  curbsideHours {\n    ...OperatingHoursFragment\n    __typename\n  }\n  cateringHours {\n    ...OperatingHoursFragment\n    __typename\n  }\n  timezone\n  deliveryHours {\n    ...OperatingHoursFragment\n    __typename\n  }\n  diningRoomHours {\n    ...OperatingHoursFragment\n    __typename\n  }\n  distanceInMiles\n  drinkStationType\n  driveThruHours {\n    ...OperatingHoursFragment\n    __typename\n  }\n  driveThruLaneType\n  email\n  environment\n  franchiseGroupId\n  franchiseGroupName\n  frontCounterClosed\n  hasBreakfast\n  hasBurgersForBreakfast\n  hasCatering\n  hasCurbside\n  hasDelivery\n  hasDineIn\n  hasDriveThru\n  hasTableService\n  hasMobileOrdering\n  hasLateNightMenu\n  hasParking\n  hasPlayground\n  hasTakeOut\n  hasWifi\n  hasLoyalty\n  id\n  isDarkKitchen\n  isFavorite\n  isHalal\n  isRecent\n  latitude\n  longitude\n  mobileOrderingStatus\n  name\n  number\n  parkingType\n  phoneNumber\n  physicalAddress {\n    address1\n    address2\n    city\n    country\n    postalCode\n    stateProvince\n    stateProvinceShort\n    __typename\n  }\n  playgroundType\n  pos {\n    vendor\n    __typename\n  }\n  posRestaurantId\n  restaurantImage {\n    asset {\n      _id\n      metadata {\n        lqip\n        palette {\n          dominant {\n            background\n            foreground\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    crop {\n      top\n      bottom\n      left\n      right\n      __typename\n    }\n    hotspot {\n      height\n      width\n      x\n      y\n      __typename\n    }\n    __typename\n  }\n  restaurantPosData {\n    _id\n    __typename\n  }\n  status\n  vatNumber\n  timezone\n  __typename\n}\n\nfragment OperatingHoursFragment on OperatingHours {\n  friClose\n  friOpen\n  monClose\n  monOpen\n  satClose\n  satOpen\n  sunClose\n  sunOpen\n  thrClose\n  thrOpen\n  tueClose\n  tueOpen\n  wedClose\n  wedOpen\n  __typename\n}\n"}]'
"""
