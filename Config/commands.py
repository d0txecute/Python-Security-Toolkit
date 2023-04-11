import os
from Config.colours import *


def clear():
    os.system('cls||clear')


def update():
    process("Checking for Updates")
    os.system("git pull")


def ifconfig():
    os.system("ipconfig||ifconfig||ip a")
