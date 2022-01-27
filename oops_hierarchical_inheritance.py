class Parent:

      def fun1(self,a):
        self.a = a
        print("My phone number :",a ,end = "-")

class Child(Parent):
      
      def fun2(self,b):
        self.b = b
        print( b ,end = "-")

class Child2(Parent):
      
      def fun3(self,c):
        self.c = c
        print(c)
 
obj = Child()
obj.fun1(9123)
obj.fun2(456)
obj1=Child2()
obj1.fun3(789)