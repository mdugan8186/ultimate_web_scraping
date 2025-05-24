# ==== case study: coffee shop locations ====

#
#
"""
== Objective ==
- Identify the specific network request responsible for returning dynamic data on a website.
- Use browser DevTools to locate and analyze the response payload and request payload of that API call.
- Learn to replicate a POST-based GraphQL request using an HTTP client (e.g., HTTPie), even without sending headers.

== Finding the Data Source ==
- Input a location (e.g., a postal code) into the Tim Hortons store locator. The location we will use is M5E
- Open DevTools > Network tab > Filter by **XHR**.
    - XHR = XML HTTP Request, often used to fetch dynamic JSON content via JavaScript.
- Watch for newly triggered requests after submitting the location.
- Look for request names that hint at relevant data (e.g., `restaurants` or `getRestaurants`).

== Confirming the Response ==
- Select a promising XHR request and view the **Response** tab.
- Look for structured JSON data:
    - Confirm names and addresses match the rendered stores.
    - Check for extra metadata like `franchiseGroupName`, `storeNumber`, `latitude`, etc.
- This indicates the API returns **more data than the UI shows**, which can be scraped.

== Exploring the Request ==
- View the **Request Payload** tab:
    - The request body contains a **GraphQL query**, sent as JSON.
- View the **Headers** tab:
    - Method: `POST`
    - Status: `200 OK` (success)
    - Content-Type: typically `application/json` or `application/graphql`
- Most headers (e.g., `Origin`, `Referer`, `User-Agent`) can be ignored unless the server blocks access.

== Using HTTPie to Test ==
- Copy the API endpoint URL from the browser.
- Identify the method as `POST`.
- Copy the GraphQL query payload from the request body.
- In HTTPie (or any HTTP client), replicate the request:

```bash
http POST https://example-api/graphql query@body.json

- You can set the body as raw text or as a GraphQL-specific payload. select text
- to get the payload: in the payload tab right click on the list item and select copy value to get a copy of what you want
right click this:
[{operationName: "GetRestaurants", variables: {,…},…}]

- Even without copying headers, the server may still return full JSON responses.
- the list items are fully modifiable, ex. change first: 20 to first: 2 in the "GetRestaurants" tab

== Takeaways ==
- The API accepted the request with no headers or cookies, indicating no security or anti-scraping protection.
- Many production APIs will require headers, authentication, or cookies, but this one did not.
- GraphQL queries are editable — you can:
    - Rename operations
    - Remove unnecessary fields
    - Modify variables or coordinates
- This gives you full control over what data to extract and how much of it.

== What's Next ==
- We'll translate this GraphQL-based request into Python using a library like `requests` or `httpx`.
- Future examples will demonstrate how to:
    - Pass headers
    - Add cookies
    - Mimic more protected API calls
"""
