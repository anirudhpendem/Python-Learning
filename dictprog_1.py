
keys = []

values = []

n = int(input("Enter number of elements for dict:"))

print("keys :")

for x in range(0,n):

	ele = str(input("Enter ele " + str(x+1) + ":" ))

	keys.append(ele)

print("value :")

for x in range(0,n):

	ele = int(input("Enter ele " + str(x+1) + ":" ))

	values.append(ele)

my_dict = dict(zip(keys,values))

print("The dict is : " ,my_dict)

#print(my_dict)

print(sum(my_dict.values()))