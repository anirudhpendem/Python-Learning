from collections import UserList
	
class MyList(UserList):
	
	def append(self, s = None):
		raise RuntimeError("Insertion not allowed")
	"""	
	def remove(self, s = None):
		raise RuntimeError("Deletion not allowed")
"""
L = MyList([1, 2, 3, 4])

print("Original List :",end=" ")
print(L)
L.remove(4)
print("After Deletion:",end =" ")
print(L)

L.append(5)


"""
print("Original List :",end=" ")
print(L)
L.append(5)
print("After Insertion:",end =" ")
print(L)

L.remove(5)

"""