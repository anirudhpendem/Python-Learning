number = int(input("Enter the number :"))

fact = 1

"""
for i in range(1,number+1):

	fact = fact * i

	print(" The factorial of given number is {0} = {1}" .format(number,fact))

"""
i = 1
while(i <=number):

	fact = fact * i

	i = i+1

	print(" The factorial of given number is %d = %d" %(number,fact))

