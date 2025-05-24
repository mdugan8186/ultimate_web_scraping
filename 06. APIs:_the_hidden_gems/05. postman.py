# ==== postman ====


#
#
"""
== Objective ==
- Use **Postman** as a visual HTTP client to replicate browser requests with full headers and body.
- Learn how to import `cURL` commands into Postman and inspect or save the requests for later use.

== Why Use Postman ==
- Postman is a **full-featured**, visual HTTP client — widely used in API development and testing.
- Offers more features than lightweight tools like HTTPie:
    - GUI-based request editing
    - Response preview
    - Header organization
    - Request collections and saving
    - Code generation for multiple languages

== Steps to Import a Request ==
1. Copy the request from your browser (DevTools → Right-click → **Copy as cURL**)
2. Open Postman
3. Choose **Import** → **Raw Text**
4. Paste the copied `cURL` command
5. Click **Continue** → **Import**

== After Importing ==
- Postman will:
    - Set the method (e.g., `POST`)
    - Fill in the URL
    - Populate all headers (e.g., User-Agent, Content-Type)
    - Paste the request body (GraphQL or JSON)
- Optional:
    - Save the request (`Cmd+S` or `Ctrl+S`)
    - Add it to a collection for future use
    - Beautify the body for better readability

== Testing the Request ==
- Click **Send**
- Wait for the response:
    - Confirm that you receive the expected JSON
    - Response will display in Postman's interface
    - You can save or export the response if needed

== Postman Features Recap ==
- Organize requests into collections
- Export requests or entire collections
- Save responses for comparison or archiving
- Auto-format body, headers, and raw responses

== Summary ==
- Postman allows point-and-click control of the request pipeline.
- It supports full header emulation and is ideal for exploring or debugging complex API requests.
- Works seamlessly with browser-exported `cURL` commands.

== Next ==
- We'll take the final step and convert this request from Postman (or HTTPie) into **pure Python code**, so that it can be automated in your scripts.
"""
