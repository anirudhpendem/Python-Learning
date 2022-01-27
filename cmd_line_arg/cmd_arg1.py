import sys

n = len(sys.argv)

print("\n Total argumrnts passed:",n)

print("\n Name of python script:",sys.argv[0])

print("\n Argument passed:",end = " ")
for i in range(1,n):
	print(sys.argv[i],end = " ")

sum = 0

for i in range(1,n):
	sum += int(sys.argv[i])

print("\n\n Result :",sum)