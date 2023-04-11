#!/usr/bin/python3

from time import sleep
from Config.colours import *
from Config.commands import *

# Update on start up
print("Updating Repo")

sleep(1)
# Clear Screen (Windows/*NIX)
clear()

# Start Up Banner
Banner()
Copyright()
sleep(1)
clear()

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
            from Networks import netscan

        case "2":
            from Networks import portscan

        # Web Application
        case "3":
            from Webapp import directory_enum

        case "4":
            from Webapp import subdomain_enum

        # Brute Force
        case "5":
            from Bruteforce import hashcracker

        # Utility

        # Colour Settings
        case "99":
            Info("Change Colour Settings from Config/colours.py")

        # Exit
        case "0":
            Info("Until Next Time!\n")
            sleep(1)
            clear()
            exit()

        # Error Handling
        case TypeError:
            Fail("Error: Bad Option")

except KeyboardInterrupt:
    quit_message = input(
        Fore.LIGHTRED_EX + "\n[!] Are you sure you want to quit? (yes/no): " + Style.RESET_ALL).lower()
    if quit_message == 'y' or quit_message == 'yes':
        exit()
    else:
        pass
