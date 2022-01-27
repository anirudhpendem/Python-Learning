import json

fileobj = open("demo_testfire_v1.json","r")
my_data = json.load(fileobj)
#my_data = json.load(open("demo_testfire_v1.json","r").read())
for x in my_data['requests']:
	if x['method'] == 'POST':
			print(x['name'])
			print(x['headers'])
			print("*************************************")

fileobj.close()