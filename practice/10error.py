sum = 0
while(sum<5):
    print("Sum is:", sum)
    sum += 1
print()

#multiplication table using while loop
num = int(input("Enter a number to display its multiplication table: "))
i = 1
while i <= 10:
    print(f"{num} x {i} = {num*i}")
    i += 1
print()

# muliplication table using for loop
num = int(input("Enter a number to display its multiplication table: "))
for i in range(1,11):
    print(f"{num} x {i} = {num*i}")
print()