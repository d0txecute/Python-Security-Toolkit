#!/usr/bin/python3
import socket
from config.colours import *
from config.commands import *


clear()
PortScanBanner()


    # Prompt the user to input the IP addresses and ports
start_ip = input(
    f'{Fore.BLUE}[i] Enter the starting IP address: {Style.RESET_ALL}'
)
end_ip = input(
    f'{Fore.BLUE}[i] Enter the ending IP address: {Style.RESET_ALL}'
)

class portScan(start_ip, end_ip):
    # Loop through each IP address in the range and perform the port scan
    for i in range(int(socket.inet_aton(start_ip).hex(), 16), 
                int(socket.inet_aton(end_ip).hex(), 16) + 1):
        ip_address = socket.inet_ntoa(bytes.fromhex(hex(i)[2:]))
        results = []


        # Loop through each port and attempt to connect
        for port in range(1, 65535):
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.settimeout(1)
                    s.connect((ip_address, port))
                    service = socket.getservbyport(port)
                    results.append((port, 'open', service))
            except Exception:
                pass


        # Print the results for the IP addresses
        info("IP address: ")
        process(f'{"Port":<10} {"Status":<10} {"Service":<10}')
        count = 1


        for result in results:
            print(f'{Fore.YELLOW}[{count}] {result[0]:<10} {result[1]:<10} {result[2]:<10}')
            count += 1
        print(Style.RESET_ALL)

portScan(start_ip, end_ip)