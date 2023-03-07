#!/bin/python3

import os
import shlex
import subprocess
from colorama import Fore as color

RED = color.RED
BLUE = color.BLUE
YELLOW = color.YELLOW
CYAN = color.CYAN
GREEN = color.GREEN

def banner():
	os.system('clear')
	print(f"{GREEN}")
	print("@@@@@@@")
	print("@        @    @    @@     @@@@@")
	print("@        @@  @@   @  @      @")
	print("@@@@@    @ @@ @  @    @     @")
	print("@        @    @  @@@@@@     @")
	print("@        @    @  @    @     @")
	print("@@@@@@@  @    @  @    @     @")
	print("")
	print(f"{YELLOW}[{BLUE}!!!{YELLOW}] {BLUE}Tool-Name {YELLOW}: {GREEN}Emat")
	print(f"{YELLOW}[{BLUE}!!!{YELLOW}] {BLUE}Github    {YELLOW}: {GREEN}https://github.com/K3ysTr0K3R")
	print(f"{YELLOW}[{BLUE}!!!{YELLOW}] {BLUE}Instagram {YELLOW}: {GREEN}1_k3ystr0k3r_1")
	print(f"{YELLOW}[{BLUE}!!!{YELLOW}] {BLUE}Coded By  {YELLOW}: {GREEN}K3ysTr0K3R")
	print("")
banner()

current_directory = subprocess.check_output(['pwd']).strip().decode('utf-8')
print(f'{YELLOW}[{GREEN}!{YELLOW}] {GREEN}Crawling Your Current Directory{BLUE}: {RED}{current_directory}')
print(f'{YELLOW}')

emails = subprocess.check_output(['grep', '-hrioP', r'\b[a-zA-Z0-9.-]+@[a-zA-Z0-9.-]+\.[a-zA-Z0-9.-]+\b'])
emails = emails.strip().decode('utf-8')
emails = emails.split('\n')

gmail_emails = [email for email in emails if 'gmail' in email]
yahoo_emails = [email for email in emails if 'yahoo' in email]
hotmail_emails = [email for email in emails if 'hotmail' in email]
government_emails = [email for email in emails if 'gov' in email]

gmail_encoded = '\n'.join(gmail_emails).encode('utf-8').decode('utf-8')
yahoo_encoded = '\n'.join(yahoo_emails).encode('utf-8').decode('utf-8')
hotmail_encoded = '\n'.join(hotmail_emails).encode('utf-8').decode('utf-8')
government_encoded = '\n'.join(government_emails).encode('utf-8').decode('utf-8')
banner()

if not gmail_emails:
	print('')
	print(f'{YELLOW}[{RED}~{YELLOW}] {CYAN}No Gmail accounts were found ')
	print('')
else:
	print('')
	print(f'{YELLOW}[{BLUE}+{YELLOW}] {CYAN}Gmail accounts were found ')
	print('\n'.join(gmail_emails))
	print('')

if not yahoo_emails:
	print('')
	print(f'{YELLOW}[{RED}~{YELLOW}] {CYAN}No Yahoo accounts were found')
	print('')
else:
	print('')
	print(f'{YELLOW}[{BLUE}+{YELLOW}] {CYAN}Yahoo accounts were found')
	print('\n'.join(yahoo_emails))
	print('')

if not hotmail_emails:
	print('')
	print(f'{YELLOW}[{RED}~{YELLOW}] {CYAN}No Hotmail accounts were found')
	print('')
else:
	print('')
	print(f'{YELLOW}[{BLUE}+{YELLOW}] {CYAN}Hotmail mail accounts were found')
	print('\n'.join(hotmail_emails))
	print('')

if not government_emails:
	print('')
	print(f'{YELLOW}[{RED}~{YELLOW}] {CYAN}No Government accounts were found')
	print('')
else:
	print('')
	print(f'{YELLOW}[{BLUE}+{YELLOW}] {CYAN}Government accounts were found')
	print('\n'.join(government_emails))
	print('')
