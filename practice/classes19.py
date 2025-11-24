class Myclass:
    a = 0
A = Myclass()
print(A.a)
print(A.__class__)
print(dir(A))

#defining a method within a class
class Myclass2:
    def Sayhello():
        print("Hello there!")
        
print(Myclass2.Sayhello())

        
#defining an instance method(it is a method that can only be called by intantiating the class)
class Myclass3():
    def Saybye(self):
        print("Bye Bye!")

B = Myclass3()
print(B.Saybye())

#constructors in class
class Hey:
    greetinngs = ""
    def __init__(self, name="There"):
        self.greetinngs = name + "!"
    def Sayhello(self):
        print("Hello, {0}".format(self.greetinngs))
        
hi = Hey()
print(hi.Sayhello())
hy = Hey("Amy")
print(hy.Sayhello())


class Hi:
    greetings = ""

    def Sayhello(self):
        print("Hello, {0}".format(self.greetings))
        
Hi.Sayhello = "Bisi"
print(Hi.Sayhello)

class Doadd:
    def add(self, a=2, b=4):
        sum = a + b
        print("The sum of {0} and {1} is {2}.".format(a, b, sum))
c = Doadd()
c.add()
c.add(12, 3)
print()

#using variable list argument
class List:
    def list1(*args):
        for count, item in enumerate (args):
            print("{0} likes {1}".format(count, item))
    def list2(**kwargs):
        for name, value in kwargs.items():
            print("{0} like {1}.".format(name, value))
            
print(List.list1("red", "green", "blue"))
print(List.list2(George="Red", Sue="Blue", Zarah="Green"))
print()

# overloading the operator
class MyClass:
   def __init__(self, *args):
      self.Input = args

   def __add__(self, Other):
      Output = MyClass()
      Output.Input = self.Input + Other.Input
      return Output

   def __str__(self):
      Output = ""
      for Item in self.Input:
         Output += Item + " "
      return Output

Value1 = MyClass("Red", "Green", "Blue")
Value2 = MyClass("Yellow", "Purple", "Cyan")
Value3 = Value1 + Value2

print("{0} + {1} = {2}".format(Value1, Value2, Value3))
print()

