import os
import sys
import subprocess
import platform

from scapy import *

def doobyscan_header():
	print("+--------------------------------------------------------+")
	print("|        _             _                                 |")
	print("|       | |           | |                                |")
	print("|     __| | ___   ___ | |__  _   _ ___  ___ __ _ _ __    |")
	print("|    / _` |/ _ \ / _ \| '_ \| | | / __|/ __/ _` | '_ \   |")
	print("|   | (_| | (_) | (_) | |_) | |_| \__ \ (_| (_| | | | |  |")
	print("|    \__,_|\___/ \___/|_.__/ \__, |___/\___\__,_|_| |_|  |")
	print("|                             __/ |                      |")
	print("|                            |___/                       |")
	print("|   Created by Sc00by                                    |")
	print("+--------------------------------------------------------+\n")


def main_menu(o,pn,pv):
	print("     1) Show network interfaces (UP)")
	print("     2) ???")
	option = input("\n[?] OPTION: ")

	if str(option) == "1":
		if pn.lower() == "linux":
			p1 = subprocess.Popen(["netstat", "-i"], stdout=subprocess.PIPE)
			p2 = subprocess.check_output(["grep", "eth0"], stdin=p1.stdout)
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

	doobyscan_header()

	finish = main_menu(os_name,plat_name,plat_ver)

	while finish is False:
		finish = main_menu(os_name,plat_name,plat_ver)
