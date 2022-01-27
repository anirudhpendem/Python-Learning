from collections import OrderedDict

print("This is a Dict:\n")
a = dict()
a['b'] = 1
a['c'] = 2
a['d'] = 3
a['a'] = 4

for key, value in a.items():
	print(key, value)

print("\nThis is an Ordered Dict:\n")
b = OrderedDict()
b['b'] = 1
b['c'] = 2
b['d'] = 3
b['a'] = 4

for key, value in b.items():
	print(key, value)

print("**********************************************************************************")
print("Order dict before and after deleting")

c = OrderedDict()
c['a'] = 1
c['b'] = 2
c['c'] = 3
c['d'] = 4

print('Before Deleting')
for key, value in c.items():
	print(key, value)
	
c.pop('a')

c['a'] = 1

print('\nAfter re-inserting')
for key, value in c.items():
	print(key, value)

print("****************************************************************")
print("Dict before and after deleting")

d = dict()
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4

print('Before Deleting')
for key, value in d.items():
	print(key, value)

d.pop('a')

d['a'] = 1

print('\nAfter re-inserting')
for key, value in d.items():
	print(key, value)