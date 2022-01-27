import xml.etree.ElementTree as ET
tree = ET.parse(r"C:\Users\aniru\Downloads\books.xml")
root = tree.getroot()
#print(root)
tag = root.tag
print("Root tag:",tag,"\n")

def book():
	for x in root.findall('book'):
		#print(x)
		a = 'price'
		if(a=='id'):
			att = x.get('id')
			print("ID of book:",att)
		elif(a=='author'):
			att = x.find('author').text
			print("Author of book:",att)
		elif(a=='title'):
			att = x.find('title').text
			print("Title of book:",att)
		elif(a=='genre'):
			att = x.find('genre').text
			print("Genre Book:",att)
		elif(a=='price'):
			att = x.find('price').text
			print("Price of the book:",att)
		elif(a=='publish_date'):
			att = x.find('publish_date').text
			print("Publish date of book:",att)
		else:
			att = x.find('description').text
			print("Book description:",att)
book()



