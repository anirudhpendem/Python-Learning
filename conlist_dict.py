"""keys = ["a","b","c","d"]

values = ["10","20","30","40"]

res = list(zip(keys,values))

res1 = dict(zip(keys,values))

print(res)
print(type(res))

print(res1)
print(type(res1))"""

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

my_list = list(zip(keys,values))

print("The list is : " ,my_list)
print(type(my_list))

my_dict = dict(zip(keys,values))

print("The dict is : ", my_dict)
print(type(my_dict))