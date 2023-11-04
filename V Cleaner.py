from tkinter import messagebox
from bs4 import BeautifulSoup
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from smtplib import SMTPException
from cryptography.fernet import Fernet

import pyttsx3
import ctypes
import hashlib
import subprocess
import os
import time
import textwrap
import requests
import webbrowser
import wget
import shutil
import imaplib
import smtplib


logo = """
██╗   ██╗     ██████╗██╗     ███████╗ █████╗ ███╗   ██╗███████╗██████╗ 
██║   ██║    ██╔════╝██║     ██╔════╝██╔══██╗████╗  ██║██╔════╝██╔══██╗
██║   ██║    ██║     ██║     █████╗  ███████║██╔██╗ ██║█████╗  ██████╔╝
╚██╗ ██╔╝    ██║     ██║     ██╔══╝  ██╔══██║██║╚██╗██║██╔══╝  ██╔══██╗
 ╚████╔╝     ╚██████╗███████╗███████╗██║  ██║██║ ╚████║███████╗██║  ██║
  ╚═══╝       ╚═════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝\n"""

menu = """
FIREWALL: Enable firewall.
UPDATE: Check for and install available updates.

INFO-IP: Obtain information about an IP address.
INFO-PORT: Obtain information about a port.
INFO-PROCESS: Obtain information about a process.
INFO-DLL: Obtain information about a DLL.

PROCESS: Display processes running on the system.

RESTORE: Create a restore point.
RESET: Perform a system reset.

ENCRYPT: Encrypt a drive, directory or single file.
DECRYPT: Decrypt a drive, directory or a single file.

TEMP: Delete temporary files.

E-MAIL: Delete all emails, listed in the spam category of Gmail.

ASSISTANCE: Request email support regarding the use and operation of V Cleaner.

UPDATE: Allow your email address to be registered, in order to get any updates to V Cleaner.

------------------ANTIVIRUS------------------

AVAST: Perform an antivirus scan with Avast.
"""

ctypes.windll.kernel32.SetConsoleTitleW("V Cleaner")

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

if not ctypes.windll.shell32.IsUserAnAdmin():

    engine.say("In order to use V Cleaner optimally, please run it from the command prompt in administrator mode.")
    engine.runAndWait()

    messagebox.showwarning(title=" V Cleaner :", message="In order to use V Cleaner optimally, please run it from the command prompt in administrator mode !")

    engine.say("Do you need a tutorial on how to run V Cleaner via command prompt in administrator mode ?")
    engine.runAndWait()

    tutorial = input("Do you need a tutorial on how to run V Cleaner via command prompt in administrator mode ? : ")

    os.system("cls")

    if tutorial.lower() in ["y", "yes"]:

        webbrowser.open("https://imgur.com/a/Cno2672")
        time.sleep(3)

        quit()

    elif tutorial.lower() in ["n", "no"]:

        quit()

elif ctypes.windll.shell32.IsUserAnAdmin():

    os.system("cls")

    engine.say("V Cleaner does not save any input data. Except for your email address, if you wish to receive updates by email.")
    engine.runAndWait()

    messagebox.showwarning(title="V Cleaner :", message="V Cleaner does not save any input data !\n\nExcept for your email address, if you wish to receive updates by email.")

    engine.say("In order for V Cleaner to become known to the public, please share it with your loved ones if necessary !")
    engine.runAndWait()

    messagebox.showinfo(title="V Cleaner :", message="In order for V Cleaner to become known to the public, please share it with your loved ones if necessary.\n\nTHANK YOU !")

def select_option():

    menu_options = {

    "FIREWALL": firewall,
    "UPDATE": update,
    "INFO-IP": info_ip,
    "INFO-PORT": info_port,
    "INFO-PROCESS": info_process,
    "INFO-DLL": info_dll, 
    "PROCESS": process,
    "E-MAIL": email_spam, 
    "RESTORE": restore,
    "RESET": reset,
    "ENCRYPT": encrypt,
    "DECRYPT": decrypt,
    "TEMP": temp,
    "ASSISTANCE": assistance, 
    "UPDATE": update,
    "AVAST": avast,

    }

    while True:

        try:

            console_cleaning()

            print(logo)
            print(menu.strip() + "\n")

            engine.say("Please select an option to execute the desired action.")
            engine.runAndWait()

            option = input("Please select an option to execute the desired action : ")

            console_cleaning()

            if option in menu_options:
                
                menu_options[option]()

            elif not option in menu_options:

                engine.say("Please choose only one option from the program !")
                engine.runAndWait()

                messagebox.showwarning(title="V Cleaner :", message="Please choose only one option from the program !")

        except KeyboardInterrupt:

            console_cleaning()

            engine.say("Are you sure you want to quit V Cleaner ?")
            engine.runAndWait() 

            confirmation = input("Are you sure you want to quit V Cleaner ? : ")

            console_cleaning()

            if confirmation.lower() in ["y", "yes"]:

                quit()

            elif confirmation.lower() in ["n", "no"]:

                select_option()

