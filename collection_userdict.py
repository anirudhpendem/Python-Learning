
from collections import UserDict
	
class MyDict(UserDict):
		
	"""def pop(self, s = None):
		raise RuntimeError("Deletion not allowed")
"""
	def update(self, s = None):
		raise RuntimeError("Insertion not allowed")
	
d = MyDict({'a':1,'b': 2,'c': 3})

"""print("Current dictionary:",end =" ")
print(d)
print("After Deletion in dictionary:",end =" ")
d.pop(1)
print(d)

"""
print("Current dictionary :",end =" ")
print(d)
print("After Insertion in dictionary:",end =" ")
d.update({'d':4})
print(d)
