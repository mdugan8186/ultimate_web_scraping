# ==== the advantages of APIs ====

#
#
"""
== Objective ==
- Understand the key **advantages of using APIs** for web scraping over traditional HTML parsing.
- Learn why APIs offer faster, more reliable, and more customizable scraping workflows.

== Why Use APIs for Scraping? ==
1. **Faster and More Efficient**
    - Traditional scraping involves multiple steps:
        1. Send request to webpage
        2. Wait for full page (and JS) to render
        3. Parse the HTML
        4. Traverse the DOM to extract data
    - API scraping skips rendering and DOM traversal.
    - JSON is returned immediately and can be processed directly — fewer moving parts = faster scraping.

2. **Less Volatile / More Stable**
    - Front-end pages change frequently (e.g., holiday themes, layout shifts, renaming classes).
    - APIs, especially data-returning endpoints, change much less often.
    - HTML/CSS changes often break traditional scrapers — API requests tend to stay consistent longer.
    - Example: Store hours (Mon-Sun) are stable fields with low change frequency.

3. **More Customizable**
    - API parameters can often be modified to:
        - Change the number of results (e.g., `"first": 1` vs. `"first": 200`)
        - Adjust geolocation or filters (`"lat"`, `"lng"`, `"radius"`, etc.)
    - You can dynamically test and tune payloads to extract only the data you want.
    - GraphQL especially allows control over both:
        - **Input shape**: filters, coordinates, limits
        - **Response shape**: which fields are included (e.g., name, franchiseGroupName, hours)

== Example of Customization ==
- Changing:
    ```json
    "first": 1
    ```
    returns only one restaurant node.
- Changing:
    ```json
    "searchRadius": 20000,
    "first": 2000
    ```
    could return nearly all restaurants in a region or country.
- Warning: Abusing these endpoints (e.g. requesting everything at once) may violate fair use.

== Summary ==
- APIs reduce fragility, improve speed, and offer better control.
- Whenever an API is discoverable and accessible, it's generally a **preferred scraping method** over parsing HTML.
- Pairing APIs with Python lets you:
    - Easily automate dynamic queries
    - Handle large volumes of clean data
    - Avoid brittle DOM parsing logic

== Next ==
- Explore how to reshape GraphQL responses and introduce filtering logic in Python scrapers.
"""
