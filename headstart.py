#!/usr/bin/env python

import sys, argparse, logging
import os
from utils import nmap_scan, ffuf_dir_enum, ffuf_sub_enum

def main(args, loglevel):
    logging.basicConfig(format="%(levelname)s: %(message)s", level=loglevel)
    logging.info("A script to give you a headstart to a CTF")
    logging.info("Runs nmap, direcory and subdomain enumeration with ffuf and ???")
    # TODO nmap, ffuf direcories, ffuf subdomains

    # TODO open new terminal windows for each task
    # TODO write output

    ip_address = args.hostname 
    output_file = args.output 
    logging.debug("Hostname: %s" %ip_address)
    logging.debug("Output: %s" %output_file)

    nmap_scan(ip_address, output_file)
    ffuf_dir_enum(ip_address, output_file)
    ffuf_sub_enum(ip_address, output_file)
    
if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--hostname", dest = "hostname", default = "0.0.0.0", help="Hostname/IP addr")
    parser.add_argument("-o", "--output", dest = "output", default = "output", help="Name of the service/CTF, used for saving outputs")
    parser.add_argument("-dw", "--directorywordlist", dest = "directorywordlist", default = "/usr/share/wordlist/", help="direcory wordlist")
    parser.add_argument( "-v", "--verbose", help="increase output verbosity",  action="store_true")
    # TODO User chosen tools
    args = parser.parse_args()
    
    # Setup logging
    if args.verbose:
        loglevel = logging.DEBUG
    else:
        loglevel = logging.INFO
    
    main(args, loglevel)