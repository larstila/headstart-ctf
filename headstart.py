#!/usr/bin/env python

import sys, argparse, logging
import os
import subprocess

#You can change the used wordlists

dir_wordlist = "/usr/share/dirb/wordlists/big.txt"
sub_wordlist = "/usr/share/seclists/Discovery/DNS/bitquark-subdomains-top100000.txt"

def run_command(command):
    os.system(command)

def nmap_scan():
    logging.info("Starting nmap")
    run_command(f"nmap -Pn -sV -sC -oN {output_file}.nmap {ip_address}")

def ffuf_dir_enum():
    logging.info("Starting ffuf direcory enumeration")
    run_command(f"ffuf -w {dir_wordlist} -u {hostname}/FUZZ -t 100 -o {output_file}.dirs")

def ffuf_sub_enum():
    logging.info("Starting subdomain enumeration")
    run_command(f"ffuf -w {sub_wordlist} -u FUZZ.{hostname} -t 100 -o {output_file}.subs")

def check_tools():
    tools = ['nmap', 'ffuf']
    for tool in tools:
        try:
            subprocess.run([tool, '--version'], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            logging.info(f"{tool} is installed.")
        except subprocess.CalledProcessError:
            logging.info(f"Error: {tool} is not installed.")
            sys.exit(1)

def main(args, loglevel):
    logging.basicConfig(format="%(levelname)s: %(message)s", level=loglevel)
    logging.info("A script to give you a headstart to a CTF")
    logging.info("Runs nmap, direcory and subdomain enumeration with ffuf and ???")

    check_tools()
    
    try:
        hostname = args.hostname
    except AttributeError:
        hostname = args.ip_address
    
    ip_address = args.ip_address
    output_file = args.output

    logging.debug("Hostname: %s" %ip_address)
    logging.debug("Output: %s" %output_file)

    nmap_scan()
    ffuf_dir_enum()
    ffuf_sub_enum()
    
if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-ip", "--ip_address", dest = "ip_address", default = "", help="IP addr")
    parser.add_argument("-u", "--hostname", dest = "hostname", default = "0.0.0.0", help="Hostname")
    parser.add_argument("-o", "--output", dest = "output", default = "output", help="Name of the service/CTF, used for saving outputs")
    # TODO parser.add_argument("-dw", "--directorywordlist", dest = "directorywordlist", default = "/usr/share/wordlist/", help="direcory wordlist")
    parser.add_argument( "-v", "--verbose", help="increase output verbosity",  action="store_true")
    # TODO User chosen tools
    args = parser.parse_args()
    
    # Setup logging
    if args.verbose:
        loglevel = logging.DEBUG
    else:
        loglevel = logging.INFO
    
    main(args, loglevel)