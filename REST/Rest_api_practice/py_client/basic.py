import requests

endpoint = "http://127.0.0.1:8000/api/" # 127.0.0.1


get_response = requests.post(endpoint, data={'title': 'Brush', 'price': 10.00, 'sale_price': 5.00})

#http request returns HTML
#Rest API Http request returns JSON
#JavaScript Object Notation

print(get_response.json())
print(get_response.status_code)