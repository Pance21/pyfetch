#!/usr/bin/python3

# to run it: python3 pyfetch.py

class bcolors:
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

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
print ("\t" + bcolors.OKGREEN + bcolors.BOLD + os.getlogin() + "@" + socket.gethostname() + bcolors.ENDC)
print ("\t-----")

import distro
import platform
distro = open('/etc/lsb-release', 'r').read()
distro = distro.replace('\n', '')
distro = distro.replace('"', '')
x=distro.find("DISTRIB_DESCRIPTION=")+20
print (bcolors.OKGREEN + bcolors.BOLD + "\tOS: " + bcolors.ENDC + distro[x:] + " " + platform.machine())

producthost = open('/sys/devices/virtual/dmi/id/product_name', 'r').read()
producthost = producthost.replace('\n', '')
productvnd = open('/sys/devices/virtual/dmi/id/sys_vendor', 'r').read()
productvnd = productvnd.replace('\n', '')
print (bcolors.OKGREEN + "\tHost: " + bcolors.ENDC + productvnd + " " + producthost)

print (bcolors.OKGREEN + "\tKernel: " + bcolors.ENDC + platform.release())
print (bcolors.OKGREEN + "\tPlatform: " + bcolors.ENDC + platform.platform())

import subprocess
de_result = subprocess.run(['cinnamon', '--version'], stdout=subprocess.PIPE)
de_result = de_result.stdout.decode('utf-8')
de_result = de_result.replace('\n', '')
print( bcolors.OKGREEN + "\tDE: " + bcolors.ENDC + de_result)
print(bcolors.OKGREEN + "\tHost Name: " + bcolors.ENDC + socket.gethostname())

import cpuinfo
from cpuinfo import get_cpu_info
info = get_cpu_info()
cores = info['count']
print(bcolors.OKGREEN + "\tCPU: " + bcolors.ENDC + info['brand_raw'] + " (" + str(cores).strip() + " cores)") 

# IP info
myip = socket.gethostbyaddr(socket.gethostname())[2]

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
internalIP = s.getsockname()[0]
s.close()

externalIP4  = os.popen('curl -s v4.ident.me').readline()
externalIP6  = os.popen('curl -s v6.ident.me').readline()
print(bcolors.OKGREEN + "\tInternal eth0 IP: " + bcolors.ENDC + internalIP)
print(bcolors.OKGREEN + "\tInternal lo IP: " + bcolors.ENDC , listToString(myip))
print(bcolors.OKGREEN + "\tExternal v4 IP: " + bcolors.ENDC + externalIP4)
print(bcolors.OKGREEN + "\tExternal v6 IP: " + bcolors.ENDC + externalIP6)
