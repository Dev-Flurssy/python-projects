a = 2
b = 5
c = 3
d = 10
e = 2

# Using basic arithmetic operations to update values
a = a + b - c
b = a * c + b
c = b // a + c

print("Updated a: ", a)
print("Updated b: ", b)
print("Updated c: ", c)

# Using compound assignment operators to update values
c += b - a
print("Final a: ", a)
b -= c + a
print("Final b: ", b)
a *= b + c
print("Final c: ", c)
d /= a + b + c
print("Updated d: ", d)
d %= a + b + c
print("Final d: ", d)
e **= a - b + c
print("Updated e: ", e)
e //= a + b - c
print("Final e: ", e)

#memberhip operators
