import requests
import getpass
endpoint = "http://127.0.0.1:8000/login/"
username = input("Username: ")
password = getpass.getpass("Password: ")

data = {
    'csrfmiddlewaretoken': '',
    'username': username,
    'password': password
}

post_request = requests.post(endpoint, data=data)

if post_request.status_code == 200:
    endpoint = "http://127.0.0.1:8000/main/"
else:
    print("Error: " + str(post_request.status_code))
    print("Access Denied")