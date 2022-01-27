import requests
import json

file = open("basictest123.txt","r")
data = json.loads(open("basictest123.txt").read())
my_data = json.loads(data)
#print(type(my_data))
#print(my_data)

url = "http://testfire.net/api"
for i in my_data:
	#print( i['api_method'],i['api_url'],i['body']) 
	my_url = (str(url) + i['api_url'])
	print(my_url)
	