def firewall():

    enable_firewall = subprocess.run(["netsh", "advfirewall", "set", "allprofiles", "state", "on"])

    console_cleaning()

    try:

        if enable_firewall.returncode == 0:

            engine.say("The firewall has just been activated !")
            engine.runAndWait()

            messagebox.showinfo(title="V Cleaner :", message="The firewall has just been activated !")

        elif enable_firewall.returncode == 1:

            engine.say("Firewall activation could not be completed !")
            engine.runAndWait()

            messagebox.showwarning(title="V Cleaner :", message="Firewall activation could not be completed !")

    except Exception as e:

        engine.say("An error has occurred !")
        engine.runAndWait()

        messagebox.showwarning(title="V Cleaner :", message=f"An error has occurred ! {e}")

def update():

    engine.say("This operation may take several minutes, do you want to continue ?")
    engine.runAndWait()

    messagebox.showwarning(title="V Cleaner :", message="This operation may take several minutes, do you want to continue ?")

    engine.say("The search for available updates is in progress.")
    engine.runAndWait()

    install_updates = subprocess.run(["powershell", "Get-WindowsUpdate", "-AcceptAll", "-Install", "-Verbose"])

    if install_updates.returncode == 0:

        engine.say("All available updates have been installed successfully !")
        engine.runAndWait()

        messagebox.showinfo(title="V Cleaner :", message="All available updates have been installed successfully !")

    elif install_updates.returncode == 1:

        engine.say("Installation of updates could not be completed !")
        engine.runAndWait()

        messagebox.showwarning(title="V Cleaner :", message="Installation of updates could not be completed !")

def info_ip():

    engine.say("What is the IP address ?")
    engine.runAndWait()
    
    ip_address = input("What is the IP address ? : ")

    console_cleaning()

    url = "https://fr.infobyip.com/ip-" + ip_address + ".html"
    webbrowser.open(url)
    
    os.system("pause > nul")
    
    console_cleaning()

def info_port():

    engine.say("What is the port ?")
    engine.runAndWait()

    while True:

        port_number = input("What is the port ? : ")

        console_cleaning()

        if port_number.isdigit() and int(port_number) in range(65536):

            url = "https://www.speedguide.net/port.php?port=" + port_number
            webbrowser.open(url)

            break

        elif not port_number.isdigit():

            engine.say("Please transmit a valid port, all alphanumeric characters cannot be transmitted !")
            engine.runAndWait()

            messagebox.showwarning(title="V Cleaner :", message="Please transmit a valid port, all alphanumeric characters cannot be transmitted !")
        
        elif not int(port_number) in range(65536):

            engine.say("Please transmit port within 65535.")
            engine.runAndWait()

            messagebox.showwarning(title="V Cleaner :", message="Please transmit port within 65535.")

def info_process():

    engine.say("What is the name of the process ?")
    engine.runAndWait()

    while True:

        process_name = input("What is the name of the process ? : ")

        console_cleaning()

        if process_name.endswith(".exe"):

            url = "https://www.file.net/process/" + process_name + ".html"
            response = requests.get(url)

            soup = BeautifulSoup(response.text, "html.parser")

            span = soup.find("span", itemprop="description")
            process = span.get_text()

            print(textwrap.dedent(process))

            os.system("pause > nul")
            
            console_cleaning()

            break

        elif not process_name.endswith(".exe"):

            engine.say("Please transmit only the process name with its extension !")
            engine.runAndWait()

            messagebox.showwarning(title="V Cleaner :", message="Please transmit only the process name with its extension !")

def info_dll():

    engine.say("What is the name of the DLL ?")
    engine.runAndWait()

    while True:

        dll_name = input("What is the name of the DLL ? : ")

        console_cleaning()

        if dll_name.endswith(".dll"):

            url = "https://www.file.net/process/" + dll_name + ".html"
            response = requests.get(url)

            soup = BeautifulSoup(response.text, "html.parser")

            div = soup.find("div", itemprop="description")
            dll = div.get_text()

            print(textwrap.dedent(dll))

            os.system("pause > nul")
            
            console_cleaning()

            break

        elif not dll_name.endswith(".dll"):

            engine.say("Please only transmit the DLL name with its extension !")
            engine.runAndWait()

            messagebox.showwarning(title="V Cleaner :", message="Please transmit only the DLL name with its extension !")

