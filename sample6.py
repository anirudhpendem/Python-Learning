import json

fileobj = open("newproject123.txt","r") 

data = json.loads(open("newproject123.txt","r").read())

dat = json.loads(data)

my_list =[]

#print(dat)

#print(type(dat))

for x in dat:
	#print(x['id'],x['api_method'],x['api_url'],x['body'],x['resource_headers'])
	my_dict = {'id' : x['id'],'api_url' : x['api_url'], 'body' : x['body']}

	#print(my_dict)
	#print(type(my_dict))
	my_list.append(my_dict)

print(my_list)
print(type(my_list))

fileobj.close()


"""import requests

url = "http://testfire.net/api/login"

body = {"username" : "jsmith", "password" : "demo1234"}

res = requests.post(url,json = body)

print(res.status_code)
print(res.content)"""