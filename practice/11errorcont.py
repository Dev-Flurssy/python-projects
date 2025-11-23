try:
    a = int(input("Enter a whole number: "))
    b = int(input("Enter a whole number: "))
    average = a/ b
except ValueError:
    print("You must type a whole number")
except KeyboardInterrupt:
    print("You presses ctr c")
except ZeroDivisionError:
    print("Attempt to divide by zero")
except ArithmeticError:
    print("An undefined math error occured")
else:
    print(average)
print()

#nesting of exceptions
TryAgain = True

while TryAgain:
    try:
        value = int(input("Enter a whole number: "))
    except ValueError:
        print("You must enter a whole number")

        DoOver = input("Try again? (Y/N): ").strip()

        if DoOver.upper() == "N":
            print("Ok, See you next time")
            TryAgain = False

    except KeyboardInterrupt:
        print("\nYou pressed Ctrl+C!")
        print("See you next time!")
        TryAgain = False

    else:
        print("You typed:", value)
        TryAgain = False
print()

# how to raise an error
try:
    raise ValueError
except ValueError:
    print("ValueError Exception!")
print()

#how to raise erro
try:
    Ex = ValueError()
    Ex.strerror = "Value must be within 1 and 10."
    raise Ex
except ValueError as e:
    print("ValueError Exception!", e.strerror)
    
class CustomValueError(ValueError):
    def __init__(self, arg):
        self.strerror = arg
        self.args = {arg}
        
try:
    raise CustomValueError("Value must be within 1 and 10.")
except CustomValueError as e:
    print("CustomValueError Exception!", e.strerror)
print()

#using finally
import sys
try:
    raise ValueError
    print("Raising an exception.")
except ValueError:
    print("ValueError Exception!")
    sys.exit()
finally:
    print("Taking care of last minute details.")
   
print("This code will never execute.")