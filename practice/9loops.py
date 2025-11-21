#loops
# for loops execute a loop a fixed amount of time

#using for loop to iterate through a word
for letter in "Welcome":
    print(letter)
print()

# using for loop to iterate
letternum = 1
for letter in "Hello":
    print(f"Letter {letternum}: {letter}")
    letternum += 1
print()

#breaks is used to end a loop before it has looped through all items

#using break to exit a loop when a condition is met
value = input("please enter less than 6 characters: ")
letternum = 1
for letter in value:
    print(f"{value} {letternum} is: {letter}")
    letternum +=1
    if letternum >6:
        print("character is too long")
        break
print()

#continue is used to skip an iteration of a loop when a condition is met

#using continue to continue to next iteration when condition is met
word = "Welcome"
for letter in word:
    if letter == "o":
        print("o was encountered and unproceesed")
        continue
    print(f"{word} {letternum} is: {letter}")
    letternum +=1
print()

#using continue to skip even numbers
for number in range(1,11):
    if number % 2 ==0:
        continue
    print(f"Odd number: {number}")

    
# Improper understanding of else with for loops
# else block after for loop is executed when loop is not terminated by break statement
special = input("Type less than 6 characters: ")
LetterNum = 1
for Letter in special:
   print(f"{special} {letternum} is: {letter}")
   LetterNum+=1
else:
    print("The string is blank.")

# while loops execute a loop while a condition is true
# using while loop to iterate until condition is false

#using while to count
count = 1 
while count <= 5:
    print(f"Count is: {count}")
    count += 1
print() 