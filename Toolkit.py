#!/usr/bin/python3 

print ("MAIN MENU".center(80, "—"))

print ("\nNETWORK\n")
print ("1. Network Scanner")
print ("2. Port Scanner")

print ("\nWEB APPLICATION\n")
print ("3. Domain Enumerator")
print ("4. Subdomain Enumerator")

print ("\nBrute Force\n")
print ("5. Hash Cracker")

selection = input("Select a Program Number: ")
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
