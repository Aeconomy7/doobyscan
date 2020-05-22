import os
import sys
import platform

from scapy import *

if __name__ == '__main__':

    os_name     = os.name
    plat_name   = platform.system()
    plat_ver    = platform.release()
    
    print(os_name + ", " + plat_name + ", " + plat_ver)
