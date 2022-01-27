def fun(a,b):
	try:
		c = ((a+b)//(a-b))
		print(c)

	except Exception as e:
		print("Zero division Error Exception")
		#print(e)

	else:
		print("Function argument is success")
	finally:
		print("Program executed")
	
#fun(8,8)
fun(10,5)