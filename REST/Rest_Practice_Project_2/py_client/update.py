from turtle import update
import requests

endpoint = "http://127.0.0.1:8000/api/user/update/1/"

data = {
    'first_name': 'John',
    'last_name': 'Doe',
    'email': 'rest_ahre@gmail.com',
    'password': '123456',
}


update_user = requests.put(endpoint, data=data)

print(update_user.json())