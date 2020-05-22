import os
import sys
import subprocess
import platform

from scapy import *

def main_menu(o,pn,pv):
	if pn.lower() == "linux":
		p1 = subprocess.Popen(["netstat", "-i"], stdout=subprocess.PIPE)
		p2 = subprocess.check_output(["grep", "eth0"], stdin=p1.stdout)
		p1.wait()
		print(p2)


if __name__ == '__main__':

	os_name		= os.name
	plat_name	= platform.system()
	plat_ver	= platform.release()

	main_menu(os_name,plat_name,plat_ver)
