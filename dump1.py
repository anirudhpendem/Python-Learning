import json

Dictionary = {1 :'Python', 2 :'Programming',
			3 :'language', 4 :'is',
			5 :'simple', 6 :'too',
			7 : 'understand' }

json_string = json.dumps(Dictionary)

print(json_string)

print("	 ")

print(type(json_string))
