class Car:

     def brand(self,b):
        self.brand = b
        b = input("Enter the car brand :")
        print("Car brand :",b)
 
class Car_colour(Car):

     def colour(self,c):
        self.colour = c
        c = str(input("Enter the car colour :"))
        print("Car colour :",c)
 
class Car_fuel(Car):
     
     def fuel(self,f):
        self.fuel = f
        f = str(input("Enter the fuel type as Petrol/Diesel/CNG : "))
        print("The fuel type of car :",f)
 
class Car_wheel(Car_colour, Car_fuel):

     def wheel(self,w):
        self.wheel = w
        w = str(input("Enter car wheel type as Disc/Drum : "))
        print("The Wheel type of car : ",w)

obj1 = Car_colour()
obj1.brand('b')
obj2 = Car_wheel()
obj2.colour('c')
obj2.fuel('f')
obj2.wheel('w')