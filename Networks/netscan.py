#!/usr/bin/python3
from prettytable import PrettyTable

# Goes back a directory then imports from the Config directory
from scapy.layers.l2 import Ether, ARP
from scapy.sendrecv import srp

from Config.colours import *
from Config.commands import *

NetScanBanner()

# Display interfaces (3 commands for each OS)
ifconfig()

Seperator()
myTable = PrettyTable()

# User Prompt
ip_range = input("Enter IP Range (10.10.X.X/24): ")

Seperator()

# MAC will be replaced with Ether.src
broadcastMac = "ff:ff:ff:ff:ff:ff"

packet = Ether(dst=broadcastMac) / ARP(pdst=ip_range)

ans = srp(packet, timeout=1, verbose=0)[0]

myTable.field_names = ['IP Addresses',
                       'MAC Addresses']
myTable.padding_width = 3

for send, receive in ans:
    myTable.add_row([receive.sprintf(r"%ARP.psrc%"),
                     receive.sprintf("%Ether.src%")])

print(Fore.GREEN)
print(myTable)
print(Style.RESET_ALL)
