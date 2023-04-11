#!/usr/bin/python3
import requests
from Config.colours import *
from Config.commands import *

SubBanner()


def domain_scan(domain_name, sub_names):
    print('Subdomains'.center(80, '-'))

    for subdomain in sub_names:
        url = f"http://{subdomain}.{domain_name}"

        try:  # Displays successful results
            requests.get(url)
            Success(url)

        # If Connection Error, skip to next subdomain
        except requests.ConnectionError:
            pass


# Wordlist Path
wordlist = os.path.abspath('Wordlists/subdomain.txt')

dom_name = input(Fore.BLUE + "[i] Enter Domain: ")
print('\n')

with open(wordlist, 'r') as file:
    name = file.read()
    sub_dom = name.splitlines()

domain_scan(dom_name, sub_dom)