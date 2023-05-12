import requests
import json

response = requests.get('http://httpbin.org/get')
obj = json.loads(response.text)
print(response["headers"])