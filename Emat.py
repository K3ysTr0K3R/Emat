#!/bin/python3

import shlex
import subprocess

current_directory = subprocess.check_output(['pwd']).strip().decode('utf-8')
print(f'[!] Crawling Your Current Directory: {current_directory}')

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

if not gmail_emails:
	print("")
	print('[~] No Gmail accounts were found')
  print("")
else:
	print("")
	print('[+] Gmail accounts were found ')
	print("")
	print('\n'.join(gmail_emails))
	print("")

if not yahoo_emails:
	print("")
	print('[~] No Yahoo accounts were found ')
	print("")
else:
	print("")
	print('[+] Yahoo accounts were found ')
	print("")
	print('\n'.join(yahoo_emails))
	print("")

if not hotmail_emails:
	print("")
	print('[~] No Hotmail accounts were found ')
	print("")
else:
	print("")
	print('[+] Hotmail mail accounts were found ')
	print("")
	print('\n'.join(hotmail_emails))
	print("")

if not government_emails:
	print('<------------------------------->')
	print('[~] No Hotmail accounts were found ')
	print('<------------------------------->')
else:
	print("")
	print('[+] Hotmail mail accounts were found ')
	print("")
	print('\n'.join(government_emails))
	print("")
