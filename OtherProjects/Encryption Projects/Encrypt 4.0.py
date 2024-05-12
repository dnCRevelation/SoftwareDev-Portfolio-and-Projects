from cryptography.fernet import Fernet
from tkinter import *

key = Fernet.generate_key()
with open('secret.key', 'wb') as new_key_file:
    new_key_file.write(key)
    
print(key)

gui = Tk()
gui.config(bg= 'White')
gui.geometry("600x500")
gui.title("Encrypt 3.0")


msg = Entry(gui)
msg = msg.encode() 


f = Fernet(key)
ciphertext = f.encrypt(msg)
print(ciphertext)