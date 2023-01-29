#!/usr/bin/env python

import sys, argparse, logging
import os
import subprocess

#You can change the used wordlists

dir_wordlist = "/usr/share/dirb/wordlists/big.txt"
sub_wordlist = "/usr/share/wordlists/amass/subdomains-top1mil-110000.txt "
hostname = ""; 
ip_address ="";
subdomains = True


def run_command(command):
    os.system(command)

def nmap_scan():
    logging.info("Starting nmap")
    run_command(f"nmap -Pn -sV -sC -oN {ip_address}.nmap {ip_address}")

def ffuf_dir_enum():
    logging.info("Starting ffuf direcory enumeration")
    run_command(f"ffuf -w {dir_wordlist} -u {hostname}/FUZZ -t 100 -o {hostname}.dirs")

def ffuf_sub_enum():
    print(subdomains)
    if (subdomains):
        logging.info("Starting subdomain enumeration")
        run_command(f"ffuf -w {sub_wordlist} -u FUZZ.{hostname} -t 100 -o {hostname}.subs")
    else:
        logging.info("Subdomain enumeration not possible, please define hostname with -u")


def main(args, loglevel):
    logging.basicConfig(format="%(levelname)s: %(message)s", level=loglevel)
    logging.info("A script to give you a headstart to a CTF")

    try:
        hostname = args.hostname
        print(args.hostname + "HOSTNAME??!?!?")
    except AttributeError:
        subdomains = False
        hostname = args.ip_address
        print(subdomains + "HOSTNAME??!?!?")
    ip_address = args.ip_address

    nmap_scan()
    ffuf_dir_enum()
    ffuf_sub_enum()
    
if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-ip", "--ip_address", dest = "ip_address", default = "", help="IP addr")
    parser.add_argument("-u", "--hostname", dest = "hostname", help="Hostname")
    parser.add_argument( "-v", "--verbose", help="increase output verbosity",  action="store_true")
    # TODO User chosen tools
    args = parser.parse_args()
    
    # Setup logging
    if args.verbose:
        loglevel = logging.DEBUG
    else:
        loglevel = logging.INFO
    
    main(args, loglevel)