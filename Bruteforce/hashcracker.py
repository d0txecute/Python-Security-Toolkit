#!/usr/bin/python3
import hashlib

# Goes back a directory then imports from the Config directory
sys.path.append('..')
from Config import colours

colours.HashCrackBanner()

wordlist_location = os.path.join(os.path.dirname(_file_), '..', 'Wordlists', 'passwords.txt')
hash_input = str(input('[+] Enter hash to be cracked: '))

# hashtype = input("[+] Enter Hash Type:").lower()

with open(wordlist_location, 'r') as file:
    for line in file.readlines():

        # Replace Sha256 with a hash type
        hash_ob = hashlib.sha256(line.strip().encode())
        hashed_pass = hash_ob.hexdigest()
        if hashed_pass == hash_input:
            print(Fore.GREEN + '[+] Password Found: ' + line.strip())
            exit(0)
