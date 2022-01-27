import xml.etree.ElementTree as ET

def update(filename):
	tree = ET.ElementTree(file=filename)
	root = tree.getroot()

	for ages in root.iter("Age"):
		ages.text = "50"

	tree = ET.ElementTree(root)
	file = open(filename,"wb+")
	tree.write(file)

update("sample.xml")
