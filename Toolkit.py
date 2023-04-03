#!/usr/bin/python3 
import pyfiglet, os
from colorama import *
from time import sleep

# Clear Screen (UNIX/Windows)
os.system ('cls||clear')

# Colour Settings
from Config import colours

# Start Up Banner
colours.Banner()
colours.Copyright()

sleep(2)

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
colours.Seperator

## Utility ##
colours.Settings()
colours.Seperator()

## Exit ##
colours.Seperator()
colours.Exit()
colours.Seperator()

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

    case "99":
        os.system("Change Colour Settings from Config/colours.py")

    # Other
    case "0":
        print ("Until Next Time!\n")
        sleep (1)
        os.system ('cls||clear')
        exit()

    # Error Handling
    case TypeError:
        print ("[!] Error: Bad Option")
