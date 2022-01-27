import json
import requests
import string
import random

url = "https://testfire.net/api"

fileobj = open("newproject123.txt","r")

data = json.loads(open("newproject123.txt","r").read())

my_data = json.loads(data)

#print(my_data)

#print(type(my_data)
my_list =[]

for x in my_data:

	my_dict = x['api_url']

	my_list.append(my_dict)

#print((my_list)
s = ""
for data_list in my_list:
	s += url + str(data_list) + "\n"

#print(s)

url = s

header = {'Authorization': 'YW5OdGFYUm86WkdWdGJ6RXlNelE9Oj80PE0\\/PyY='}

body = {"username" : "jsmith", "password" : "demo1234"}

S = 15

string = ''.join(random.choices(string.ascii_uppercase +string.ascii_lowercase + string.digits , k = S))

print("The generated random string : " + str(string))

print("\t")

modified_token =""

modified_token += str(header) + string

#print(modified_token)

value = modified_token

my_dict = {'Authorization_token' : value }

res = requests.post(url,json = body,headers = my_dict)

#print(my_dict)
print(res.content)


fileobj.close()