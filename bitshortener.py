import os
import pyshorteners
import time
from colorama import Fore
def banner_banner():
	os.system("figlet bitshortener -f banner")
def clear():
	os.system("clear")
def primary_list():
	list_primary = ["[1] shorten url", "[2] About the tool", "[3] Exit"]
	for list_x in list_primary:
		print(Fore.RED + list_x)
		time.sleep(0.3)
clear()
banner_banner()
primary_list()
user_one = int(input("===> "))
if user_one == 1:
	url_url = input("write url: ")
	shortener = pyshorteners.Shortener()
	short_url = shortener.dagd.short(f'{url_url}')
	print(f"Your shortened url: {short_url}")
elif user_one == 2:
	list_oo = ["created by: bitmap", "language used: Python 3.9.2", "text editor: sublime-text", "tool compatible with:", "Debian", "Ubuntu", "Fedora", "Termux"]
	for list_short in list_oo:
		print(Fore.GREEN + list_short)
		time.sleep(1)
elif user_one == 3:
	quit()
