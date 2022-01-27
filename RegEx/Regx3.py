
import re

regx = r"^\d{10}$"

match = re.compile(regx)

PhoneNumber = input("Enter the Phone Number:")

if (re.search(match,PhoneNumber)):
	print ("Valid Number")	
else :
	print ("Invalid Number")



