#Import Modules
import os
from platform import machine
import tkinter as tk
from tkinter import filedialog, messagebox
import shutil

#Check 32/64 bit OS
if machine() == "AMD64":
    os_type = "AMD64"
else:
    os_type = "x86"

#DXVK libraries version checker
def dxvkVersionCheck():
    content = os.listdir()
    for i in content:
        if i.startswith("dxvk-"):
            version = i
    return version

#Interface
folderDialog = tk.Tk()
folderDialog.withdraw()
folderDialog.attributes('-topmost', True)
file_path = filedialog.askopenfilename(title="Select game to install DXVK...")
file_path = os.path.dirname(file_path)+"//"

#Installer
if os_type=="AMD64":
    source = os.getcwd()+ '\\'+dxvkVersionCheck() +'\\x64\\'
    for file_name in os.listdir(source):
        sourceFolder = source + file_name
        destinationFolder = file_path + file_name
        if os.path.isfile(sourceFolder):
            shutil.copy(sourceFolder, destinationFolder)
    tk.messagebox.showinfo(title="DXVK Installer", message="DXVK "+dxvkVersionCheck()[5:]+" installed sucessfuly!")
else:
    source = os.getcwd()+ '\\'+dxvkVersionCheck() +'\\x32\\'
    for file_name in os.listdir(source):
        sourceFolder = source + file_name
        destinationFolder = file_path + file_name
        if os.path.isfile(sourceFolder):
            shutil.copy(sourceFolder, destinationFolder)
    tk.messagebox.showinfo(title="DXVK Installer", message="DXVK "+dxvkVersionCheck()[5:]+"installed sucessfuly!")