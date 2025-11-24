list1 = ["one", 1, "two", True]
print(list1)
dir(list1)
print(list1[1:3])
print(list1[1:])
print(list1[:3])

#looping through a list
items = [0, 1, 2, 3, 4, 5]
for item in items:
    print(item)
print()

#modifying a list
items = []
print("Original Length: ",len(items))
items.append("bag")
print(items)
items.insert(1, "shoes")
print(items)
print()

item2 = items.copy()
print(item2)
item3 = ["hello"]* 3
print(item3)
print()

#practical example
Colors = ["Red", "Orange", "Yellow", "Green", "Blue"]
ColorSelect = ""
while str.upper(ColorSelect) != "QUIT":
    ColorSelect = input("Please type a color name: ")
    if (Colors.count(ColorSelect) >= 1):
        print("The color exists in the list!")
    elif (str.upper(ColorSelect) != "QUIT"):
        print("The list doesn't contain the color.")
print()

#sorting lists
Colors = ["Red", "Orange", "Yellow", "Green", "Blue"]
for Item in Colors:
    print(Item, end=" ")
print()
 
Colors.sort()
Colors.reverse
for Item in Colors:
    print(Item, end=" ")
print()

#working with collections
from collections import Counter
MyList = [1, 2, 3, 4, 1, 2, 3, 1, 2, 1, 5]
ListCount = Counter(MyList)
print(ListCount)
for ThisItem in ListCount.items():
    print("Item: ", ThisItem[0],
          " Appears: ", ThisItem[1])
print("The value 1 appears {0} times."
      .format(ListCount.get(1)))