from email.encoders import encode_quopri
import requests

enpoint = 'http://127.0.0.1:8000/api/user/create/'

data = {
    'first_name': 'John',
    'last_name': 'Doe',
    'email': 'asfa@gmail.com',
    'password': '123456',
}

post_request = requests.post(enpoint, data=data)
print(post_request.json())

