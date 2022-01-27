year = int(input("Enter the year:"))

if((year % 400 == 0) or (year % 4 == 0) and (year % 100 != 0)):

	print("%d is a leap year " %year)

else:

	print("%d is not a  leap year" %year)
