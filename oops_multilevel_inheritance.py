class Emp(): 
 
   def name(self,n): 
      self.name = n
      print("Employee Name :",n)
 
class Company(Emp):
   
   def company_name(self,c):
      self.company_name = c
      print ("Company Nmae :",c)
 
class Place(Company):
  
   def place_name(self,p):
      self.place_name = p
      print ("Place Name :",p)
 
obj = Place()
obj.name('Anirudh')
obj.company_name('Entersoft')
obj.place_name('Hyderabad')