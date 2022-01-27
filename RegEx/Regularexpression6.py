import re

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+[A-Z|a-z]{2,}\b'

email1 = "anirudhpendem913%@gmail.com"

email2= "Entersoft._company+_@entersoft.org"

email3 = "anirudh326&gmail.in"

if(re.search(regex, email1)):
	print("Valid Email")

else:
	print("Invalid Email")


