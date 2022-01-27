class Dispaly:
	try:
		a,b = 50,80
		def method(n):
			print("Show message")

	except AttributeError:
		obj = Dispaly()
		print(obj.a,obj.b,obj.c)
		obj.method()
	print("Exception Attribute Error")
