import os, logging

logging.basicConfig(format="%(levelname)s: %(message)s", level=INFO)

#You can change the used wordlists

dir_wordlist = "/usr/share/dirb/wordlists/big.txt"
sub_wordlist = "/usr/share/seclists/Discovery/DNS/bitquark-subdomains-top100000.txt"


def run_command(command):
    os.system(f"gnome-terminal -x bash -c '{command}; exec bash'")

def nmap_scan(ip_address, output_file):
    logging.info("Starting nmap")
    run_command(f"nmap -Pn -sV -sC -oN {output_file}.nmap {ip_address}")

def ffuf_dir_enum(ip_address, output_file):
    logging.info("Starting ffuf direcory enumeration")
    run_command(f"ffuf -w {dir_wordlist} -u {ip_address}/FUZZ -t 100 -o {output_file}")

def ffuf_sub_enum(ip_address, output_file):
    logging.info("Starting subdomain enumeration")
    run_command(f"ffuf -w {sub_wordlist} -u FUZZ.{ip_address} -t 100 -o {output_file}")