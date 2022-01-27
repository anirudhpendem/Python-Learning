class Number:  # Class as Number
   
   def display(self,a,b): # function with self parameter along with a and b
      self.a = a
      self.b = b
      try:

         add = a + b
         sub = a - b
         mul = a * b
         div = a / b
         print("The addition of a and b : ",add)
         print("The subtraction of a and b : ",sub)
         print("The multiplication of a and b : ",mul)
         print("The Division of a and b : ",div)
      
      except ZeroDivisionError:
         print("Change 2nd argument as non-zero")


obj = Number() # Object as obj
obj.display(10,2) # object call








