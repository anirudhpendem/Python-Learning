import xml.etree.ElementTree as ET
tree = ET.parse("customers.xml")
root = tree.getroot()

tag = root.tag
print("root tag :",tag,"\n")

att = root.attrib
print(att,"\n")

for i in root.findall('customer'):
	print("No. of customers elemrnt tokens:",i,"\n")
for c in root:
	att = c.attrib
	print("Customers attribute type:",att,"\n")
for x in root:
	att = x.get('type')
	print("customer type:",att,"\n")
for j in root:
	place = j.find('place').text
	print("Place:",place)
	Amount = j.find('amount').text
	print("Amount:",Amount,"\n")

"""for c in root.findall('customer'):
	print(c)
	att = c.attrib
	print(att)
	t = c.get('type') 
	print(t)
	place = c.find('place').text
	print(place)
	amount = c.find('amount').text
	print(amount)"""