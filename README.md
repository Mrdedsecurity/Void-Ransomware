     /$$    /$$          /$$       /$$       /$$$$$$$                                                                                                   
    | $$   | $$         |__/      | $$      | $$__  $$                                                                                                  
    | $$   | $$ /$$$$$$  /$$  /$$$$$$$      | $$  \ $$  /$$$$$$  /$$$$$$$   /$$$$$$$  /$$$$$$  /$$$$$$/$$$$  /$$  /$$  /$$  /$$$$$$   /$$$$$$   /$$$$$$ 
    |  $$ / $$//$$__  $$| $$ /$$__  $$      | $$$$$$$/ |____  $$| $$__  $$ /$$_____/ /$$__  $$| $$_  $$_  $$| $$ | $$ | $$ |____  $$ /$$__  $$ /$$__  $$
     \  $$ $$/| $$  \ $$| $$| $$  | $$      | $$__  $$  /$$$$$$$| $$  \ $$|  $$$$$$ | $$  \ $$| $$ \ $$ \ $$| $$ | $$ | $$  /$$$$$$$| $$  \__/| $$$$$$$$
      \  $$$/ | $$  | $$| $$| $$  | $$      | $$  \ $$ /$$__  $$| $$  | $$ \____  $$| $$  | $$| $$ | $$ | $$| $$ | $$ | $$ /$$__  $$| $$      | $$_____/
       \  $/  |  $$$$$$/| $$|  $$$$$$$      | $$  | $$|  $$$$$$$| $$  | $$ /$$$$$$$/|  $$$$$$/| $$ | $$ | $$|  $$$$$/$$$$/|  $$$$$$$| $$      |  $$$$$$$
        \_/    \______/ |__/ \_______/      |__/  |__/ \_______/|__/  |__/|_______/  \______/ |__/ |__/ |__/ \_____/\___/  \_______/|__/       \_______/
                                                                                                                                                       
Description:

This repository contains a simulated basic ransomware script for educational purposes only. The script is designed to demonstrate the potential risks associated with cybersecurity threats, such as ransomware attacks. It should not be used for any malicious intent, and its usage is strictly limited to educational and awareness purposes.

The ransomware is designed to be deployed in VM environment with attacker and victim systems within the same network. Both systems will need to be configured to use SSH. Additionally, the repository also contains a "victimfolder" which can be used for demo purposes.

・┈┈・┈┈・┈┈・・┈┈・┈┈・┈┈・・┈┈・┈┈・┈┈・・┈┈・┈┈・┈┈・・┈┈・┈┈・


Features:

* Encryption of files using the Fernet symmetric key encryption algorithm.
* Key generation and storage for demonstration purposes.
* Encrypt folder which the ransomware is contained within.
* Work with multiple file types.
* Decryption script available with secret password being "dedopswashere"
* Exfiltration of victim data and encryption key via SSH (SCP), sent to a "Command and Control (C2)".
* Starts to delete encrypted victim data within 2 minutes, then destroys a file every minute.
* Once executed, opens a Youtube video and gif on separate browser sessions.  


・┈┈・┈┈・┈┈・・┈┈・┈┈・┈┈・・┈┈・┈┈・┈┈・・┈┈・┈┈・┈┈・・┈┈・┈┈・


Instructions:

Clone Repository:
*      git clone https://github.com/Mrdedsecurity/Void-Ransomware

Navigate to the project:
*      cd Void-Ransomware

Navigate to the victim folder demo:
*      cd victimfolder

Run Ransomware Script:
*      python3 voidransom.py

Decrypt Files
*      python3 voiddecrypt.py

Secret Phase
*      dedopswashere



・┈┈・┈┈・┈┈・・┈┈・┈┈・┈┈・・┈┈・┈┈・┈┈・・┈┈・┈┈・┈┈・・┈┈・┈┈・┈┈・

Disclaimer:

This script is intended solely for educational use and ethical hacking practice. I do not endorse or encourage any form of illegal or harmful activity. Any misuse of this script for malicious purposes is strongly condemned. Always respect privacy and adhere to legal and ethical standards.
