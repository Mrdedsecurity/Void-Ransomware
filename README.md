   ![Void](https://github.com/Mrdedsecurity/Void-Ransomware/blob/main/image/void.jpg)
    
    
    ___    __     ______________   ________                                                                    
    __ |  / /________(_)_____  /   ___  __ \_____ ___________________________ ______      _______ ____________ 
    __ | / /_  __ \_  /_  __  /    __  /_/ /  __ `/_  __ \_  ___/  __ \_  __ `__ \_ | /| / /  __ `/_  ___/  _ \
    __ |/ / / /_/ /  / / /_/ /     _  _, _// /_/ /_  / / /(__  )/ /_/ /  / / / / /_ |/ |/ // /_/ /_  /   /  __/
    _____/  \____//_/  \__,_/      /_/ |_| \__,_/ /_/ /_//____/ \____//_/ /_/ /_/____/|__/ \__,_/ /_/    \___/ 
                                                                                                                                                                                                                          
                                                                                                                     
Description:

This repository contains a simulated basic ransomware script for educational purposes only. The script is designed to demonstrate the potential risks associated with cybersecurity threats, such as ransomware attacks. It should not be used for any malicious intent, and its usage is strictly limited to educational and awareness purposes.

The ransomware is designed to be deployed in VM environment with attacker and victim systems within the same network. Both systems will need to be configured to use SSH. Additionally, the repository also contains a "victimfolder" which can be used for demo purposes. All testing for the ransomware has been performed with Kali Linux and Ubuntu.

The goal of the project was a fun hobby for me, it isn't designed for in the wild attacks, as it would be very easy to detect in real-world attacks.

・┈┈・┈┈・┈┈・・┈┈・┈┈・┈┈・・┈┈・┈┈・┈┈・・┈┈・┈┈・┈┈・・┈┈・┈┈・

Requriements:

* Python 3
* SSH

・┈┈・┈┈・┈┈・・┈┈・┈┈・┈┈・・┈┈・┈┈・┈┈・・┈┈・┈┈・┈┈・・┈┈・┈┈・

Features:

* Encryption of files using the Fernet symmetric key encryption algorithm.
* Key generation and storage for demonstration purposes.
* Encrypts the folder in which the ransomware is contained.
* Work with multiple file types.
* Decryption script available with the secret password being "dedopswashere"
* Exfiltration of victim data and encryption key via SSH (SCP), sent to a "Command and Control (C2)".
* Starts to delete encrypted victim data within 2 minutes, then destroys a file every minute.
* Once executed, opens a YouTube video and GIF on separate browser sessions.  


・┈┈・┈┈・┈┈・・┈┈・┈┈・┈┈・・┈┈・┈┈・┈┈・・┈┈・┈┈・┈┈・・┈┈・┈┈・
  ![Void](https://github.com/Mrdedsecurity/Void-Ransomware/blob/main/image/server.jpg)
・┈┈・┈┈・┈┈・・┈┈・┈┈・┈┈・・┈┈・┈┈・┈┈・・┈┈・┈┈・┈┈・・┈┈・┈┈・

Instructions:

Clone Repository:
*      git clone https://github.com/Mrdedsecurity/Void-Ransomware

Navigate to the project:
*      cd Void-Ransomware

Data exfilatration configuration:
*     configure script's SSH connection 

Navigate to a victim folder:
*      cd victimfolder (if encrypting demo files)

Run Ransomware Script:
*      python3 voidransom.py

Decrypt Files:
*      python3 voiddecrypt.py

Secret Phase:
*      dedopswashere



・┈┈・┈┈・┈┈・・┈┈・┈┈・┈┈・・┈┈・┈┈・┈┈・・┈┈・┈┈・┈┈・・┈┈・┈┈・┈┈・

Disclaimer:

This script is intended solely for educational use. I do not endorse or encourage any form of illegal or harmful activity. Any misuse of this script for malicious purposes is strongly condemned. Always respect privacy and adhere to legal and ethical standards.
