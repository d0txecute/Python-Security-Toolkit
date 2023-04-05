#!/usr/bin/python3 
import pyfiglet, os
from colorama import *
from time import sleep

# Update on start up
print ("Updating Repo")
os.system ("git pull")
sleep(1)
# Clear Screen (Windows/*NIX)
os.system ('cls||clear')

# Colour Settings
from Config import colours

# Start Up Banner
colours.Banner()
colours.Copyright()

sleep(1)

os.system ('cls||clear')

# Print Menu
colours.Menu()

## Networks ## 
colours.Network()
colours.Seperator()

## Web Applications ##
colours.Webapp()
colours.Seperator()

## Brute Force ##
colours.Brute()
colours.Seperator()

## Utility ##
colours.Settings()

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
        os.system("Change Colour Settings from Config/colours.py")

    # Exit
    case "0":
        print ("Until Next Time!\n")
        sleep (1)
        os.system ('cls||clear')
        exit()

    # Error Handling
    case TypeError:
        print ("[!] Error: Bad Option")
