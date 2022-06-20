import requests

endpoint = "http://127.0.0.1:8000/api/user/1/"
get_all_users = requests.get(endpoint)

print(get_all_users.json())