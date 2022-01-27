import requests
import xmltodict
response = requests.get("https://www.w3schools.com/xml/books.xml")

data = xmltodict.parse(response.content)
#print(data)
#print(type(data))
xml_list = []
for i in data['bookstore']['book']:
	res = {'Author' : i['author'], 'Title' : i['title']['#text'], 'Category' : i['@category'],'Year' : i['year'], 'Price' : i['price']}
	xml_list.append(res)
print(xml_list)