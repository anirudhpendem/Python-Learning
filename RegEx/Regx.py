import re
def main():
	regx = re.compile(r"(\d{1,4}\s\d{1,4}\s\d{1,4}\s\d{1,4})")
	regx1 = re.compile(r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})")
	regx2 = re.compile(r"([A-Z]{5}\d{4}[A-Z]{1})")
	file = open(r"C:\Users\aniru\OneDrive\Desktop\sample.txt")
	for i in file:
		if(regx.findall(i)):
			print(i)

main()



