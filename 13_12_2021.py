import json

fileobj = open("file1.txt","r")

data = json.loads(open("file1.txt","r").read())

my_data = json.loads(data)

#print(my_data)

#print(type(my_data))

my_list =[]

for x in my_data:

	my_dict = {'id' :x['id'],'api_url':x['api_url'],'body':x['body'],'api_method':x['api_method']}

	my_list.append(my_dict)

print(my_list)

