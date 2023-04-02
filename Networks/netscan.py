#!/usr/bin/python3

print ("Network Scanner".center(80, "—"))

from scapy.all import *

# Select Interface ex. eth0
interface = f"{sys.argv[1]}"

# Select IP Range ex. 10.10.X.X/24
ip_range = f"{sys.argv[2]}"
broadcastMac = "ff:ff:ff:ff:ff:ff"
packet = Ether(dst=broadcastMac)/ARP(pdst = ip_range)

ans, unans = srp(packet, timeout =2, iface=interface, inter=0.1)

for send,receive in ans:
       print (receive.sprintf(r"%Ether.src% - %ARP.psrc%"))