def process(): 

    engine.say("Please wait, the display of processes running on the system is in progress.")
    engine.runAndWait()

    time.sleep(5)

    subprocess.run("tasklist /m")
    os.system("pause > nul")

    console_cleaning()

def restore():
    
    engine.say("Are you sure you want to perform a system restore ?")
    engine.runAndWait()

    confirmation = input("Are you sure you want to perform a system restore ? : ")
    
    console_cleaning()

    if confirmation in ["y", "yes"]:

        try:

            subprocess.run(["powershell", "-Command", "Checkpoint-Computer -Description 'RESTORE' -RestorePointType 'MODIFY_SETTINGS'"], check=True)

            engine.say("The restore point has been created successfully !")
            engine.runAndWait()

            messagebox.showinfo(title="V Cleaner", message="The restore point has been created successfully !")
    
        except subprocess.CalledProcessError:

            engine.say("The restore point could not be created !")
            engine.runAndWait()
                
            messagebox.showwarning(title="V Cleaner", message="The restore point could not be created !")

    elif confirmation.lower() in ["n", "no"]:

        pass      

def reset():

    engine.say("Are you sure you want to reset your system ?")
    engine.runAndWait()

    confirmation = input("Are you sure you want to reset your system ? : ")

    console_cleaning()

    if confirmation.lower() in ["y", "yes"]:

        subprocess.run("systemreset")

    elif confirmation.lower() in ["n", "no"]:

        pass

def email_spam():

    try:

        engine.say("What is your e-mail address ?")
        engine.runAndWait()

        email_address = input("What is your e-mail address ? : ")

        console_cleaning()

        engine.say("What is your password ?")
        engine.runAndWait()

        password = input("What is your password ? : ")

        console_cleaning()

        server = imaplib.IMAP4_SSL("imap.gmail.com")
        server.login(email_address, password)

        mailbox = "[Gmail]/Spam"
        server.select(mailbox)

        status, email_ids = server.search(None, "ALL")

        if status == "OK":

            email_id_list = email_ids[0].split()

            if not email_id_list:

                engine.say("You have no spam e-mails !")
                engine.runAndWait()

                messagebox.showinfo(title="V Cleaner :", message="You have no spam e-mails !")

            else:
                    
                for email_id in email_id_list:
                    
                    server.store(email_id, '+FLAGS', '(Deleted)')
                    
                    server.expunge()

                    engine.say("All e-mails in the spam category have been deleted !")
                    engine.runAndWait()

                    messagebox.showinfo(title="V Cleaner :", message="All e-mails in the spam category have been deleted !")

                else:

                    engine.say("An error occurred while searching for e-mails.")
                    engine.runAndWait()

                    messagebox.showwarning(title="V Cleaner :", message="An error occurred while searching for e-mails !")

    except imaplib.IMAP4.error as e:

        engine.say("An error has occurred with the Gmail IMAP server.")
        engine.runAndWait()

        messagebox.showwarning(title="V Cleaner :", message=f"An error has occurred with the Gmail IMAP server ! : {e}")

    except Exception as e:

        engine.say("An error has occurred !")
        engine.runAndWait()

        messagebox.showwarning(title="V Cleaner :", message=f"An error has occurred ! : {e}")

    finally:
            
        server.logout()

key_path = os.path.join(os.path.expanduser("~"), "Desktop", "v-cleaner.vkey")

def create_key():
    
    key = Fernet.generate_key()
    
    with open(key_path, "wb") as key_file:
        
        key_file.write(key)

def get_key():

    with open(key_path, "rb") as key_file:
        
        key = key_file.read()
    
    return Fernet(key)

def encrypt():
    
    create_key()
    
    fernet = get_key()
    
    encrypt_options = """
    DIRECTORY: Encrypt a directory.
    FILE: Encrypt a file."""
    
    print(textwrap.dedent(str(encrypt_options) + "\n").lstrip())

    engine.say("Please choose an option.")
    engine.runAndWait()
    
    encrypt_option = input("Please choose an option : ")

    console_cleaning()
    
    if encrypt_option == "DIRECTORY":

        engine.say("Please transmit the directory path.")
        engine.runAndWait()
        
        directory = input("Please transmit the directory path : ")

        console_cleaning()
        
        for parent_folder, subfolders, files in os.walk(directory):
            
            for file in files:
                
                file_path = os.path.join(parent_folder, file)
                
                with open(file_path, "rb") as original_file:
                    
                    original_content = original_file.read()
                    encrypted_content = fernet.encrypt(original_content)
                
                with open(file_path, "wb") as encrypted_file:
                    
                    encrypted_file.write(encrypted_content)

    elif encrypt_option == "FILE":

        engine.say("Please transmit the file path.")
        engine.runAndWait()
        
        path = input("Please transmit the file path : ")

        console_cleaning()
        
        if os.path.isfile(path):
            
            with open(path, "rb") as original_file:
                
                original_content = original_file.read()
                encrypted_content = fernet.encrypt(original_content)
            
            with open(path, "wb") as encrypted_file:
                
                encrypted_file.write(encrypted_content)

