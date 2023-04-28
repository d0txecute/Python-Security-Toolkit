#!/usr/bin/python3
import hashlib

from config.colours import *
from config.commands import *

clear()
HashCrackBanner()

def hash_cracker(hash_input, hashtype):
    with open("wordlists/passwords.txt", 'r') as file:
        for line in file.readlines():

            hash_obj = hashtype(line.strip().encode())
            hashed_pass = hash_obj.hexdigest()
            if hashed_pass == hash_input:
                success("Password Found: " + line)
                break
        else:
            fail('Password Not Found')


# Choose hashing algorithm and type in the hash to be cracked
def set_hashing_algorithm():
    hash_input = input(str(f'{Fore.BLUE}[i] Enter hash to be cracked: '))
    hashtype = input(str(f'{Fore.BLUE}\n[1] SHA1\n[2] SHA224\n[3] SHA256\n[4] SHA384\n[5] SHA512\n[6] MD5\n[+] Enter Hash Type(number): '))
    print(Style.RESET_ALL)
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
            fail("\nIncorrect input.\nPlease enter a number (1 - 6).")


while True:
    set_hashing_algorithm()

    decision = input(str(Fore.BLUE + '\n[i] Do you want to enter another hash? (y/n): '+Style.RESET_ALL)).lower()
    print('=' * 80)
    if decision == 'y':
        continue
    else:
        exit(0)
