from colorama import *
from colorama import init
import os
import pyfiglet as pf

# This is a config file for the colours. You can add your functions here or do it on the main program if you wish.

# TOOLKIT COLOURS

def Menu():
    print (Fore.YELLOW + "[ MAIN MENU ]".center(80, "—"))

def Banner():
    banner = pf.figlet_format("Python Security Toolkit", font = "larry3d"  )
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

def Exit():
    print (Fore.RED + "\n0. Exit")
    print(Style.RESET_ALL)

def Seperator():
    print ("")
    print (Fore.MAGENTA + "".center(80, "-"))
    print(Style.RESET_ALL)

# NETWORK COLOURS
def NetScanBanner():
    os.sys('cls')
    print (Fore.GREEN + "[ Network Scanner ]".center(80, "—"))

def PortScanBanner():
    os.sys('cls')
    print (Fore.GREEN + "[ Port Scanner ]".center(80, "—"))

# WEB COLOURS

# BRUTE COLOURS

# UTILITY COLOURS
