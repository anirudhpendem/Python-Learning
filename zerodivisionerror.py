
a = int(input("Enter the value of a:"))

b = int(input("Enter the value of b:"))

try:
	c = a // b
	print(c)

except ZeroDivisionError:
	print("a,b result will be 0") 
