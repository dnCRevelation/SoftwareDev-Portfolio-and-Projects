# Function that returns a value
def count_a(word):
    total_a = 0
    for letter in word:
        if letter == "a":
            total_a = count_a + 1
        return total_a

username = input("Enter your name: ")
total_as_in_name = count_a(username)
print("There are " +str(total_as_in_name), " A's in your name")
####################################################################################################
# Adding to a list
mylist = [1,2,3,4]
mylist.append(5)
print(mylist)
#################################################################################################
# Break Loops
sensors = [1,2,3,4,5]
total = 0

for sensor in sensors:
    if sensor < 0:
        break # <------ stops all instances once the value of sensor goes below zero
    total = total + sensor
print ("Total is: " +str(total))
##################################################################################################
# Continue Loops
for sensor in sensors:
    if sensor < 0:
        continue # <------ Makes an exception and ignores the "If" statement and continues the instance
    total = total + sensor
print ("Total is: " +str(total))
#################################################################################################
# While / Nested Loops

"""While Loop"""
answer = input("Shall we keep going? (y/n)")
while answer == "y":
    answer = input("Should we seriously keep going? (y/n)")

"""Nested Loop"""
answer = input("Launch another rocket?(y/n)")
while answer == "y":
    for count in range(10, 0, -1):
        print(count)
    print("LIFT OFF!!!")
################################################################################################
# Input From File / Output to File

"""Input"""
file = open("C:\desktop\list.txt")
file.read() # Reads all data in file
file.readline() # Reads line by line from file
file.close # Closes file

"""Output"""
file = open("C:\desktop\list.txt", "a") #<---- Apphends file data for writing info
file.write("Whatever you want to add into the file data") #<----- Writes data to file
file.close
#################################################################################################
# If, Else, Elif Statements (Branching)

"""If Statement"""
temp = 75
if temp < 75:
    print("Nice and cold in here")

"""Else Statement"""
age = 15
if age > 17:
    print("you can vote")
else:
    print("You can't vote")

"""Elif Statement"""
quiz_score = 9 
if quiz_score > 8:
    print("You are a quiz champion!!!")
elif quiz_score > 5:
    print("you could do better")
else:
    print("Your test-taking skills suck dick bro, are you dumb?!?!?!")
###################################################################################################
# Libraries

"""Import"""                                         # Imports a library and its modules for use in a program, to use a function from the library, type in the name of the module followed by a period to access its avaliable functions. Ex: "time._____"
import time
offset = time.timezone
print("your offset is", offset)

"""From Import"""
from random import randint                           # If a program only needs one or two functions from the library, it is considered more streamlined to use this method rather than imort the whole module
dice_roll = randint(1,6)
print("you threw a ", dice_roll)

"""From Import As"""
from webbrowser import open as show_me               # From a module of an imported library, this allows programmers to refer to the function needed by a custom name so that duplicates in code dont cause errors
url = input("Enter a URL: ")
show_me(url)
###################################################################################################
# Splitting Lists / Using the len() Function

