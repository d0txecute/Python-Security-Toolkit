#!/usr/bin/python3 
from time import sleep
from config.colours import *
from config.commands import update
# Update on start up
update()

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
            info("Until Next Time!\n")
            sleep(1)
            clear()
            exit()

        # Error Handling
        case TypeError:
            fail("Error: Bad Option")

except KeyboardInterrupt:
    quit_message = input(
    Fore.LIGHTRED_EX + "\n[!] Exiting - Keyboard Interrupt" + Style.RESET_ALL).lower()
    exit()

except Exception as e:
    fail(e)
    exit()