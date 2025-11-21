a = 2
b = 5
c = 3

sum = a+b
diff = b-a
prod = a*c
quot = b/a
quot2 = b//a
exp = a**c
mod = b%c

print("Sum: ", sum)
print("Difference: ", diff) 
print("Product: ", prod)
print("Quotient: ", quot)
print("Quotient2: ", quot2)
print("Exponent: ", exp)
print("Modulus: ", mod)

res = a == b
res2 = c != b
res3 = a > c
res4 = a < b
res5 = a >= c
res6 = a <= b
res7 = (a + c) == b
print("Equal: ", res)
print("Not Equal: ", res2)
print("Greater than: ", res3)
print("Less than: ", res4)
print("Greater than or Equal: ", res5)
print("Less than or Equal: ", res6)
print("Combined Equal: ", res7)

# Logical Operators
# AND, OR, NOT
# And operator returns True if both conditions are True
# Or operator returns True if at least one condition is True
# Not operator returns the opposite of the condition
res8 = (a < b) and (c < b)
res9 = (a > b) or (c < b)
res10 = not(a < b)
print("Logical AND: ", res8)
print("Logical OR: ", res9)
print("Logical NOT: ", res10)