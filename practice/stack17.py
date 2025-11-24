#creating and working on a stack
Mystack = []
Stacksize = 3
def Displaystack():
    print("Stack currently contains: ")
    for item in Mystack:
        print(item)

def Addstack(value):
    if len(Mystack) < Stacksize:
        Mystack.append(value)
    else:
        print("Stack is full")
def Popstack():
    if len(Mystack) > 0:
        print(Mystack.pop())
    else:
        print("My stack is empty")
Addstack(1)
Addstack(2)
Addstack(3)
Displaystack()
input("Press any key when ready...")
Addstack(4)
Displaystack()
input("Press any key when ready...")
Popstack()
Displaystack()
input("Press any key when ready...")
Popstack()
Popstack()
Popstack()
Displaystack()
