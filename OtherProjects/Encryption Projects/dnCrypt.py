import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit
from cryptography.fernet import Fernet

class EncryptionApp(QWidget):
    def __init__(self):
        super().__init__()

        
        self.key = Fernet.generate_key()
        self.fernet = Fernet(self.key)

       
        self.title_label = QLabel("Encryption App")
        self.encrypt_label = QLabel("Enter message to encrypt:")
        self.encrypt_input = QLineEdit()
        self.encrypt_button = QPushButton("Encrypt")
        self.decrypt_label = QLabel("Enter message to decrypt:")
        self.decrypt_input = QLineEdit()
        self.key_label = QLabel("Encryption key:")
        self.key_output = QTextEdit()
        self.decrypt_button = QPushButton("Decrypt")

        
        self.encrypt_button.clicked.connect(self.encrypt_message)
        self.decrypt_button.clicked.connect(self.decrypt_message)

        
        vbox = QVBoxLayout()
        vbox.addWidget(self.title_label)

        hbox_encrypt = QHBoxLayout()
        hbox_encrypt.addWidget(self.encrypt_label)
        hbox_encrypt.addWidget(self.encrypt_input)
        hbox_encrypt.addWidget(self.encrypt_button)
        vbox.addLayout(hbox_encrypt)

        hbox_decrypt = QHBoxLayout()
        hbox_decrypt.addWidget(self.decrypt_label)
        hbox_decrypt.addWidget(self.decrypt_input)
        vbox.addLayout(hbox_decrypt)

        vbox.addWidget(self.key_label)
        vbox.addWidget(self.key_output)

        vbox.addWidget(self.decrypt_button)

        self.setLayout(vbox)

    def encrypt_message(self):
        message = self.encrypt_input.text().encode()
        encrypted_message = self.fernet.encrypt(message)
        self.key_output.setText(str(self.key))

    def decrypt_message(self):
        key = self.key_output.toPlainText().encode()
        message = self.decrypt_input.text().encode()
        fernet = Fernet(key)
        decrypted_message = fernet.decrypt(message)
        self.decrypt_input.setText(decrypted_message.decode())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EncryptionApp()
    window.show()
    sys.exit(app.exec_())
