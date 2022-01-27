
import re

regx =("((http|https)://)|(www.)?"+"[a-zA-Z0-9@:%._\\=//&?#~+]"+"{2,}\\.[a-zA-Z]"+"{2,}\\b([a-zA-Z0-9@:%"+"._\\+~#?&//=]*)")
	
match = re.compile(regx)

Url = input("Enter the Url:")
	
if(re.search(match,Url)):
	print("Url is valid")
else:
	print("Url is not valid")

