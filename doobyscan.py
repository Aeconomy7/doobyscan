import os
import sys
import subprocess
import platform

from scapy import *
from colorama import *

def doobyscan_header():
	print(Fore.GREEN + Style.BRIGHT + "+",end='');print(Fore.MAGENTA + Style.BRIGHT + "--------------------------------------------------------",end='');print(Fore.GREEN + Style.BRIGHT + "+")
	print(Fore.YELLOW + Style.BRIGHT + "|",end='');print(Fore.CYAN + Back.BLACK + Style.BRIGHT + "        _             _                                 ",end='');print(Fore.YELLOW + Back.RESET + Style.BRIGHT + "|")
	print(Fore.YELLOW + Style.BRIGHT + "|",end='');print(Fore.CYAN + Back.BLACK + Style.BRIGHT + "       | |           | |                                ",end='');print(Fore.YELLOW + Back.RESET + Style.BRIGHT + "|")
	print(Fore.YELLOW + Style.BRIGHT + "|",end='');print(Fore.CYAN + Back.BLACK + Style.BRIGHT + "     __| | ___   ___ | |__  _   _ ___  ___ __ _ _ __    ",end='');print(Fore.YELLOW + Back.RESET + Style.BRIGHT + "|")
	print(Fore.YELLOW + Style.BRIGHT + "|",end='');print(Fore.CYAN + Back.BLACK + Style.BRIGHT + "    / _` |/ _ \ / _ \| '_ \| | | / __|/ __/ _` | '_ \   ",end='');print(Fore.YELLOW + Back.RESET + Style.BRIGHT + "|")
	print(Fore.YELLOW + Style.BRIGHT + "|",end='');print(Fore.CYAN + Back.BLACK + Style.BRIGHT + "   | (_| | (_) | (_) | |_) | |_| \__ \ (_| (_| | | | |  ",end='');print(Fore.YELLOW + Back.RESET + Style.BRIGHT + "|")
	print(Fore.YELLOW + Style.BRIGHT + "|",end='');print(Fore.CYAN + Back.BLACK + Style.BRIGHT + "    \__,_|\___/ \___/|_.__/ \__, |___/\___\__,_|_| |_|  ",end='');print(Fore.YELLOW + Back.RESET + Style.BRIGHT + "|")
	print(Fore.YELLOW + Style.BRIGHT + "|",end='');print(Fore.CYAN + Back.BLACK + Style.BRIGHT + "                             __/ |                      ",end='');print(Fore.YELLOW + Back.RESET + Style.BRIGHT + "|")
	print(Fore.YELLOW + Style.BRIGHT + "|",end='');print(Fore.CYAN + Back.BLACK + Style.BRIGHT + "                            |___/                       ",end='');print(Fore.YELLOW + Back.RESET + Style.BRIGHT + "|")
	print(Fore.YELLOW + Style.BRIGHT + "|",end='');print(Fore.BLUE + Back.BLACK + Style.BRIGHT + "   Created by Sc00by                                    ",end='');print(Fore.YELLOW + Back.RESET + Style.BRIGHT + "|")
	print(Fore.GREEN + Style.BRIGHT + "+",end='');print(Fore.MAGENTA + Style.BRIGHT + "--------------------------------------------------------",end='');print(Fore.GREEN + Style.BRIGHT + "+")

def main_menu(o,pn,pv):
	print("     1) Show network interfaces (UP)")
	print("     2) ???")
	option = input("\n[?] OPTION: ")

	if str(option) == "1":
		if pn.lower() == "linux":
			p1 = subprocess.Popen(["ifconfig"], stdout=subprocess.PIPE)
			p2 = subprocess.check_output(["sed", "s/[ \t].*//;/^\(lo\|\)$/d"], stdin=p1.stdout)
			p1.wait()
			print(p2)
		return False
	elif str(option) == "2":
		print("[-] Coming soon...")
	else:
		return True

if __name__ == '__main__':
	os_name		= os.name
	plat_name	= platform.system()
	plat_ver	= platform.release()

	# if os is windows, initialize colorama
	#if plat_name == "Windows":
	init()

	doobyscan_header()

	finish = main_menu(os_name,plat_name,plat_ver)

	while finish is False:
		finish = main_menu(os_name,plat_name,plat_ver)
