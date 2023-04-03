from colorama import *
from colorama import init
import os
import pyfiglet as pf

# This is a config file for the colours. You can add your functions here or do it on the main program if you wish.

# TOOLKIT COLOURS

def Menu():
    print (Fore.YELLOW + "[ MAIN MENU ]".center(80, "—"))

def Banner():
    banner = pf.figlet_format("Python Security Toolkit", font = "larry3d", justify="center")
    print (Fore.WHITE + Style.BRIGHT + banner)

def Copyright():
    print (Fore.YELLOW + Style.BRIGHT + "Version V0.1\t\tProof of Concept\tCreative Commons Zero License".center(80))
    print(Style.RESET_ALL)

def Network():
    print (Fore.GREEN + "\nNETWORK\n")
    print ("1. Network Scanner")
    print ("2. Port Scanner")
    print(Style.RESET_ALL)

def Webapp():
    print (Fore.BLUE + "\nWEB APPLICATION\n")
    print ("3. Domain Enumerator")
    print ("4. Subdomain Enumerator")
    print(Style.RESET_ALL)

def Brute():
    print (Fore.CYAN + "\nBRUTE FORCE\n")
    print ("5. Hash Cracker")
    print(Style.RESET_ALL)

def Settings():
    print (Fore.YELLOW + "\nSETTINGS\n")
    print ("99. Configure Colours")
    print (Fore.RED + "0. Exit")
    print(Style.RESET_ALL)

def Seperator():
    print ("")
    print (Fore.MAGENTA + "".center(80, "-"))
    print(Style.RESET_ALL)

# NETWORK COLOURS - GREEN
def NetScanBanner():
    os.system('cls||clear')
    print (Fore.GREEN + "[ Network Scanner ]".center(80, "—"))
    print(Style.RESET_ALL)

def PortScanBanner():
    os.system('cls||clear')
    print (Fore.GREEN + "[ Port Scanner ]".center(80, "—"))
    print(Style.RESET_ALL)

# WEB COLOURS - BLUE
def SubBanner():
    os.system('cls||clear')
    print (Fore.BLUE + "[ Subdomain Enumerator ]".center(80, "—"))
    print(Style.RESET_ALL)

def DirBanner():
    os.system('cls||clear')
    print (Fore.BLUE + "[ Directory Enumerator ]".center(80, "—"))
    print(Style.RESET_ALL)

# BRUTE COLOURS - CYAN
def HashCrackBanner():
    os.system('cls||clear')
    print (Fore.CYAN + "[ Hash Cracker ]".center(80, "—"))
    print(Style.RESET_ALL)

# Success - GREEN
def Success():
    Fore.GREEN + "[+] "

# Fail - RED
def Fail():
    Fore.RED + "[-] "

# Info - BLUE
def Info():
    Fore.BLUE + "[i] "

# Alert - YELLOW
def Alert():
    Style.BRIGHT + Fore.YELLOW + "[!] "

