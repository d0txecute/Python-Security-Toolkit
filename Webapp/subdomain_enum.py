#!/usr/bin/python3
import os,sys,argparse
from scapy.all import *

# Goes back a directory then imports from the Config directory
sys.path.append('..')
from Config import colours

colours.SubBanner()


