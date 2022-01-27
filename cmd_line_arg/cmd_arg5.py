import sys
num =1
if len(sys.argv) == 2:
	num = int(sys.argv[1])

for i in range(num):
	print("Command line Argument")
