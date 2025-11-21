#input is used to take input from the user

# This is a simple prompt program that collects user information and displays a welcome message.
name = input("Enter your name: ")
age = input("Enter your age: ")
nationality = input("Enter your nationality: ")
print(f"Hello, {name}, you are {age} old and you are a {nationality}! \n Welcome to the Python programming world.")
print()

# a simple voting eligibility checker
def voting_eligibility():
    age = int(input("Please enter your age to check voting eligibility: "))
    if age >= 18:
        print("You are eligible to vote.")
    else:
        print("You are not eligible to vote yet.")
          
voting_eligibility()
print()

# a simple calculator that adds two numbers
def simple_calculator():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = num1 + num2
    print(f"The sum of {num1} and {num2} is {result}.")
    
simple_calculator()
print()