import requests

endpoint = "http://127.0.0.1:8000/api/products/4/delete/" # 127.0.0.1


get_response = requests.delete(endpoint)

#http request returns HTML
#Rest API Http request returns JSON
#JavaScript Object Notation
print(get_response.status_code)