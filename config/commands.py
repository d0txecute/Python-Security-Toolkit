import os
from config.colours import *


def clear():
    os.system('cls||clear')


def update():
    print(f"{Fore.YELLOW}[*] Checking for Updates{Style.RESET_ALL}")
    os.system("git pull")


def ifconfig():
    os.system("ipconfig||ifconfig||ip a")
