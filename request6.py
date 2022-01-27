import json
import random
import string
import requests

host_url = "http://testfire.net/api"
#fileobj = open("newproject123.txt","r") 
data = json.loads(open("newproject123.txt","r").read()) 
dat = json.loads(data)
my_list =[]  #print(dat)  #print(type(dat))
for x in dat:  #print(x['id'],x['api_method'],x['api_url'],x['body'],x['resource_headers'])
	my_dict = {'id' : x['id'],'method':x['api_method'],'url' : x['api_url'], 'body' : x['body'],'resource_name' : x['resource_name']} #print(my_dict['resource_name'])  #print(type(my_dict))
	my_list.append(my_dict) #print(my_list) #print(type(my_list))
header = {'Authorization': 'YW5OdGFYUm86WkdWdGJ6RXlNelE9OhU\\/bwA\\/Pz8='}
string = ''.join(random.choices(string.ascii_letters + string.digits , k = 15))
value = header['Authorization'] + (str(string))
print("\t")
modified_token = {'Authorization' : value } #print(modified_token)
for dict_data in my_list:
	my_url = (str(host_url) + dict_data['url']) #print(my_url) #print(dict_data['body'])
	if dict_data['method'] == "GET":
		res = requests.get(my_url,headers = modified_token)
		print(res.status_code)
		print(res.content)
	if dict_data['method'] == "POST":
		res = requests.post(my_url,json=dict_data['body'],headers = modified_token)
		print(res.status_code)
		print(res.content)
