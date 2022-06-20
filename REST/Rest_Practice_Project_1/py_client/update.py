import requests

endpoint = "http://127.0.0.1:8000/users/update/4/"

data = {
    "first_name": "test121",
    "email": "dasdsahdha@gmail.com",
    "password": "test2121",
}


post_response = requests.put(endpoint, data=data)

print(post_response.json())