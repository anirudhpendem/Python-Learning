import requests
import json

url = "https://httpbin.org/post"

header = {"Content-Type": "application/json; charset=utf-8"}

data = {
	"id": 3333,
	"name": "Anirudh",
	"passion": "Entersoft",
}

response = requests.post(url,json=data,headers=header)

print("Status Code", response.status_code)
#print("JSON Response ", response.json())
#print("Response Content",response.content)
print("Response Text : ",response.text)

