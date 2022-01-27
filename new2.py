import requests

url = "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"

response = requests.post(url)

#print(response.text)

print("respone of status is %d", response.status_code)