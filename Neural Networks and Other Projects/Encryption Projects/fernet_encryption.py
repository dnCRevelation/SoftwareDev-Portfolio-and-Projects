from cryptography.fernet import Fernet

key = Fernet.generate_key()
with open('secret.key', 'wb') as new_key_file:
    new_key_file.write(key)
    
print(key)

msg = "Meet me at 84.26981 N, 23.21591 W at 0300"
msg = msg.encode() 


f = Fernet(key)
ciphertext = f.encrypt(msg)
print(ciphertext)
