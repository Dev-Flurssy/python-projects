# errors at specific times compile-time vs runtime 
# compile occurs when a program is run before the computer can execute it,
# runtime occurs while the program is running,

# specific type of errors
# syntax errors - mistakes in the use of the programming language or grammar
# logical errors - mistakes in the program's logic that lead to incorrect results
# runtime errors - errors that occur while the program is running, often due to invalid operations
# semantic errors - errors where the code runs without crashing but produces incorrect results, a loop that runs too many times

try:
    value = int(input("Enter a number between 1 to 10: "))
except ValueError:
    print("please enter a number between 1 and 10")
else:
    if (value > 0) and (value <= 10):
        print("you typed: ", value)
    else:
        print("the value you typed is incorrect")
print()

#without stating value error
try:
    value = int(input("Enter a number between 1 to 10: "))
except :
    print("please enter a number between 1 and 10")
else:
    if (value > 0) and (value <= 10):
        print("you typed: ", value)
    else:
        print("the value you typed is incorrect")

#using the system to get an error information
import sys
try:
    file = open('file.txt')
    print("file opened as expected")
except IOError as e:
    print("Error opening file\r\n"
          f"Error Number: {e.errno}\r\n"
          f"Error text: {e.strerror}")
    print()
    
# printing error in lines
import sys
try:
    file = open('file.txt')
except IOError as e:
    for arg in e.args:
        print(arg)
else:
    print("File opened as expected")
    file.close()
print()

# using system to obtain a list of arguments
import sys
try:
    file = open('file.txt')
except IOError as e:
    for entry in dir(e):
        if(not entry.startswith("-")):
            try:
                print(entry, "=", e.__getattribute__(entry))
            except AttributeError:
                print("Attribute", entry, "not available")
else:
    print("File opened as expected")
    file.close()
print()

# using keyboard interrupt
try:
    a = int(input("Enter a number between 1 to 10: "))
except (ValueError, KeyboardInterrupt):
    print(input("you must enter a number between 1 to 10:"))
else:
    if (a > 0) and (a <= 10):
        print("value: ", a)
    else:
        print("The value you print is incorrect")
print()

# using ctr c to interrupt 

try:
    a = int(input("Enter a number between 1 to 10: "))
except (ValueError, KeyboardInterrupt):
    print(input("you presses ctr c"))
else:
    if (a > 0) and (a <= 10):
        print("value: ", a)
    else:
        print("The value you print is incorrect")
print()