"""import json

url = "http://testfire.net/api"

fileobj = open("file1.txt","r")

data = json.loads(open("file1.txt","r").read())

my_data = json.loads(data)

#print(my_data)

#print(type(my_data))

my_list =[]

for x in my_data:

	my_dict = x['api_url']

	my_list.append(my_dict)

#print((my_list)
s = ""
for data_list in my_list:
	s += url + str(data_list) + "\n"

print(s)"""

import json
import requests

url = "http://testfire.net/api"

fileobj = open("newproject123.txt","r")

data = json.loads(open("newproject123.txt","r").read())

my_data = json.loads(data)

#print(my_data)

#print(type(my_data))

my_list =[]

for x in my_data:

	my_dict = x['api_url']

	my_list.append(my_dict)

#print((my_list)
s = ""
for data_list in my_list:
	s += url + str(data_list) + "\n"

print(s)

fileobj.close()


#print(url.join(map(str,my_list)))






