#modules are codes placed in seperate groupings that can be imported and used in another file
# modules should be grouped according to similarity

#example of a simple module
def SayHi(name):
    print("Hello", name)
    return

def GoodBye(name):
    print("See you next time ", name)
    return

#checking if the folder exists
import os

path1 = r"C:\BPP4D3E-main"
path2 = r"C:\BPP4D3E-main\Chapter10"

# Check first folder
if os.path.exists(path1):
    print(f"{path1} exists!")
else:
    print(f"{path1} does NOT exist.")

# Check second folder
if os.path.exists(path2):
    print(f"{path2} exists!")
else:
    print(f"{path2} does NOT exist.")
