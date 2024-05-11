"""
Python - Cryptography

Import 'Fernet' from the 'Cryptography' module.

Define a function called 'encrdecr', which takes 3 parameters, as follows:
-The first parameter is 'keyval', which is used to encrypt and decrypt data.
-The second parameter is 'textencr', which contains the text to be encrypted.
-The third paramater is 'textdecr', which contains the byte-code to be decrypted.

The function defintion code stub is given in the editor.
Write code based on the following conditions:
-Declare an empty main list.
-Encrypt the text in 'textencr' and append it to the list.
-Decrypt the byte-code in 'textdecr' and append it to the list.
-Return the list.

Input Sample: 



"""

from cryptography.fernet import Fernet


def encrdecr(keyval, textencr, textdecr):
    mainlist = []
    key = keyval
    f = Fernet(key)

    encrypted_text = f.encrypt(textencr)
    mainlist.append(encrypted_text)

    decrypted_text = f.decrypt(textdecr)
    mainlist.append(decrypted_text.decode())

    return mainlist
