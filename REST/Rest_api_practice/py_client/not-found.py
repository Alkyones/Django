import requests

endpoint = "http://127.0.0.1:8000/api/products/13213123131312" # 127.0.0.1


get_response = requests.get(endpoint)

#http request returns HTML
#Rest API Http request returns JSON
#JavaScript Object Notation

print(get_response.json())
print(get_response.status_code)