import os, logging

logging.basicConfig(format="%(levelname)s: %(message)s", level=INFO)

def run_command(command):
    os.system(f"gnome-terminal -x bash -c '{command}; exec bash'")

def nmap_scan(ip_address, output_file):
    logging.info("Starting nmap")
    run_command(f"nmap -oN {output_file} {ip_address}")

def ffuf_dir_enum(ip_address, output_file):
    logging.info("Starting ffuf direcory enumeration")
    run_command(f"ffuf -w /usr/share/dirb/wordlists/big.txt -u {ip_address}/FUZZ -t 100 -o {output_file}")

def ffuf_sub_enum(ip_address, output_file):
    logging.info("Starting subdomain enumeration")
    run_command(f"ffuf -w /usr/share/seclists/Discovery/DNS/bitquark-subdomains-top100000.txt -u {ip_address}/FUZZ -t 100 -o {output_file}")