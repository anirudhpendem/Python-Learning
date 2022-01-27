import xml.etree.ElementTree as ET

root = ET.Element("head")
b1 = ET.Element("body1")
root.append(b1)
b2 = ET.Element("body2")
root.append(b2)

name = ET.SubElement(b1,"Name")
name.text ="ANIRUDH"

age = ET.SubElement(b1,"Age")
age.text = "25"

name = ET.SubElement(b2,"Name")
name.text = "Entersoft"

age = ET.SubElement(b2,"Age")
age.text = "30"

tree = ET.ElementTree(root)

file = open("sample.xml","wb+")
tree.write(file)
