### Decryption Program 1.0 ###

## Written and debugged by John Wilkinson 4-9-22 ##

from cryptography.fernet import Fernet

with open('secret.key', 'rb') as my_private_key:
    key = my_private_key.read()

### Place your Encrypted code within the "Ciphertext" brackets ###
ciphertext = (b'gAAAAABiUa11wdafCcgY9KjyftGx0KuZ0LS_UUFZp0OCmA562RcIX1VRMrti2FsgMZTDn6w6rktxVMBiYuNg06h798Nbhqfbso6DBVrxGNAeJmA1gpsTOQ4_muUyP58Rl5Lr5Kg5VeGk')

f = Fernet(key)
cleartext = f.decrypt(ciphertext)
cleartext = cleartext.decode()
print(cleartext)