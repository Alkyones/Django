import requests
import getpass
auth_respons = "http://127.0.0.1:8000/api/"

username = input("Username: ")
password = getpass.getpass("Password: ")

auth_response = requests.post(auth_respons, data={"username": username, "password": password})


if auth_response.status_code == 200:
    token = auth_response.json()["token"]
    print(token)
    headers = {"Authorization": f"Token {token}"}

    endpoint = "http://127.0.0.1:8000/api/user/" #
    response = requests.get(endpoint, headers=headers)
    print(response.json())
    print(response.status_code)
else:
    print('Authentication failed')