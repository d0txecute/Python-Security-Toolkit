#!/usr/bin/python3
import requests, os
from config.colours import *

SubBanner()

def domain_scan (domain_name, sub_names):
    print ('Subdomains'.center(80, '-'))

    for subdomain in sub_names:
        url = f"http://{subdomain}.{domain_name}"

         # Displays successful results
        try:
            requests.get(url)
            success(url)

        # If Conection Error, skip to next subdomain
        except requests.ConnectionError:
            pass

# Wordlist Path
wordlist = os.path.abspath('Wordlists/subdomain.txt')

dom_name = input(f"{Fore.YELLOW}[*] Enter Domain: {Style.RESET_ALL}")
print ('\n')

with open ("wordlists/subdomain.txt", 'r') as file:
    name = file.read()
    sub_dom = name.splitlines()

domain_scan(dom_name, sub_dom)