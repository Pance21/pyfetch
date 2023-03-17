# to run it: python3 pyfetch.py

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Function to convert list to string
def listToString(s):
    # initialize an empty string
    str1 = ""
 
    # traverse the list and store in the string
    for ele in s:
        str1 += ele
 
    # return string
    return str1

import os
import socket
print (bcolors.OKGREEN + bcolors.BOLD + os.getlogin() + "@" + socket.gethostname() + bcolors.ENDC)
print ("-----")

import distro
import platform
distro = open('/etc/lsb-release', 'r').read()
distro = distro.replace('\n', '')
distro = distro.replace('"', '')
x=distro.find("DISTRIB_DESCRIPTION=")+20
print (bcolors.OKGREEN + "OS: " + bcolors.ENDC + distro[x:] + " " + platform.machine())
# also: cat /etc/issue  # Linux Mint 21.1 Vera \n \l

producthost = open('/sys/devices/virtual/dmi/id/product_name', 'r').read()
producthost = producthost.replace('\n', '')
productvnd = open('/sys/devices/virtual/dmi/id/sys_vendor', 'r').read()
productvnd = productvnd.replace('\n', '')
print (bcolors.OKGREEN + "Host: " + bcolors.ENDC + productvnd + " " + producthost)

print (bcolors.OKGREEN + "Kernel: " + bcolors.ENDC + platform.release())
print (bcolors.OKGREEN + "Platform: " + bcolors.ENDC + platform.platform())

import subprocess
de_result = subprocess.run(['cinnamon', '--version'], stdout=subprocess.PIPE)
de_result = de_result.stdout.decode('utf-8')
de_result = de_result.replace('\n', '')
print( bcolors.OKGREEN + "DE: " + bcolors.ENDC + de_result)
print(bcolors.OKGREEN + "Host: " + bcolors.ENDC + socket.gethostname())

myip = socket.gethostbyaddr(socket.gethostname())[2]

import cpuinfo
from cpuinfo import get_cpu_info
info = get_cpu_info()
print(bcolors.OKGREEN + "CPU: " + bcolors.ENDC + info['brand_raw'])  #Intel(R) Core(TM) i7-6700 CPU @ 3.40GHz

externalIP  = os.popen('curl -s ifconfig.me').readline()
print(bcolors.OKGREEN + "Internal IP: " + bcolors.ENDC , listToString(myip))
print(bcolors.OKGREEN + "External IP: " + bcolors.ENDC + externalIP)
