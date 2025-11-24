print('Hello There (Single Quote)!')
print("Hello There (Double Quote)!")
print("""This is a multiple line string using triple double quotes. 
You can also use triple single quotes.""")
print()

# \ displays new line, \\ displays a slash, \' displays a single quote, \" displays a double quote
print("Part of this text\r\nis on the next line.")
print("This is an A with a grave accent: \xC0.")
print("This is a drawing character: \u2562.")
print("This is a pilcrow: \266.")
print("This is a division sign: \xF7.")
print()

# string 
Mystring = "Hello Dear"
Mystring2 = "Welcome to Python"
String3 = Mystring[:6] + Mystring2[:7]
print(Mystring[0])
print(Mystring[0:5])
print(Mystring2[:7])
print(String3)
print(Mystring2[:8]*5)
print()

MyString = "  Hello World  "

print(MyString.upper())
print(MyString.strip())
print(MyString.center(21, "*"))
print(MyString.strip().center(21, "*"))
print(MyString.isdigit())
print(MyString.istitle())
print(max(MyString))
print(MyString.split())
print(MyString.split()[0])
print()

SearchMe = "The apple is red and the berry is blue!"
print(SearchMe.find("is"))
print(SearchMe.rfind("is"))
print(SearchMe.count("is"))
print(SearchMe.startswith("The"))
print(SearchMe.endswith("The"))
print(SearchMe.replace("apple", "car")
    .replace("berry", "truck"))
print(SearchMe)
print()

# formatting strings
Formatted = "{:d}"
print(Formatted.format(7000))
Formatted = "{:,d}"
print(Formatted.format(7000))
Formatted = "{:^15,d}"
print(Formatted.format(7000))
Formatted = "{:*^15,d}"
print(Formatted.format(7000))
Formatted = "{:*^15.2f}"
print(Formatted.format(7000))
Formatted = "{:*>15X}"
print(Formatted.format(7000))
Formatted = "{:*<#15x}"
print(Formatted.format(7000))
Formatted = "A {0} {1} and a {0} {2}."
print(Formatted.format("blue", "car", "truck"))
