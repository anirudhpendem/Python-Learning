a = int(input("Enter the value of a:"))

try:
	
	if a > 18:

		#print(b)
		print("Age is eligible")
	
	else:
		
		print("Age is not eligible")

except NameError:

	print("Exception Name Error")