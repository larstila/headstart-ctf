#!/usr/bin/env python

import sys, argparse, logging
import os
from utils import check_tools, nmap_scan, ffuf_dir_enum, ffuf_sub_enum

def main(args, loglevel):
    logging.basicConfig(format="%(levelname)s: %(message)s", level=loglevel)
    logging.info("A script to give you a headstart to a CTF")
    logging.info("Runs nmap, direcory and subdomain enumeration with ffuf and ???")

    check_tools()
    # TODO nmap, ffuf direcories, ffuf subdomains

    # TODO open new terminal windows for each task
    # TODO write output
    try:
        hostname = args.hostname
    except AttributeError:
        hostname = args.ip_address
    ip_address = args.ip_address
    output_file = args.output

    logging.debug("Hostname: %s" %ip_address)
    logging.debug("Output: %s" %output_file)

    nmap_scan(ip_address, output_file)
    ffuf_dir_enum(hostname, output_file)
    ffuf_sub_enum(hostname, output_file)
    
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