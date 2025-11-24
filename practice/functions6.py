def sayHi():
    return "Welcome, dear user!"
print(sayHi())
print()

def greetings(name):
    return "Hello, " + name + "!"
print(greetings("Bisola"))
print()

def hello(greeting ="Hello World"):
    return greeting + "!!!"
print(hello())
print(hello("Hi there"))
print()


def  counts(a, *Varargs):
    print("The first argument is: ", a)
    print("The number of additional arguments is: ", len(Varargs))
    print("The last arguments is: ", Varargs[-1])
    for arg in Varargs:
        print("Another argument is: ", arg)
        
counts(1, 2, 3, 4, 5)
print()
