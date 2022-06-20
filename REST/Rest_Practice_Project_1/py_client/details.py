import requests

endpoint = "http://127.0.0.1:8000/users/detail/4"


post_response = requests.get(endpoint)

print(post_response.json())