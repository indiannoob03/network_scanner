#!/usr/bin/env python

import scapy.all as scapy
import argparse

# Checking for arguments and generating help menu.
def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest = "ip", help="Enter the ip range. This is mandatory")
    options = parser.parse_args()
    if not options.ip:
        parser.error("[-] Please specify an IP address, use --help for more info")
    return options

# Creating ARP request assigning Ether destination combining both the requests and broadcasting it.
def scan(ip):
    arp_request = scapy.ARP(pdst = ip)
    broadcast = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    #Using srp instead of sr because srp allows a custom ether network.
    #Give timeout 1 sec otherwise it will keep waiting for a response.
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    return answered_list

# Accepting the result from the scan function and creating a list with dictionaries in it.
def creating_dict(answers):
    clients_list = []
    for element in answers:
        client_dict = {"IP": element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(client_dict)
    return clients_list

# Displaying the result
def display(clients):
    print("IP\t\t\tMAC Address\n------------------------------------------------------")
    for client in clients:
        print(client["IP"] + "\t\t" + client["mac"])

# Function calls
options = get_arguments()
answers = scan(options.ip)
clients = creating_dict(answers)
display(clients)
