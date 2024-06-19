"""PRINT() FUNCTION"""

# Basic command for printing a string 
print("hello world!")

"""BRANCHING EXPRESSIONS"""

# 1 Branch
if:
# More than 2 Branches
elif:
# 2 Branches
else:
    word 


"""INPUT AND OUTPUT"""

# User input required in form of string # Ex: 
input("")
# Input from file
file = open("/file/location/here.txt")
file.read()
# Output from file
file = open("/file/location/here.txt")
file.write("Write to file here...")


"""BOOLEAN OPERATORS"""

# For this to be True, both expressions must be true
and 
# For this to be True, only one expression must be true 
or
# Putting "not" in front of an expression results in the value False
not 


"""LOGICAL OPERATORS"""

# Greater than >
# Less than <
# Equal value ==
# Not equal value !=
# Counts spaces and letters within string
len()


"""ARITHMETIC OPERATORS"""

# Addition +
# Subtraction -
# Multiplication *
# Division /


"""INTEGERS AND FLOATS"""

Integer = 1
Float = 1.1

"""STRING TYPES"""

String = "Hello"
Combination_String = String + String + String
Casting = ("This is called casting" + str(String) or int(Integer))

"""LOOPS"""

# For loops
for body in range(1,4):
    print(body)

# While loops
answer = input("Keep going? (y/n)")
while answer == "y":
    answer = input("Okay, how about now?(y/n)")

# Nested loops (loop within a loop)
answer = input("Launch another rocket?(y/n)")
while answer == "y":
    for count in range(10,0,-1):
        print(count)
    print("LIFT OFF!")
    answer = input("Launch another?(y/n)")

# Lists of lists 
teams = [["Red", "Adam"], ["Blue", "John"], ["Green", "Sarah"]]
for team in teams: #Selects a team to process
    for name in team: #Prints names in a team one after the other
        print(name)
    print("\n") #Prints an empty line between each team listing

"""ESCAPING LOOPS"""

(break) #abandons the loop completely

(continue) #abandons the current iteration of a loop

"""FUNCTIONS"""

# Creating a function
def greeting():
    print("hello!")

# round() function
pi = 22/7
round(pi, 2) #2 represents the decimal places you want to be rounded to | #Ex: 2 = 3.14 | 1 = 3.1 | 0 = 3

# upper() function
city = "london"
city.upper() #bracket determines which letters will be uppercase

# append() function 
mylist = [1,2,3,4]
mylist.apphend(5) #adds a new number to the end of the list e.g. [1,2,3,4,5]

"""IMPORTING LIBRARIES AND USING MODULES"""
import... #Makes all of the module's code avaliable to the program 
from...import... #If a program only needs to use one or two functions from a module | Ex: "from random import randint"
from...import...as... #Renames a function in the library as something else if its name is too long or too similarly named to other functions written within your code

### Pygame Library ###
## Pygame is very powerful but can be challenging for new programmers, one solution to this is Pygame Zero, which makes pygame functions easier to use ##

