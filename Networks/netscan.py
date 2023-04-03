#!/usr/bin/python3
import os,sys,argparse
from scapy.all import *

# Goes back a directory then imports from the Config directory
sys.path.append('..')
from Config import colours

colours.NetScanBanner()

# Display interfaces
os.system("ipconfig||ifconfig||ip a")

colours.Seperator()

# User Prompts
ip_range = input("Enter IP Range (10.10.X.X/24): ")

# MAC will be replaced with Ether.src
broadcastMac = "ff:ff:ff:ff:ff:ff"

packet = Ether(dst = broadcastMac) / ARP(pdst = ip_range)

ans = srp (packet, timeout = 1, verbose=0)[0]

for send, receive in ans:
    print (receive.sprintf(r"%Ether.src% - %ARP.psrc%"))
