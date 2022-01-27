"""
# *****************Encapsulation***********
class Employee:

    def __init__(self, n,a,c):
        self.name = n          # data-variables
        self.age = a 
        self.company = c

    def display(self):         # methods
        print("Name : ", self.name, "Age :",self.age)

    def show(self):
        print(self.name, 'is working at', self.company)

obj = Employee('Anirudh',24,'Entersoft')
obj.display()
obj.show()

"""
# ***************Data Hiding**************

class Employee:

    def __init__(self, n,c,l):
        self.name = n          # public member 
        self.__company = c     # private member
        self._location = l     # Protected member

    def show(self):
        print("Name: ", self.name, "Company :",self.__company, "Location :",self._location)

obj = Employee('Anirudh','Entersoft','Hyderabad')

obj.show()
