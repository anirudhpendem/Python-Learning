import json

fileobj = open("demo_testfire_v1.json","r")

data = json.load(fileobj)

print(type(data))
#print(data)

#print(data['name'])
#print(data['description'])
#print(data['variables'])
#print(data['order'])
for x in data['requests']:
	print(x['id'])
	print(x['name'])
	print("*****************")
	#for y in x['headerData']:
		#print(y['key'])
		#print(y['value'])
		#print("********************")