student= {
    "jerry": "python",
    "lily": "data analysis",
    "michael": "ai engineering",
    "duke": "software engineering",
    "lana": "cybersecurity expert"
}
print(student)
print(student["duke"])
print(student["lana"])
for s in student:
    print(f"{s}: ", student[s])
print()
print(student.keys())
print()

#updating the content of the dictionary
student["jerry"] = "data science"
student["lily"] = "robotics"
print(student)
print(len(student))
del student["jerry"]
print(len(student))
student.clear()
print(len(student))

# using a dictionary to simulate a switch statement
def blue():
    print("you picked the blue color!")

def pink():
    print("you picked the pink color!")


def grey():
    print("you picked the grey color!")


def purple():
    print("you picked the purple color!")


def orange():
    print("you picked the orange color!")

ColorSelect = {
    0: blue,
    1: pink,
    2: grey,
    3: purple,
    4: orange
}
selection = 0
while(selection!=5):
    print("0. Blue")
    print("1. Pink")
    print("2. Grey")
    print("3. Purple")
    print("4. Orange")
    print("5. Quit")
    selection = int(input("Please select a number: "))
    if(selection>+0) and (selection<=4):
        print(ColorSelect[selection]())
    elif selection == 5:
        print("Goodbye!")
    else:
        print("Invalid choice, please try again.")