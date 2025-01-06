#Application Programming Interfaces
"""
Definition: An API is a set of rules and protocols for building and interacting with software applications. It allows different software systems to communicate with each other, enabling functionalities such as data retrieval, manipulation, and integration.
Web APIs: These are APIs that operate over the internet, allowing applications to send requests and receive responses through HTTP protocols. Common examples include RESTful APIs, which use standard HTTP methods like GET, POST, PUT, and DELETE.
Purpose: The requests library in Python simplifies the process of making HTTP requests to web APIs. It abstracts away much of the complexity involved in sending requests and handling responses.
"""
import sys
import requests

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple/com/search?entity=song&limit=1&term=" + sys.argv[1])
print(response.json())