def decrypt():

    fernet = get_key()

    decrypt_options = """
    DIRECTORY: Decrypt a directory.
    FILE: Decrypt a file."""
    
    print(textwrap.dedent(str(decrypt_options) + "\n").lstrip())

    engine.say("Please choose an option.")
    engine.runAndWait()
    
    decrypt_option = input("Please choose an option : ")

    console_cleaning()
    
    if decrypt_option == "DIRECTORY":

        engine.say("Please transmit the directory path.")
        engine.runAndWait()

        directory = input("Please transmit the directory path : ")

        console_cleaning()
        
        for parent_folder, subfolders, files in os.walk(directory):
            
            for file in files:
                
                file_path = os.path.join(parent_folder, file)
                
                with open(file_path, "rb") as encrypted_file:
                    
                    encrypted_content = encrypted_file.read()
                    decrypted_content = fernet.decrypt(encrypted_content)
                
                with open(file_path, "wb") as decrypted_file:
                    
                    decrypted_file.write(decrypted_content)
    
    elif decrypt_option == "FILE":

        engine.say("Please transmit the file path.")
        engine.runAndWait()
        
        path = input("Please transmit the file path : ")

        console_cleaning()
        
        if os.path.isfile(path):
            
            with open(path, "rb") as encrypted_file:
                
                encrypted_content = encrypted_file.read()
                decrypted_content = fernet.decrypt(encrypted_content)
            
            with open(path, "wb") as decrypted_file:
                
                decrypted_file.write(decrypted_content)

def temp():
    
    temp_path = os.environ.get('TEMP')

    if temp_path and os.path.exists(temp_path):
        
        for root, dirs, files in os.walk(temp_path):
            
            for file in files:
                
                file_path = os.path.join(root, file)
                
                try:
                    
                    os.remove(file_path)

                except OSError:

                    pass
                
                except Exception as e:

                    engine.say(f"A file could not be deleted !")
                    engine.runAndWait()
                    
                    messagebox.showwarning(title="V Cleaner :", message=f"A file could not be deleted : {str(e)}")

            for directory in dirs:
                
                dir_path = os.path.join(root, directory)
                
                try:
                    
                    shutil.rmtree(dir_path)

                except OSError:

                    pass
                
                except Exception as e:

                    engine.say(f"A directory could not be deleted !")
                    engine.runAndWait()
                    
                    messagebox.showwarning(title="V Cleaner :", message=f"A directory could not be deleted : {str(e)}")

        engine.say("Files as well as directories have been deleted !")
        engine.runAndWait()

        messagebox.showinfo(title="V Cleaner :", message="Files as well as directories have been deleted !")
    
    else:

        engine.say("The directory containing the temporary files does not exist !")
        engine.runAndWait()

        messagebox.showwarning(title="V Cleaner", message="The directory containing the temporary files does not exist !")

def assistance():

    try:

        while True:

            engine.say("What is your e-mail address ?")
            engine.runAndWait()

            email_address = input("What is your e-mail address ? : ")

            console_cleaning()

            engine.say("What is your password ?")
            engine.runAndWait()

            password = input("What is your password ? : ")

            console_cleaning()

            recipient = "an0n53c@proton.me"

            msg = MIMEMultipart()
            msg['From'] = email_address
            msg['To'] = recipient
            msg['Subject'] = "V Cleaner support request."
            
            message = """\
            Hello,

            I would like to contact you to inform you that, I am having problems with V Cleaner."""

            msg.attach(MIMEText(message, 'plain'))

            smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
            
            smtp_server.ehlo()
            smtp_server.starttls()
            smtp_server.ehlo()

            smtp_server.login(email_address, password)

            smtp_server.sendmail(email_address, recipient, msg.as_string())
            smtp_server.quit()

            engine.say("Your assistance request has been sent, you will shortly receive an e-mail which will help you !")
            engine.runAndWait()

            messagebox.showinfo(title="V Cleaner :", message="Your assistance request has been sent, you will shortly receive an e-mail which will help you !")

            break

    except smtplib.SMTPException as e:

        engine.say("Your support request could not be sent, please check the information you submitted !")
        engine.runAndWait()

        messagebox.showwarning(title="V Cleaner :", message=f"Your support request could not be sent, please check the information you submitted ! : {e}")

