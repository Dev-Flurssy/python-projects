# Membership Operators
# in, not in
# Used to test if a sequence is present in an object
fruits = ["mango", "peach", "banana"]

print(fruits)
print("mango" in fruits)
print("grape" not in fruits)
print("apple" in fruits)
print("banana" not in fruits)

print()
# Identity Operators
# is, is not
# Used to compare the memory locations of two objects
a = [3, 0, 7]
b = a
c = [3, 0, 7]
x = 5
y = x
z = 5
print(a is b)        # True, because a and b refer to the same object
print(a is c)        # False, because a and c refer to different objects with same content
print(a is not c)    # True, because a and c refer to different objects
print(b is not c)    # True, because b and c dont have the same value
print(x is y)        # True, because x and y refer to the same object
print(x is z)        # False, because x and z refer to different objects with same content
print(x is not z)    # True, because x and z refer to different objects