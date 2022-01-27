import requests
import json

file = open("anotherdata.txt","r")
data = json.loads(open("anotherdata.txt").read())
my_data = json.loads(data)
#print(type(my_data))
#print(my_data)
#for i in my_data:
#	print( i['api_method'],i['api_url'],i['body']) 

url = "http://testfire.net/api"
header = {"Authorization":"YW5OdGFYUm86WkdWdGJ6RXlNelE9OkE\\/Ei18P2I="}
for i in my_data:
	my_url = (str(url) + i['api_url'])
	#print(my_url)
	if i['api_method'] == 'GET':
		res = requests.get(my_url,json=i['body'],headers = header)
		print(res.status_code)
		print(res.content)
		print('\n')
	if i['api_method'] == 'POST':
		res = requests.post(my_url,json=i['body'],headers = header)
		print(res.status_code)
		print(res.content)
		print('\n')


"""
# Token - Creation
url = "http://testfire.net/api/login"
body = {"username":"jsmith","password":"demo1234"}
res = requests.post(url,json =body)
print(res.content)
"""