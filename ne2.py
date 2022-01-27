import requests
import json
url = "https://httpbin.org/post"

response = requests.post(url)

print("Status Code :", response.status_code)
#print("Response Content :",response.content)
#print("JSON Response:  ", response.json())
print("Response Text :",response.text)