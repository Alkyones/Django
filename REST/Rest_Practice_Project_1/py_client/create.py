import requests

endpoint = "http://127.0.0.1:8000/users/create/"
data = {
    "first_name": "test",
    "email": "dasdsahdha@gmail.com",
    "password": "test",
}

post_response = requests.post(endpoint,data=data)

print(post_response.json())