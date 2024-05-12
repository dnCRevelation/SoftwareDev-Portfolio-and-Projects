                       ### Decryption Program 1.0 ###
            ## Written and debugged by John Wilkinson 4-9-22 ##
        # Place your Encrypted code within the "Ciphertext" brackets #
#----------------------------------------------------------------------------#
from cryptography.fernet import Fernet

with open('secret.key', 'rb') as my_private_key:
    key = my_private_key.read()


ciphertext = () 
#            ^^ Here

f = Fernet(key)
cleartext = f.decrypt(ciphertext)
cleartext = cleartext.decode()
print(cleartext)

##### MAKE SURE TO SAVE THIS FILE AFTER INPUT BEFORE YOU RUN THIS PROGRAM!!! #####