def update():

    engine.say("Do you consent to your email address being registered, in order to obtain any updates to V Cleaner ?")
    engine.runAndWait()

    confirmation = input("Do you consent to your email address being registered, in order to obtain any updates to V Cleaner ? : ")

    console_cleaning()

    if confirmation.lower() in ["y", "yes"]:

        try:

            while True:

                engine.say("What is your e-mail address ?")
                engine.runAndWait()

                email_address = input("What is your e-mail address ? : ")

                console_cleaning()

                engine.say("What is your password ?")
                engine.runAndWait()

                password = input("What is your password ? : ")

                console_cleaning()

                recipient = "an0n53c@proton.me"

                msg = MIMEMultipart()
                msg['From'] = email_address
                msg['To'] = recipient
                msg['Subject'] = "Permission to register the e-mail address, in order to obtain any updates to V Cleaner."
                
                message = """\
                Hello, 

                I hereby consent to my email address being registered in order to obtain any updates to V Cleaner."""

                msg.attach(MIMEText(message, 'plain'))

                smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
                
                smtp_server.ehlo()
                smtp_server.starttls()
                smtp_server.ehlo()

                smtp_server.login(email_address, password)

                smtp_server.sendmail(email_address, recipient, msg.as_string())
                smtp_server.quit()

                engine.say("An email has been sent to the creator, confirming your consent to your email address being enregistred in order to obtain any updates to V Cleaner !")
                engine.runAndWait()

                messagebox.showinfo(title="V Cleaner :", message="An email has been sent to the creator, confirming your consent to your email address being enregistred in order to obtain any updates to V Cleaner !")

                break

        except smtplib.SMTPException as e:

            engine.say("Confirmation of your consent to the registration of your email address in order to obtain updates from V Cleaner, could not be sent to the creator !")
            engine.runAndWait()

            messagebox.showwarning(title="V Cleaner :", message=f"Confirmation of your consent to the registration of your email address in order to obtain updates from V Cleaner, could not be sent to the creator ! : {e}")

    elif confirmation.lower() in ["n", "no"]:

        pass

def avast():

    directory = r"C:\Program Files\Avast Software\Avast"

    if os.path.exists(directory):

        pass 

    else: 

        engine.say("You do not have Avast, please install it to perform an analysis.")
        engine.runAndWait()

        messagebox.showwarning(title="V Cleaner :", message="You do not have Avast, please install it to perform an analysis.")

        engine.say("Do you want to install Avast ?")
        engine.runAndWait()

        confirmation = input("Do you want to install Avast ? : ")

        console_cleaning()

        if confirmation.lower() in ["y", "yes"]:

            engine.say("Please wait, Avast is being installed.")
            engine.runAndWait()

            messagebox.showinfo(title="V Cleaner :", message="Please wait, Avast is being installed !")

            url = "https://bits.avcdn.net/productfamily_ANTIVIRUS/insttype_FREE/platform_WIN/installertype_ONLINE/build_RELEASE/cookie_mmm_ava_012_999_a7i_m"
            install = wget.download(url)

            console_cleaning()
            select_option()

        elif confirmation.lower() in ["n", "no"]:

            pass

    avast_options = """
    DRIVE: Perform a virus scan on a drive.
    SYSTEM: Perform an antivirus scan on the system."""

    print(textwrap.dedent(str(avast_options) + "\n").lstrip())

    engine.say("Please choose a scan option.")
    engine.runAndWait()

    avast_option = input("Please choose a scan option : ")

    console_cleaning()

    if avast_option == "DRIVE":

        while True:

            engine.say("What is the drive letter ?")
            engine.runAndWait()

            drive = input("What is the drive letter ? : ")

            console_cleaning()

            if all(letter.isalpha() for letter in drive):

                drive_colon = drive + ":" 
            
                os.chdir(r"C:\Program Files\Avast Software\Avast")
                os.system("start ashCmd.exe " + drive_colon)

                break
            
            else:
                
                engine.say("Please transmit only the letter from the drive to be analyzed.")
                engine.runAndWait()
                
                messagebox.showwarning(title="V Cleaner :", message="Please transmit only the letter from the drive to be analyzed !")
                 
    elif avast_option == "SYSTEM":

        os.chdir(r"C:\Program Files\Avast Software\Avast")
        os.system("start ashCmd.exe C:")

def console_cleaning():

    os.system("cls")

if __name__ == "__main__":
    
    select_option()
