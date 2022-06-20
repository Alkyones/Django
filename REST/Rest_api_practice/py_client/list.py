import requests
import getpass
endpoint = "http://127.0.0.1:8000/api/auth/" # 127.0.0.1
username = input("Username: ")
password = getpass.getpass("Password: ")

auth_response = requests.post(endpoint, data={"username": username, "password": password})


if auth_response.status_code == 200:
    token = auth_response.json()["token"]
    print(token)
    headers = {"Authorization": f"Bearer {token}"}

    endpoint = "http://127.0.0.1:8000/api/products/" # 127.0.0.1

    response = requests.get(endpoint, headers=headers)
    print(response.json())

#http request returns HTML
#Rest API Http request returns JSON
#JavaScript Object Notation

print(auth_response.json())
print(auth_response.status_code)