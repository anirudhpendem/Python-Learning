def sum(my_dict):

	sum = 0

	for i in my_dict:

		sum = sum + my_dict[i]

	return sum

my_dict  = {'a' : 10,'b' : 20, 'c' : 50, 'd' : 60}

print("sum = ",sum(my_dict))



"""my_dict = { 'a': 50, 'b': 150 , 'c' : 178 , 'd' : 201}

data = sum(my_dict.values())

print("sum of dictionaries are = ",+data  )
"""