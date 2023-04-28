#!/usr/bin/python3
import socket

from config.colours import *
from config.commands import *

clear()
PortScanBanner()

# Prompt the user to input the IP addresses and ports
start_ip = input(f'{Fore.BLUE}[i] Enter the starting IP address: ')
end_ip = input(f'{Fore.BLUE}[i] Enter the ending IP address: ')
ports = [int(port.strip()) for port in input(f'{Fore.BLUE}[i] Enter the port numbers separated by commas: ').split(',')]
print(Style.RESET_ALL)


# Loop through each IP address in the range and perform the port scan
for i in range(int(socket.inet_aton(start_ip).hex(), 16), int(socket.inet_aton(end_ip).hex(), 16) + 1):
    ip_address = socket.inet_ntoa(bytes.fromhex(hex(i)[2:]))
    results = []

    # Loop through each port and attempt to connect
    for port in ports:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1)
                s.connect((ip_address, port))
                service = socket.getservbyport(port)
                results.append((port, 'open', service))
        except:
            results.append((port, 'closed', '-'))

    # Print the results for the IP addresses
    print(f'{Fore.BLUE}[i] IP address: {ip_address}')
    print(f'\n{Fore.GREEN}[*] {"Port":<10} {"Status":<10} {"Service":<10}')

    count = 1

    for result in results:
        print(f'{Fore.YELLOW}[{count}] {result[0]:<10} {result[1]:<10} {result[2]:<10}')
        count += 1