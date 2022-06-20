import requests

headers = {
    "Authorization": "Bearer d5867133eaa200b1cfcf2b7fcbe15ab8a5b35d76"
}

endpoint = "http://127.0.0.1:8000/api/products/" # 127.0.0.1

data = {'title': 'Hre1', 'price': 20.00, 'sale_price': 5.00}

get_response = requests.post(endpoint, json=data, headers=headers)

#http request returns HTML
#Rest API Http request returns JSON
#JavaScript Object Notation

print(get_response.status_code)