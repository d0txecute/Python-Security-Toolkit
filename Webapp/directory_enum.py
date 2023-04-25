#!/usr/bin/python3
import requests
from config.colours import *

DirBanner()

def domain_scan(domain_name,dir_names):
    print('')
    print(Fore.LIGHTCYAN_EX + '[ Directory Listing ]'.center(80, "—")   + Style.RESET_ALL)
    print('')

    for directories in dir_names:
        url = f"http://{domain_name}/{directories}.html"

        r = requests.get(url)
        if r.status_code != 404:
            requests.get(url)
            print(f'{Fore.GREEN}[+] {url}{Style.RESET_ALL}')
     

dom_name = input(f"{Fore.YELLOW}[*] Enter a Domain: {Style.RESET_ALL}")

with open ("wordlists/common.txt", 'r') as file:
    name = file.read()
    dir_dom = name.splitlines()

domain_scan(dom_name,dir_dom)