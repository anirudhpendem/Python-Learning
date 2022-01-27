import sys

def factorial(n):
	if n ==1 :
		return 1
	return n * factorial(n-1)
n = int(sys.argv[1])
fact = factorial(n)
print("Factorial of",sys.argv[1],"is",fact)