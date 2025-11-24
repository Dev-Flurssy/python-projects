# statements in python

# if statement can execute a block of code based on a condition
# it can execute single or multiple statement when condition is true
# it can combine multiple condition into a single decision and execute one or more statement if the combined condition is true

#using if to check the course enrolled
totalCourse = 8
if totalCourse == 8:
    print("You are enrolled in 8 courses.")
print()   
 
#using indentation to define a block of code
if totalCourse > 5:
    print("You have a heavy course load this semester.")
    print("Make sure to manage your time effectively.") 
print()

#using and operator to combine multiple conditions
course = input("Enter the name of course: ")
grade = input("Enter the score of course: ")

if course == "Mathematics" and int(grade) >= 90:
    print(f"You have excelled in {course}! and got a total score of {grade}.")
print()

#using and to check validity of a number within a range
value = int(input("Enter a number between 1 and 10: "))
if (value >= 1) and (value <=10):
    print(f"You have entered a valid number: {value}")
print()

#if-else statement to execute one block of code if condition is true and another block if condition is false
#else clause is executed when the if condition is false

# using if-else to check status
marks = int(input("Enter your marks: "))
if marks >= 50:
    print("Congratulations! you have passed the exam.")
else:
    print("You have failed the exam")
print()

#elif is a combination of else and if with allowing different range of values

#using elif to pick a menu from a restaurant offerred menu
menu = input("Please enter desired menu from the list provided to you: ")
if menu == "Eggs":
    print(f"Toast and {menu} coming right up!")
elif menu == "Waffles":
    print(f"Tea and {menu} coming right up!")
elif menu == "Cake":
    print(f"Icecream and {menu} coming right up!")
elif menu == "Oatmeal":
    print(f"Coffe and {menu} coming right up!")
elif menu == "Sandwich":
    print(f"Juice and {menu} coming right up!")
else:
    print("We dont have the menu currently, please try again")
print()

#nested statements 

#lets check if we have an incorrect value
one = int(input("please enter number from 1 to 10: "))
two = int(input("please enter number from 1 to 10: "))
if (one >= 1) and (one <= 10):
    if(two >= 1) and (two <= 10):
        print(f"sum of {one} * {two}: ", one*two)
    else:
        print("incorrect second value")
else:
    print("Incorrect first value")
print()

# lets calculate the attendance and exam score 
score1 = int(input("please enter score from 1 to 100: "))
score2 = int(input("please enter score from 1 to 100: "))
score = (score1 + score2)/2
attendance1 =  int(input("please enter attendance from 1 to 100: "))
attendance2 = int(input("please enter attendance from 1 to 100: "))
attendance = (attendance1 + attendance2)/2
if attendance >= 70:
    if score >= 90:
        print("Excellent! you passes with distinction")
    elif score >=70:
        print("Great Job, you passed with good grades")
    elif score >= 50:
         print("Good Job, You passed")
    else:
        print("Sorry, you failed")
else:
    print("Sorry attendance is low, You didnt write exams")
print()


