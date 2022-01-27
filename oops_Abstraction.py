from abc import ABC,abstractmethod       # Abstract Module (abc)

class Polygon(ABC):        # Abstract class
	try:
		@abstractmethod    # decorator
		def square(self,s):    # abstract method
			self.suare = s
			None
		@abstractmethod
		def rectangle(self,l,w):
			self.length = l
			self.width = w
			None
		@abstractmethod
		def triangle(self,b,h):
			self.base = b
			self.height = h
			None
		@abstractmethod
		def parallelogram(self,b,h):
			self.base = b
			self.height = h
			None
	except:
		print("An error occured")

class Area(Polygon):      # concrete class
    try:
    	def square(self,s):
    		area = s*s
    		print("Area of Square :",area)
    	def rectangle(self,l,w):
    		area = l*w
    		print("Area of rectangle :",area)
    	def triangle(self,b,h):
    		area = 0.5*b*h
    		print("Area of triangle :",area)
    	def parallelogram(self,b,h):
    		area = b*h
    		print("Area of parallelogram :",area)
    except:
    	print("An error occured")

obj = Area()
obj.square(4)
obj.rectangle(5,6)
obj.triangle(7,8)
obj.parallelogram(8,9)
	
	
