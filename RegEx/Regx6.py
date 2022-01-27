import re
regx = r"^[A-Z]{4}0[A-Z0-9]{6}$"
match = input("Enter IFSC code :")

if(re.findall(regx,match)):
	print("valid")

else:
	print("not valid")