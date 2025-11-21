# lets Build a Lunch Menu Program
print("1. Rice")
print("2. Pasta")
print("3. Burger")
print("4. Salad")

MainChoice = int(input("Choose a lunch item: "))

# Setting the meal name for pasta or burger
if MainChoice == 2:
    Meal = "Pasta"
elif MainChoice == 3:
    Meal = "Burger"

if MainChoice == 1:
    print("1. Chicken Stew")
    print("2. Beef Stew")
    print("3. Vegetable Sauce")
    print("4. Pepper Stew")
    Stew = int(input("Choose a type of stew: "))

    if Stew == 1:
        print("You chose rice with chicken stew.")
    elif Stew == 2:
        print("You chose rice with beef stew.")
    elif Stew == 3:
        print("You chose rice with vegetable sauce.")
    elif Stew == 4:
        print("You chose rice with pepper stew.")
    else:
        print("We have rice, but not that stew type.")

elif (MainChoice == 2) or (MainChoice == 3):
    print("1. Cheese Sauce")
    print("2. Barbecue Sauce")
    print("3. Tomato Sauce")
    Sauce = int(input("Choose a sauce: "))

    if Sauce == 1:
        print("You chose " + Meal + " with cheese sauce.")
    elif Sauce == 2:
        print("You chose " + Meal + " with barbecue sauce.")
    elif Sauce == 3:
        print("You chose " + Meal + " with tomato sauce.")
    else:
        print("We have " + Meal + ", but not that sauce.")

elif MainChoice == 4:
    print("You chose a fresh salad.")

else:
    print("We don't serve that lunch item!")
