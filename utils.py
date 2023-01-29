import os, logging, sys

logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.INFO)

#You can change the used wordlists

dir_wordlist = "/usr/share/dirb/wordlists/big.txt"
sub_wordlist = "/usr/share/seclists/Discovery/DNS/bitquark-subdomains-top100000.txt"


def run_command(command):
    os.system(command)

def nmap_scan(ip_address, output_file):
    logging.info("Starting nmap")
    run_command(f"nmap -Pn -sV -sC -oN {output_file}.nmap {ip_address}")

def ffuf_dir_enum(hostname, output_file):
    logging.info("Starting ffuf direcory enumeration")
    run_command(f"ffuf -w {dir_wordlist} -u {hostname}/FUZZ -t 100 -o {output_file}")

def ffuf_sub_enum(hostname, output_file):
    logging.info("Starting subdomain enumeration")
    run_command(f"ffuf -w {sub_wordlist} -u FUZZ.{hostname} -t 100 -o {output_file}")

import subprocess

def check_tools():
    tools = ['nmap', 'ffuf']
    for tool in tools:
        try:
            subprocess.run([tool, '--version'], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            logging.info(f"{tool} is installed.")
        except subprocess.CalledProcessError:
            logging.info(f"Error: {tool} is not installed.")
            sys.exit(1)
