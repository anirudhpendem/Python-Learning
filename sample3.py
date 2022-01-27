import json
import requests
import string
import random

host_url = "http://testfire.net/api"

fileobj = open("newproject123.txt","r")
data = json.loads(open("newproject123.txt","r").read())
my_data = json.loads(data)
#print(my_data)
#print(type(my_data))

my_list =[]
my_body =[]
for x in my_data:
	my_dict = x['api_url']
	#my_dict = x['resource_name']
	body = x['body'] 
	my_list.append(my_dict)
	my_body.append(body)
#print(my_list)
print(my_body)
url = ""
for data_list in my_list:
	url +=host_url + str(data_list) + "\n"
	#url += str(data_list) + "\n"
#print(url)

header = {'Authorization': 'YW5OdGFYUm86WkdWdGJ6RXlNelE9OhU\\/bwA\\/Pz8='}
S = 15
string = ''.join(random.choices(string.ascii_letters + string.digits , k = S))
s = header['Authorization'] + (str(string))
print("\t")
value = s
modified_token = {'Authorization' : value }
#print(modified_token)
"""login = requests.post(url,json=my_body[0],headers = modified_token)
login_status_check = requests.get(url,json=my_body[1],headers = modified_token)
account_info = requests.get(url,json=my_body[2],headers = modified_token)"""
transfer_amount= requests.post(url,json=my_body[3],headers = modified_token)
feedback = requests.post(url,json=my_body[4],headers = modified_token)
"""add_user = requests.post(url,json=my_body[5],headers = modified_token)
admin_changepassword = requests.post(url,json=my_body[6],headers = modified_token)
transfer = requests.post(url,json=my_body[7],headers = modified_token)"""

"""print(login.status_code)
print(login.content)
print(login_status_check.status_code)
print(login_status_check.content)
print(account_info.status_code)
print(account_info.content)"""
#print(transfer_amount.status_code)
#print(transfer_amount.content)
#print(transfer_amount.headers)
#print(feedback.status_code)
#print(feedback.content)
