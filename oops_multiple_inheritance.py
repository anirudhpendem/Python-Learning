class Base:

	def c1(self,a,b):
		self.a = a
		self.b = b
		try:
			if a > b:
				print(" a is grather than b ")
		except ArithmeticError:
			print("An error occured")
class Derived1:

	def c2(self,a,b):
		self.a = a
		self.b = b
		try:
			if a < b:
				print("b ia grather than a")
		except ArithmeticError:
			print("An error occured")

class Derived2(Base,Derived1):

	def c3(self,a,b):
		self.a = a
		self.b = b
		try:
			if a == b:
				print("Both a and b are equal")
		except ArithmeticError:
			print("An error occured")

obj = Derived2()
obj.c1(10,20)
obj.c2(10,20)
obj.c3(10,20)