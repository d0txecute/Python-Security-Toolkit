#!/usr/bin/python3
import hashlib, os, sys
from colorama import Fore

# Goes back a directory then imports from the Config directory
sys.path.append('..')
from Config import colours

colours.HashCrackBanner()

wordlist_location = os.path.abspath('../Python-Security-Toolkit/Wordlists/passwords.txt')

#Class containing hashing algorithms crackers functions
class HashingAlgorithmsCracker:
    def sha256_cracker(hash_input):
        with open(wordlist_location, 'r') as file:
            for line in file.readlines():

                # Replace Sha256 with a hash type
                hash_ob = hashlib.sha256(line.strip().encode())
                hashed_pass = hash_ob.hexdigest()
                if hashed_pass == hash_input:
                    print(Fore.GREEN + '[+] Password Found: ' + line.strip())
                    break
            else:
                print(Fore.RED + '[+] Password Not Found')

    def sha1_cracker(hash_input):
        with open(wordlist_location, 'r') as file:
            for line in file.readlines():

                # Replace Sha256 with a hash type
                hash_ob = hashlib.sha1(line.strip().encode())
                hashed_pass = hash_ob.hexdigest()
                if hashed_pass == hash_input:
                    print(Fore.GREEN + '[+] Password Found: ' + line.strip())
                    break
            else:
                print(Fore.RED + '[+] Password Not Found')

#Choose hashing algorithm
def set_hashing_algorithm(hash_input, hashtype):
    if hashtype == 'sha256':
        HashingAlgorithmsCracker.sha256_cracker(hash_input)
    if hashtype == 'sha1':
        HashingAlgorithmsCracker.sha1_cracker(hash_input)

while(True):
    hash_input = str(input('[+] Enter hash to be cracked: '))
    hashtype = input("[+] Enter Hash Type: ").lower()

    set_hashing_algorithm(hash_input, hashtype)
    
    decision = input(str(Fore.WHITE + '[+] Do you want to enter another hash? (y/n): ')).lower()
    print('\n')
    if decision == 'y':
        continue
    else:
        exit(0)
