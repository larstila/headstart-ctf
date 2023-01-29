# Headstart for CTFs

## Includes my favorite scripts to run when starting a Hackthebox box

Current version does the following scripts:

```
nmap -Pn -sV -sC -oN {ip_address}.nmap {ip_address}
ffuf -w {sub_wordlist} -u FUZZ.{hostname} -t 100 -o {hostname}.subs
ffuf -w {dir_wordlist} -u {hostname}/FUZZ -t 100 -o {hostname}.dirs
```

Default wordlists:
## Setup
CLone the repo, modify script to executable and create a symbolic link to headstart.py

```
git clone https://github.com/larstila/headstart-ctf
cd headstart-ctf
chmod +x headstart.py
ln -s <path-to-script>/headstart.py /usr/local/bin/headstart
```
Then you can run the script in any directory you want:

```
headstart -ip <ip_address> -o <name for output files>
```


###Default wordlists:
```
dir_wordlist = "/usr/share/dirb/wordlists/big.txt"
sub_wordlist = "/usr/share/wordlists/amass/subdomains-top1mil-110000.txt"
```

Special thanks to ChatGPT for helping me write this. 


# TODO add other scripts, like sqlmap 
