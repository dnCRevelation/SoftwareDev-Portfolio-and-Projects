import csv
import tkinter
from collections import namedtuple
from tkinter.filedialog import askopenfilename

Task = namedtuple("Task", ["title", "duration", "prerequisites"])

def read_tasks(filename):
    tasks = {}
    for row in csv.reader(open(filename)): # Maps out which csv belongs where and identifies the index in which it is located to align them into a list 
        number = int(row[0]) # Returns string as integer
        title = row[1]
        duration = float(row[2]) # Returns string as float
        prerequisites = set(map(int, row[3].split()))
        tasks[number] = Task(title, duration, prerequisites) # Aligns the text in a format that lists the number as the identifier and the title, duration, and prerequisites as the information assigned to that task[number]
    return tasks

def order_tasks(tasks):
    incomplete = set(tasks)
    completed = set()
    start_days = {}
    while incomplete:
        for task_number in incomplete:
            task = tasks[task_number]
            if task.prerequisites.issubset(completed):
                earliest_start_day = 0
                for prereq_number in task.prerequisites:
                    prereq_end_day = start_days[prereq_number] + \
                          tasks[prereq_number].duration
                    if prereq_end_day > earliest_start_day:
                        earliest_start_day = prereq_end_day 
                start_days[task_number] = earliest_start_day 
                incomplete.remove(task_number) 
                completed.add(task_number) 
                break                      
    return start_days


"""GUI DESIGN AND WIDGET FUNCTION ELEMENTS"""

"""CANVAS DESIGN"""
# Arguments with default values specify where to draw the elements and how much space they will take on the canvas
def draw_chart(tasks, canvas, row_height=40, title_width=300, \
               line_height=40, day_width=20, bar_height=20, \
                title_indent=20, font_size=-16):
    height = canvas["height"]  ## Defines the height and width of the canvas as local variables
    width = canvas["width"]  ##
    week_width = 5 * day_width                                  
    canvas.create_line(0, row_height, width, line_height, fill="gray")                             ### Draws a horizontal line for the header, one row down and across the entire width of the chart
    for week_number in range(5):      # Loops through the number of weeks from 0-4
        x = title_width + week_number * week_width    ## Sets x to the width of the title plus the week width times the number of the week 
        canvas.create_line(x, 0, x, height, fill="gray")         ## Draws a vertical line at x down the entire height of the chart.
        canvas.create_text(x + week_width / 2, row_height / 2, \
                           text=f"Week {week_number+1}", font=("Helvetica", font_size, "bold")) ### Draws a text string at a point half a week width past x and half a row down.
        start_days = order_tasks(tasks)
        y = row_height
        for task_number in start_days:
            task = tasks[task_number]
            canvas.create_text(title_indent, y + row_height / 2, \
                               text=task.title, anchor=tkinter.W, \
                                font=("Helvetica", font_size))
            bar_x = title_width + start_days[task_number] \
            * day_width
            bar_y = y + (row_height - bar_height) / 2
            bar_width = task.duration * day_width
            canvas.create_rectangle(bar_x, bar_y, bar_x + \
                                    bar_width, bar_y + \
                                        bar_height, fill="red")
            y += row_height


"""WIDGET FUNCTIONAL AND UTILITARIAN OPERATIONS"""
def open_project():                                       # In initialdir="." , the "." is special directory name for the "current" directory
    filename = askopenfilename(title="Open Project", initialdir=".", \
                               filetypes=[("CSV Document", "*.csv")])   # Calls the function to open a file dialog for choosing a CSV file, specifies the dialog title and the acceptable file format. 
    tasks = read_tasks(filename) # Reads the tasks from the .csv file returned by the dialog
    draw_chart(tasks, canvas) # Draws a chart of the tasks in the canvas widget





### GUI ###
root = tkinter.Tk()
root.title("Project Planner")
open_button = tkinter.Button(root, text="Open Project...", \
                             command=open_project)
open_button.pack(side="top")
canvas = tkinter.Canvas(root, width=800, height=400, bg="white")
canvas.pack(side="bottom")
tkinter.mainloop()             
