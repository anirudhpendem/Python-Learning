import requests
import xml.etree.ElementTree as ET

response = requests.get("https://www.w3schools.com/xml/books.xml")
#print(response.content)
data = response.content
print(type(data))
tree = ET.fromstring(data)
#print(tree)
ET.dump(tree)

