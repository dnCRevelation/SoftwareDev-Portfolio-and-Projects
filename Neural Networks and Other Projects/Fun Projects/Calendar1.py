from tkinter import *
import calendar

def showCal():
    gui = Tk()
    gui.config(background='white')
    gui.title("CALENDAR")
    gui.geometry("1024x768")
    year = int(year_field.get())
    gui_content= calendar.calendar(year)
    cal_Year = Label(gui, text = gui_content, font= "Consolas 10 bold")
    cal_Year.grid(row = 5, column = 1, padx = 100)
    gui.mainloop()

if __name__ == '__main__':
    new = Tk()
    new.config(background= 'grey')
    new.title("CALENDAR")
    new.geometry("600x400")
    cal = Label(new, text = "CALENDAR", bg = "dark grey", font = ("times", 28, 'bold'))
    year = Label(new, text = "Enter Your Current Year:", bg = "light green")
    year_field = Entry(new)
    Show = Button(new, text = "Show Me This Bitch", fg = "Black", bg = "Yellow", command = showCal)
    Exit = Button(new, text = "Exit", fg = "Black", bg = "Red", command = exit)
    cal.grid(row = 1, column = 1)
    year.grid(row = 2, column = 1)
    year_field.grid(row = 3, column = 1)
    Show.grid(row = 4, column = 1)
    Exit.grid(row = 6, column = 1)
    new.mainloop()


