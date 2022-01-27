
from collections import UserString
	
class Mystring(UserString):
	
	def append(self, s):
		self.data += s
		
	def remove(self, s):
		self.data = self.data.replace(s, "")
	
s1 = Mystring("Entersoft")
print("Original String:", s1.data)

s1.append(" company")
print("String After Appending:",s1.data)

s1.remove("Entersoft")
print("String after Removing:", s1.data)
