
from collections import ChainMap
		
data1 = {'name1': 'ram', 'name2': 'laxman'}
data2 = {'age1':25 , 'age2': 30}
data3 = {'place1': 'hyd', 'place2': 'sec'}

a = ChainMap(data1, data2, data3)
print(type(a))
print(a)
print(a['name1'],a['age2'],a['place1'])
print(a.keys())
print(a.values())

print("********************************************************")

data1 = {'name1': 'ram', 'name2': 'laxman'}
data2 = {'age1':25 , 'age2': 30}
data3 = {'place1': 'hyd', 'place2': 'sec'}
data4 = {'state': 'Telangana'}

a = ChainMap(data1,data2,data3)

print (" chainmap  are : ")
print (a)

b = a.new_child(data4)

print ("After adding new chainmap : ")
print (b)
