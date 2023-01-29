# Headstart for CTFs

## Includes my favorite scripts to run when starting a Hackthebox box

Current version does the following scripts:

```
nmap -Pn -sV -sC -oN {output_file}.nmap {ip_address}
ffuf -w {sub_wordlist} -u FUZZ.{hostname} -t 100 -o {output_file}.subs
ffuf -w {dir_wordlist} -u {hostname}/FUZZ -t 100 -o {output_file}.dirs
```


Special thanks to ChatGPT for helping me write this. 


# TODO add other scripts, like sqlmap 