import re
regx = r"([a-zA-Z]:\\.*\w)"
match = re.compile(regx)
File_name = input("Enter the File Path:")
if(re.search(match,File_name)):
	print("Regular expreesion pattern is valid")
else:
	print("Regular expression Pattern is not valid")

#https://regex101.com/r/6qHYNG/1