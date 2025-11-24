#Note the above was done on the repl so switch to python shell by typing python and enter on your python terminal

#modules are codes placed in seperate groupings that can be imported and used in another file
# modules should be grouped according to similarity
# import is used to import a needed module

#example of a simple module
def SayHi(name):
    print("Hello", name)
    return

def GoodBye(name):
    print("See you next time ", name)
    return
print()

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
print()

#working with directory
#after comfirming a dir chdir is used to change a directory 

import os
os.chdir("C:\BPP4D3E-main")
print(os.getcwd) #this is used to get the current directory
print()


# the current entry will be looped through and printed line by line
for entry in os.listdir(): print(entry)
print()

#import a libray under the folder and print line by line  # from import in first line
# remove the import ("BPP4D3E_11_Packages")
for entry in dir("BPP4D3E_11_Packages"): 
    print(entry)

# remove the # from the line below
#print("BPP4D3E_11_Packages.SayHello("Josh")")

# the from import statement is used to get only the needed resources which saves space and uses less memory
#remove the # from below
#from BPP4D3E_11_Packages import SayHello
#dir(BPP4D3E_11_Packages)
#dir(SayHello)
#SayHello("Angie")
#del BPP4D3E_11_Packages
#dir(BPP4D3E_11_Packages)
#import BPP4D3E_11_Packages as BPP
#dir(BPP)