from os import preadv
from warnings import resetwarnings
import requests


endpoint = "http://127.0.0.1:8000/api/user/delete/1/"

delete_request = requests.delete(endpoint)

print(delete_request.status_code) 


