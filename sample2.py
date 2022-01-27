import json
fileobj = open("demo_testfire_v1.json", "r")
data = json.load(fileobj)
#print(type(data))
for i in data['requests']:
	if i['method'] == 'POST':
		print(i['url'])
	#print(i['name'])
	#print(i['url'])
	'''for j in i['headerData']:
		print(j['key'])
		print(j['value'])'''

fileobj.close()