'''import json

url = "https://testfire.net/api"

fileobj = open("newproject123.txt","r")

data = json.loads(open("newproject123.txt","r").read())

my_data = json.loads(data)

#print(my_data)

#print(type(my_data))
my_list =[]

for x in my_data:

	my_dict = x['body']

	my_list.append(my_dict)

#print(my_list)

s = ""
for data_list in my_list:
	s += url + str(data_list) + "\n"

print(s)
fileobj.close()

'''
import requests
import string
import random

url = "http://testfire.net/api/login"
url1 = "http://testfire.net/api/feedback/submit"
url2 = "http://testfire.net/api/transfer"

header = {'Authorization': 'YW5OdGFYUm86WkdWdGJ6RXlNelE9OhU\\/bwA\\/Pz8='}

body = {"username" : "jsmith", "password" : "demo1234"}
body1 = {"name": "J Smith","email": "jsmtih@altoromutual.com","subject": "Amazing web design","message": "I like the new look of your applicaiton"}
my_body = {"data" :[{"username":"mamatha","password":"pwd"}]}
S = 15

string = ''.join(random.choices(string.ascii_uppercase +string.ascii_lowercase + string.digits , k = S))

print("The generated random string : " + str(string))

modified_token = header['Authorization'] + (str(string))

#print(modified_token)

print("\t")

"""modified_token =""
modified_token += str(header) + str(string)
print(modified_token)"""

value = modified_token

my_dict = {'Authorization' : value }
#print(my_dict)

res = requests.post(url,json = body,headers = my_dict)
transfer_amount= requests.post(url,json=my_body,headers = header)
res1 = requests.post(url1,json=body1,headers = my_dict)

#print(res.status_code)
print(res.content)
print(transfer_amount.status_code)
print(transfer_amount.content)
print(res1.status_code)
print(res1.content)





