#!/usr/bin/env python

import sys, argparse, logging

def main(args, loglevel):
    logging.basicConfig(format="%(levelname)s: %(message)s", level=loglevel)
    print("ilfuhf")
    # TODO Replace this with your actual code.
    logging.debug("Your Argument: %s" %args.hostname)

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--hostname", dest = "hostname", default = "0.0.0.0", help="Hostname/IP addr")
    parser.add_argument( "-v", "--verbose", help="increase output verbosity",  action="store_true")

    args = parser.parse_args()
    
    # Setup logging
    if args.verbose:
        loglevel = logging.DEBUG
    else:
        loglevel = logging.INFO
    
    main(args, loglevel)