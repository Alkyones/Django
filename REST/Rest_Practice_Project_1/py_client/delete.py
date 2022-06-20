import requests

endpoint = "http://127.0.0.1:8000/users/delete/3/"

post_response = requests.delete(endpoint)

print(post_response.status_code)