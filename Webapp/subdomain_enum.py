#!/usr/bin/python3

import requests,sys,os

print ("Subdomain Enumerator".center(80, '-'))

def domain_scan(domain_name,sub_names):
    print('\n----URL after scanning subdomains----\n')

    for subdomain in sub_names:
        url = f"http://{subdomain}.{domain_name}"

        try:
            requests.get(url)
            print(f'[+] {url}')

        # If invalid then go to the next
        except requests.ConnectionError:
            pass

if __name__ == '__main__':
    dom_name = input("Enter a Domain: ")
    
    wordlist = input("Enter a Wordlist Path: ")
    with open (wordlist, 'r') as file:
        name = file.read()
        sub_dom = name.splitlines()

    domain_scan(dom_name,sub_dom)
