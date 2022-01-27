from collections import OrderedDict

print("This is a Dict:\n")
a = dict()
a['a'] = 1
a['b'] = 2
a['c'] = 3
a['d'] = 4

print("\n Before:\n")
for key, value in a.items():
	print(key, value)
print("\n After: \n")
a['c'] = 5
for key, value in a.items():
	print(key, value)

print("\nThis is an Ordered Dict:\n")
b = OrderedDict()
b['a'] = 1
b['b'] = 2
b['c'] = 3
b['d'] = 4

print("\n Before:\n")
for key, value in b.items():
	print(key, value)
print("\n After: \n")
b['c'] = 5
for key, value in b.items():
	print(key, value)