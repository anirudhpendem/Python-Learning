my_dict = {'book' : 50, "pen" : 30 , "pencil" : 20}

try:

	print(my_dict["pen"])

	print(my_dict["name"])

except KeyError:

	print("You entered wrong key which not listed in my_dict ")