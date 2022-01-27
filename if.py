a = int(input("Enter tha value of a:"))

b = int(input("Enter the value of b:"))

c = int(input("Enter the value of c:"))

if a > b and a > c:

	print(" a is greather than b and c")

elif b > c and b > a :

	print(" b is grather than a and c")

elif c > a and c > b:

	print(" c is greather than a and b")
	
else:
		
	print("Values are not unique")