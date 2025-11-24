# importing classes 
class Me:
    def __init__(self, name="shade", age="21"):
        self.name = name
        self.age = age
    def Getname(self):
        return self.name
    def Setname(self, name):
        self.name = name
    def Getage(self):
        return self.age
    def Setage(self, age):
        self.age = age
    def __str__(self):
        return "{0} is aged {1}.".format(self.name, self.age)

#from classes19 import Me

person = Me()
print(person.Getname())
print(person.Getage())

person.Setname("Bisola")
person.Setage("22")

print(person)

#inheritance
class Animal:
    def __init__(self, name="", age=0, type=""):
        self.name = name
        self.age = age
        self.type = type
    def getname(self):
        return self.name
    def setname(self, name):
        self.name = name
    def getage(self):
        return self.age
    def setage(self, age):
        self.age = age
    def gettype(self):
        return self.type 
    def settype(self, type):
        self.type = type
        
    def __str__(self):
        return "{0} is aged {1} and is of type{2}".format(self.name, self.age, self.type)   
    
    
    
    
class Chicken(Animal):
    def _init_(self, name="", age=0):
        super.__init__(name, age,  "chicken")
        
    def settype(self, type):
        print( "Sorry {0} will always be a {1}".format(self.name, self.type))
    def makesound(self):
        print("{0} make the sound chuck chuck chuck!".format(self.name))
        
#from classescont20 import Chicken

mychick =Chicken("sally", 12)
print(mychick)

mychick.setage(mychick.getage() + 1)
print(mychick)

mychick.settype("Gorilla")  # Will print warning

mychick.makesound()

class FormatData:
    def __init__(self, Name="", Age=0, Married=False):
        self.Name = Name
        self.Age = Age
        self.Married = Married

    def __str__(self):
        OutString = "'{0}', {1}, {2}".format( self.Name, self.Age,self.Married)
        return OutString
    def to_list(self):
        return [self.Name, self.Age, self.Married]
#from file21 import FormatData
NewData = [FormatData("George", 65, True),
           FormatData("Sally", 47, False),
           FormatData("Doug", 52, True)]
for entry in NewData:
    print(entry)