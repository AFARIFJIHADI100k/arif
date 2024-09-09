#Coded by suyaib
#TG CHANNEL : Termux Education Empire

import os
from os import system as SUYAIB

try:
	import requests
except ModuleNotFoundError:
	SUYAIB("pip install requests")
	
def termux():
	education = input("Enter Your Target Number : ")
	empire = f"https://lxbadboy.co/truecaller/?phone={education}"
	response = requests.get(empire)
	if response.status_code == 200:
		print(response.content.decode('utf-8'))
		os.system('xdg-open https://t.me/termux_education_empire')
	else:
		print("Failed to get info")
		
termux()