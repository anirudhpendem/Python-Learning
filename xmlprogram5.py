import json
import xmltodict

file = open("customers.xml")
data = xmltodict.parse(file.read())
json_data = json.dumps(data)
json_dat = json.loads(json_data)
print(type(json_data))
print(type(json_dat))
print(json_data)
print(json_dat)
