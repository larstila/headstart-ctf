# Headstart for CTFs

## Includes my favorite scripts to run when starting a Hackthebox box

Current version does the following scripts:

```
nmap -Pn -sV -sC -oN {ip_address}.nmap {ip_address}
ffuf -w {sub_wordlist} -u FUZZ.{hostname} -t 100 -o {hostname}.subs
ffuf -w {dir_wordlist} -u {hostname}/FUZZ -t 100 -o {hostname}.dirs
```

Default wordlists:
```
dir_wordlist = "/usr/share/dirb/wordlists/big.txt"
sub_wordlist = "/usr/share/seclists/Discovery/DNS/bitquark-subdomains-top100000.txt"
```

Special thanks to ChatGPT for helping me write this. 


# TODO add other scripts, like sqlmap 
