class Baseclass:

	def display(self):
		try:
			a = 10
			b = 20
			c = a+ b
			print(c)
		except:
			print("An error occured")

class Derivedclass(Baseclass):
	def show(self):
		print("The additon of two number is:",end = " ")

obj = Derivedclass()
obj.show()
obj.display()