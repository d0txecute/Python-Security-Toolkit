# Cyber Essentials Project

Python Security Toolkit is a small project aimed to package multiple tools into one place. It is (semi)-easily customisable to your requirements.

## Demo

## Information

This is a multi-tool built with Python and Bash that can:
- Bruteforce Password Hashes 
- Bruteforce Web Directories
- Bruteforce Subdomains
- Perform Network Discovery 
- Perform Port Discovery

## Requirements & Installation 

- [Wireshark](https://www.wireshark.org/download.html)
- [Npcap](https://npcap.com)

```powershell
git clone https://github.com/d0txecute/Python-Security-Toolkit
cd Python-Security-Toolkit
pip install -r requirements.txt
```

## Usage

```powershell
python Toolkit.py

—————————————————————————————————[ MAIN MENU ]—————————————————————————————————
NETWORK

1. Network Scanner
2. Port Scanner
--------------------------------------------------------------------------------
WEB APPLICATION

3. Domain Enumerator
4. Subdomain Enumerator
--------------------------------------------------------------------------------
BRUTE FORCE

5. Hash Cracker
--------------------------------------------------------------------------------
0. Exit
--------------------------------------------------------------------------------

Select a Program Number:
```

## Tool List
### Network
- [Port Scanner](Networks/portscan.py)
- [Network Scanner](Networks/netscan.py)

### Web
- [Directory Enumeration](Webapp/directory_enum.py)
- [Subdomain Enumeration](Webapp/subdomain_enum.py)

### Bruteforce
- [Hash Cracker](Bruteforce/hashcracker.py) 

## Configuration
- [Colours](Config/colours.py)
- [Main Program](Toolkit.py)
