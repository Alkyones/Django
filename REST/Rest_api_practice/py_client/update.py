import requests

endpoint = "http://127.0.0.1:8000/api/products/4/update/" # 127.0.0.1

data = {
    "title": "New Title",
    "content": "New Content",
    "price": 11.22,
}

get_response = requests.put(endpoint, json = data)

#http request returns HTML
#Rest API Http request returns JSON
#JavaScript Object Notation

print(get_response.json())
print(get_response.status_code)