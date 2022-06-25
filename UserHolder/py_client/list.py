import requests

endpoint = "http://127.0.0.1:8000/users/"


get_request = requests.get(endpoint)
print(get_request.status_code)
print(get_request.json())