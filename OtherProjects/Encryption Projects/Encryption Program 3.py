from tkinter import *
from cryptography.fernet import Fernet

key = Fernet.generate_key()
with open('secret.key', 'wb') as new_key_file:
    new_key_file.write(key)


def enClick():
    new = Tk()
    new.config(bg= 'White')
    new.title("Updated Key")
    new.geometry("450x300")
    lbl2 = Label(text= key)
    lbl2.grid(column= 0, row= 0)

    gui = Tk()
    gui.config(background='white')
    gui.title("Encrypt V.1")
    gui.geometry("600x550")
    msg = bytes(Entry(gui))
    lbl = Label(gui, text="This is your Encryption Key: ")
    lbl.grid(column = 0, row = 0)
    guikey = Label(gui, text= key)
    guikey.grid(column = 0, row = 1)
    keybut = Button(gui, text="Click to get a New Encryption Key", command= enClick)
    keybut.grid(column = 0, row = 3)
    enTxt = Label(gui, text = "Enter what you would like to Encrypt below: ")
    enTxt.grid(column = 0, row = 4)
    msg.grid(column = 0, row = 5)
    f = Fernet(key)
    msg = msg.encode()
    ciphertext = f.encrypt(msg)
    enterEn = Button(gui, text = "Encrypt", command= ciphertext ) 
    gui.mainloop()




