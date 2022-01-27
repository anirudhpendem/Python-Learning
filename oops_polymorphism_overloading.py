class Cal:
	
	def area(self, x = None, y = None): #x,y are default parameters

		try:

			if x != None and y != None:
				return x * y
			elif x != None:
 				return x * x
			else:
 				return 0
		except:
			print("Please enter less than 3 arguments only")

obj = Cal()

print("Area of Zero argument:", obj.area())

print("Area of One arugemt:", obj.area(4))

print("Area of two argument:", obj.area(3,5))