"""Splitting Lists"""
# When splitting a list you need to provide two arguement. Remember that indexes always start from 0 in python.
# For example:  "players[1:3]" would take players from index 1 up to index 2
# Here is a visualization for better understanding: "players[Starting Index : The Index You Want To Stop At]"
players = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
team1 = players[:len(players)//2]
# This example of splitting lists defines "team1" as players, "[1,2,3,4,5,6,7,8,9,10]", takes the number of players and uses the amount of people in the team, ":len(players)" = 10 and splits it into team 1 by taking the amount of players(10) and dividing them in half "[0:len(players)//2]" and defines half of the team as team 1

"""Len() Function"""
len("hello") # is == to 5 since len() counts the number of items in a list, string, or defined object with integers or string text
########################################################################################################
# Python Tuples and Comma Separated Value(.CSV) Files

"""Tuples"""
# Python Tuples are values that cannot be changed proactively through the code if they are already implemented
# Tuple Ex:
numbers = (1,2,3,4,5)
print(numbers[3]) # Prints the number from the tuple in index position 3 which is the number 4
# If you try to alter this, it wont work unless you physically alter the tuple itself
# Ex:
numbers[0] = 4
# === typeerror: 'tuple' object does not support item assignment

""" .CSV files """
#These are lists used to represent data that can be used in project planning and other tasks, that a python program grabs information from to use in creations
import csv

#First column represents task number
1,
#Second column represents the title
1,Design game functionality
#Third column gives the number of days the task is expected to take
1,Design game functionality,2, #The values in each column are separated by commas
#The fourth column gives the prerequisites of the task that have to be done before completing this task
1,Design game functionality,2,2 3

#########################################################################################################
# Strings, Integers, Floats

"""Integer"""
int("5") # Converts string("5") to integer(5)

"""String"""
str(5) # Converts integer(5) to string("5")

"""Float"""
float(5) # Converts integer(5) to float(5.0)
float("5") # Converts string("5") to float(5.0)
###########################################################################################################
# Python Sets

"""Sets"""
# Defining a set:
>>> numbers = {1,2,3} # Just like dictionaries, python sets are written inside curly brackets
# Python sets are similar to a dictionary, a set can be assigned to a variable in many different ways

# Adding numbers to a set: 
>>> numbers.add(4) # Adds the number 4 to the set
>>> numbers
{1,2,3,4} # Output
>>> numbers.add(3)
>>> numbers # The number 3 is already in the set so the value inside it does not change

# Removing values from a set
>>> numbers.remove(3)
>>> numbers
{1,2,4} # Output
############################################################################################################
# Prerequisites as Sets of Numbers

"""Turning Prerequisite Values into Sets of Numbers"""

# To read the prerequisites as a collection of task numbers, first split the string into individual values using python's built-in "split" method. 
# Next, use the int() and map() functions, as shown here, to turn the string of values into a set.
>>> value = "2 3"
>>> value.split()
['2', '3']  # Output
# map() calls the int() function on every string in the list
>>> set(map(int, value.split())) # int() converts a string value into an integer
{2, 3} # Output
# Converts values returned by map() into a (set) data structure
##############################################################################################################
# Returning Sub-Indexes

"""Sub-Index Outputs"""
>>> tasks[3]
# ^ will output the tuple on index 3 = ('Break functionality into steps', 2.0, {1})
                                # Sub-Index:      [0]^                     ^[1]  ^[2]
>>> tasks[3][1]
2.0 # Outputs the value at index [3] and sub-index[1] = "2.0"
##############################################################################################################
# Using Named Tuples

"""Named Tuples"""

from collections import namedtuple
Task = namedtuple("Task", ["title", "duration", "prerequisites"]) # Using named tuples allows you to find and call the tuples(sub-indexes) by name. 
# So instead of using tasks[3][1] as we did before, now all you have to type is tasks[3].duration to get the same result!
>>> tasks[3].duration
2.0       # The Output is the same as if you typed tasks[3][1]! 
################################################################################################################
# The .issubset Method

""".issubset Method"""
# The issubset method checks whether one set is contained within another set, meaning it checks if a set has another set within it or if it is empty.
# This means that # 
task.prerequisites.issubset(completed) # will be True for a task with no prerequisites and will begin immediately, even when no tasks have been completed yet
# The
earliest_start_day # is set to 0 before looping over a tasks prerequisites, if there are no prerequisites, then this task will use 0 as its start day.
# Once this task is added to the completed set, it will allow the tasks that depend on it to begin
############################################################################################################### 
# TKINTER GUI

"""Tkinter"""
# Tkinter starts with the root(GUI Window)
# Tkinter has widgets that serve as buttons, lists, and user text boxes
# Tk widgets, are created by calling their tk constructors with the parent widget as their first arguement, followed by a set of keyword arguements specifying different attributes of the widget, such as size and color.
# Tk module's mainloop() function draws the widgets on screen and handles events such as mouse clicks and key presses. This function does not return while the window is open.
# If you want to do anything after the window opens, you will have to define functions that will be called by mainloop() when specific events happen, such as a button being pressed
import tkinter          # e.g. import all modules of tkinter
import tkinter as tk    # e.g. "import tkinter as tk, using only tk functions and libraries for GUI purposes"
from tkinter import *   # e.g. "from tkinter import all"

root = tk.Tk() # Creating the window
