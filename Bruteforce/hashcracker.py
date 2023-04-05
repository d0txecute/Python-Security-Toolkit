#!/usr/bin/python3
import hashlib, os, sys
from colorama import *

# Goes back a directory then imports from the Config directory
sys.path.append('..')
from Config import colours
os.system('cls||clear')

colours.HashCrackBanner()

wordlist_location = os.path.abspath('Wordlists/passwords.txt')

def hash_cracker(hash_input, hashtype):
    with open(wordlist_location, 'r') as file:
        for line in file.readlines():

            hash_obj = hashtype(line.strip().encode())
            hashed_pass = hash_obj.hexdigest()
            if hashed_pass == hash_input:
                print(Fore.GREEN + '\n[+] Password Found: ' + line.strip())
                break
        else:
            print(Fore.RED + '\n[-] Password Not Found')

#Choose hashing algorithm and type in the hash to be cracked
def set_hashing_algorithm():
    hash_input = input(str(Fore.BLUE + '[i] Enter hash to be cracked: '))
    hashtype = input(str(Fore.BLUE + "\n[1] SHA1\n[2] SHA224\n[3] SHA256\n[4] SHA384\n[5] SHA512\n[6] MD5\n[+] Enter Hash Type(number): "))
    print (Style.RESET_ALL)
    match hashtype:
        case '1':
            hash_cracker(hash_input, hashlib.sha1)
        case '2':
            hash_cracker(hash_input, hashlib.sha224)
        case '3':
            hash_cracker(hash_input, hashlib.sha256)
        case '4':
            hash_cracker(hash_input, hashlib.sha384)
        case '5':
            hash_cracker(hash_input, hashlib.sha512)
        case '6':
            hash_cracker(hash_input, hashlib.md5)
        case _:
            print(Fore.RED + "\n[-] Incorrect input.\nPlease enter a number.")

while(True):
    set_hashing_algorithm()
    
    decision = input(str(Fore.BLUE + '\n[i] Do you want to enter another hash? (y/n): ')).lower()
    print('=' * 80)
    if decision == 'y':
        continue
    else:
        exit(0)

