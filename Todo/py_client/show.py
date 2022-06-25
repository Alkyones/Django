import requests

endpoint = "http://127.0.0.1:8000/main/show/"

get_request = requests.get(endpoint)

if get_request.status_code == 200:
    print(get_request.json())
else:
    print("Error: " + str(get_request.status_code))
    print('You need to login or register')
