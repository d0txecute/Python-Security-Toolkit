#!/usr/bin/python3
import os,sys,argparse
from scapy.all import *
from Config.colours import colours

colours.NetScanBanner()

# Selections
interface = input("Select Interface (eth0, wlan0, etc): ")
ip_range = input("Enter IP Range (10.10.X.X/24): ")

# MAC will be replaced with Ether.src
broadcastMac = "ff:ff:ff:ff:ff:ff"

packet = Ether(dst = broadcastMac) / ARP(pdst = ip_range)

ans, unans = srp (packet, timeout = 1, iface = interface, inter = 0.1)

for send, receive in ans:
    print (receive.sprintf(r"%Ether.src% - %ARP.psrc%"))
