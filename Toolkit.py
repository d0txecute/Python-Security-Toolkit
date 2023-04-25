#!/usr/bin/python3 
import os
from config.colours import *
from time import sleep

# Update on start up
print ("Updating Repo")
os.system ("git pull")
sleep(1)
# Clear Screen (Windows/*NIX)
os.system ('cls||clear')


# Start Up Banner
Banner()
Copyright()

sleep(1)

os.system ('cls||clear')

# Print Menu
Menu()

## Networks ## 
Network()
Seperator()

## Web Applications ##
Webapp()
Seperator()

## Brute Force ##
Brute()
Seperator()

## Utility ##
Settings()

try:

    selection = input("\nSelect a Program Number: ")
    print("")
    match selection:
    
     # Networks
        case "1":
            from networks import netscan

        case "2":
            from networks import portscan

        # Web Application
        case "3":
            from webapp import directory_enum

        case "4":
            from webapp import subdomain_enum

        # Brute Force
        case "5":
            from bruteforce import hashcracker

        # Utility
    
        # Colour Settings
        case "99":
            print("Change Colour Settings from config/colours.py")

        # Exit
        case "0":
            print ("Until Next Time!\n")
            sleep (1)
            os.system ('cls||clear')
            exit()

        # Error Handling
        case TypeError:
            print ("[!] Error: Bad Option")

except KeyboardInterrupt:
    quit_message = input(
    Fore.LIGHTRED_EX + "\n[!] Exiting - Keyboard Interrupt" + Style.RESET_ALL).lower()
    exit()

except Exception:
    pass