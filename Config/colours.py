from colorama import *
from colorama import init

# This is a config file for the colours. You can add your functions here or do it on the main program if you wish.

def Menu():
    print (Fore.YELLOW + "MAIN MENU".center(80, "—"))

def Network():
    print (Fore.GREEN + "\nNETWORK\n")
    print ("1. Network Scanner")
    print ("2. Port Scanner")

def Webapp():
    print (Fore.BLUE + "\nWEB APPLICATION\n")
    print ("3. Domain Enumerator")
    print ("4. Subdomain Enumerator")

def Brute():
    print (Fore.CYAN + "\nBRUTE FORCE\n")
    print ("5. Hash Cracker")

def Exit():
    print (Fore.RED + "\n0. Exit")

def Seperator():
    print ("")
    print (Fore.MAGENTA + "".center(80, "-"))

