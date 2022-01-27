class Parent:

	def even(self,x):
		self.x = x

		try:
			if x % 1 == 0:
				print(x,"is an even number")
			else:
				print(x,"is an odd number")

		except:
			print("An error occured")

class Child(Parent):

	def even(self,x):
		self.x = x

		try:
			if x % 2 == 0:
				print(x,"is an even number")
			else:
				print(x,"is an odd number")
		except:
			print("An error occured")

obj = Child()

x = int(input("Enter the value of x :"))

obj.even(x)