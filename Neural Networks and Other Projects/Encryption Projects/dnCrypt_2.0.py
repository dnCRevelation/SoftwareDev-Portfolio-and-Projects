import tkinter as tk
import socket
import threading
from Crypto.Cipher import AES
import hashlib


class MessageApp:
    def init(self):
        # Create a tkinter GUI window
        self.root = tk.Tk()
        self.root.title("dnCrypt Messaging")
        self.root.geometry("400x200")


    # Create a label and text box for the user to input their message
        self.label = tk.Label(self.root, text="Enter message to send:")
        self.label.pack()
        self.text_box = tk.Entry(self.root, width=40)
        self.text_box.pack()

    # Create a button to send the message
        self.send_button = tk.Button(self.root, text="Send", command=self.send_message)
        self.send_button.pack()

    # Create a label to display received messages
        self.inbox_label = tk.Label(self.root, text="Inbox")
        self.inbox_label.pack()
        self.inbox_listbox = tk.Listbox(self.root, width=40, height=10)
        self.inbox_listbox.pack()

    # Create a label to display sent messages
        self.sent_label = tk.Label(self.root, text="Sent")
        self.sent_label.pack()
        self.sent_listbox = tk.Listbox(self.root, width=40, height=10)
        self.sent_listbox.pack()

    # Create a label to display friends
        self.friends_label = tk.Label(self.root, text="Friends")
        self.friends_label.pack()
        self.friends_listbox = tk.Listbox(self.root, width=40, height=10)
        self.friends_listbox.pack()

    # Create a label to display the user's profile
        self.profile_label = tk.Label(self.root, text="Profile")
        self.profile_label.pack()
        self.profile_entry = tk.Entry(self.root, width=20)
        self.profile_entry.pack()

    # Configure the font and color scheme
        self.root.config(font="Arial 12")
        self.root.config(background="#f0f0f0")
        self.label.config(foreground="#008000")
        self.send_button.config(background="#008000")
        self.inbox_label.config(foreground="#008000")
        self.sent_label.config(foreground="#008000")
        self.friends_label.config(foreground="#008000")
        self.profile_label.config(foreground="#008000")

    # Define the send and receive functions
    def receive_thread(self):
        while True:
            # Wait for an incoming message
            data = self.client_socket.recv(1024).decode()

            if data:
                # Decrypt the message using AES
                key = hashlib.sha256(data.encode()).digest()[:32]
                cipher = AES.new(key, AES.MODE_CBC, iv=b'\0' * 16)
                decrypted_message = cipher.decrypt(bytes.fromhex(data))
                decrypted_message = decrypted_message.decode()

                # Add the decrypted message to the inbox
                self.inbox_listbox.insert(tk.END, decrypted_message)

            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client_socket.connect(("localhost", 12345))

    # Start a thread to receive messages
    receive_thread = threading.Thread(target=receive_thread)
    receive_thread.daemon = True
    receive_thread.start()

def send_message(self):
    # Get the user's input from the text box
    message = self.text_box.get()

    # Generate a random 32-byte key for AES
    key = hashlib.sha256(message.encode()).digest()[:32]

    # Encrypt the message using AES in CBC mode
    cipher = AES.new(key, AES.MODE_CBC, iv=b'\0' * 16)
    encrypted_message = cipher.encrypt(message.encode())
    encrypted_message = encrypted_message.hex()

    # Send the encrypted message to the server
    self.client_socket.send(encrypted_message.encode())

    # Add the sent message to the sent listbox
    self.sent_listbox.insert(tk.END, message)

    # Clear the text box
    self.text_box.delete(0, tk.END)

if __name__ == 'main':
    app = MessageApp()
    app.root.main