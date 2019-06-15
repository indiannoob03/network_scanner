# network_scanner
It is a network scanner written in python for discovering all the clients connected to the network. It also displays the MAC address of all the clients.

Requirements:

1. Python 2.7 should be installed to run this program.

Example : python network_scanner.py -t 192.168.126.144/24

usage: network_scanner.py [-h] [-t IP]

optional arguments:
  -h, --help          show this help message and exit
  -t IP, --target IP  Enter the ip range. This is mandatory
