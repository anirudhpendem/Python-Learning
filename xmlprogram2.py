import requests
import xml.etree.ElementTree as ET

r = requests.get("https://httpbin.org/xml")
print(r.content)

root = ET.fromstring(r.content)
tag = root.tag
print("Root tag:",tag)
#for a in root.findall('slide'):
	#print(a)
for b in root:
	att = b.attrib
	print(att)
	att = b.get('type')
	print(att)
	att = b.find('title').text
	print(att)
	
