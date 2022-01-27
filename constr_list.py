import json

"""data_string = '{"name" : "Anirudh","company" : "Entersoft","place" : "HYD"}'

print(type(data_string))

data_dict = json.loads(data_string)

print(type(data_dict))"""

fileobj = open("newproject123.txt","r")

data = json.load(fileobj)

data1 = json.loads(data)

print(type(data))

print(type(data1))

fileobj.close()

