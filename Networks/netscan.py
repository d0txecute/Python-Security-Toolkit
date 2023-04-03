#!/usr/bin/python3
import os,sys,argparse
from colorama import *
from scapy.all import *

# Goes back a directory then imports from the Config directory
sys.path.append('..')
from Config import colours

colours.NetScanBanner()

# Display interfaces (3 commands for each OS)
os.system("ipconfig||ifconfig||ip a")

colours.Seperator()

# User Prompt
ip_range = input("Enter IP Range (10.10.X.X/24): ")

colours.Seperator()

# MAC will be replaced with Ether.src
broadcastMac = "ff:ff:ff:ff:ff:ff"

packet = Ether(dst = broadcastMac) / ARP(pdst = ip_range)

ans = srp (packet, timeout = 1, verbose=0)[0]

print (Fore.GREEN + "IP Address\t\tMAC Address")
print ("".center(40, "-"))
for send, receive in ans:
    print (receive.sprintf(r"%ARP.psrc%     %Ether.src%"))
