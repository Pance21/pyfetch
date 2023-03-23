#!/usr/bin/python3

# to run it: python3 pyfetch.py

class bcolors:
    OKGREEN = '\033[92m'
    OKBLUE = '\033[94m'
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
print (bcolors.OKBLUE + "\t---- system/software -------" + bcolors.ENDC)

import distro
import platform
import os.path
path = '/etc/lsb-release'		# works with Mint
check_file = os.path.isfile(path)
if check_file:
	distro = open(path, 'r').read()
	distro = distro.replace('\n', '')
	distro = distro.replace('"', '')
	xstart=distro.find("DISTRIB_DESCRIPTION=")+20
	print (bcolors.OKGREEN + bcolors.BOLD + "\tOS: " + bcolors.ENDC + distro[xstart:] + " " + platform.machine())
else:
	path = '/etc/os-release'		# maybe other distros
	check_file = os.path.isfile(path)
	if check_file:
		distro = open(path, 'r').read()
		distro = distro.replace('\n', '')
		distro = distro.replace('"', '')
		xstart=distro.find("PRETTY_NAME=")+12
		xstop=distro.find("VERSION_ID")
		print (bcolors.OKGREEN + bcolors.BOLD + "\tOS: " + bcolors.ENDC + distro[xstart:xstop] + " " + platform.machine())
	else:
		# place code here for other distros
		print (bcolors.OKGREEN + bcolors.BOLD + "\tOS: " + bcolors.ENDC + "try another method for OS.")
		

path = '/etc/linuxmint/info'		# works with Mint
check_file = os.path.isfile(path)
if check_file:
	distro = open(path, 'r').read()
	xstart=distro.find("Cinnamon")
	if xstart>1:
		import subprocess
		de_result = subprocess.run(['cinnamon', '--version'], stdout=subprocess.PIPE)
		de_result = de_result.stdout.decode('utf-8')
		de_result = de_result.replace('\n', '')
	else:
		de_result = "try another method for DE."

print( bcolors.OKGREEN + "\tDE: " + bcolors.ENDC + de_result)
	
print (bcolors.OKGREEN + "\tKernel: " + bcolors.ENDC + platform.release())
print (bcolors.OKGREEN + "\tPlatform: " + bcolors.ENDC + platform.platform())
	
print (bcolors.OKBLUE + "\t---- hardware -------" + bcolors.ENDC)

path = '/sys/devices/virtual/dmi/id/product_name'		# works with Mint
check_file = os.path.isfile(path)
if check_file:
	producthost = open(path, 'r').read()
	producthost = producthost.replace('\n', '')
	productvnd = open('/sys/devices/virtual/dmi/id/sys_vendor', 'r').read()
	productvnd = productvnd.replace('\n', '')
	print (bcolors.OKGREEN + "\tComputer vendor: " + bcolors.ENDC + productvnd + " " + producthost)
else:
	de_result = "try another method for vendor."

#import cpuinfo
#from cpuinfo import get_cpu_info
# this works but is too slow!
#info = get_cpu_info()
#cores = info['count']
#print(bcolors.OKGREEN + "\tCPU: " + bcolors.ENDC + info['brand_raw'] + " (" + str(cores).strip() + " cores)") 

# same info as above, but much faster
de_result = subprocess.run(['cat /proc/cpuinfo'], stdout=subprocess.PIPE, shell=True)
de_result = de_result.stdout.decode('utf-8')
de_result = de_result.replace('\n', '')
de_result = de_result.replace('\t', '')
xstart=de_result.find("model name")+12
xstop=de_result.find("stepping")
xstart2=de_result.find("siblings")+10
xstop2=de_result.find("core id")
print( bcolors.OKGREEN + "\tCPU: " + bcolors.ENDC + de_result[xstart:xstop]+ " (" + de_result[xstart2:xstop2] + " cores)") 

de_result = subprocess.run(['grep MemTotal /proc/meminfo'], stdout=subprocess.PIPE, shell=True)
de_result = de_result.stdout.decode('utf-8')
de_result = de_result.replace('MemTotal:       ', '')
de_result = de_result.replace(' kB', '')
de_result = f'{int(de_result):,}'
print( bcolors.OKGREEN + "\tRAM: " + bcolors.ENDC + de_result + ' kB')

de_result = subprocess.run(['lspci | grep \'HD Graph\''], stdout=subprocess.PIPE, shell=True)
de_result = de_result.stdout.decode('utf-8')
de_result = de_result.replace('VGA compatible controller: ', '')
print( bcolors.OKGREEN + "\tGraphics: " + bcolors.ENDC + de_result[8:])

print (bcolors.OKBLUE + "\t---- internet -------" + bcolors.ENDC)

print(bcolors.OKGREEN + "\tNetwork Host Name: " + bcolors.ENDC + socket.gethostname())

# IP info
myip = socket.gethostbyaddr(socket.gethostname())[2]
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
internalIP = s.getsockname()[0]
s.close()

#externalIP4  = os.popen('curl -s v4.ident.me').readline()  #slower
externalIP4  = os.popen('curl -s ifconfig.me').readline()   #faster
#externalIP6  = os.popen('curl -s v6.ident.me').readline()	#slower
externalIP6  = os.popen('curl -s icanhazip.com').readline()	#faster
print(bcolors.OKGREEN + "\tInternal eth0 IP: " + bcolors.ENDC + internalIP)
print(bcolors.OKGREEN + "\tInternal lo IP: " + bcolors.ENDC , listToString(myip))
print(bcolors.OKGREEN + "\tExternal v4 IP: " + bcolors.ENDC + externalIP4)
print(bcolors.OKGREEN + "\tExternal v6 IP: " + bcolors.ENDC + externalIP6)

print (bcolors.OKBLUE + "\t---- apps -------" + bcolors.ENDC)
de_result = subprocess.run(['bash', '--version'], stdout=subprocess.PIPE)
de_result = de_result.stdout.decode('utf-8')
de_result = de_result.replace('\n', '')
xstop=de_result.find("Copyright")
print( bcolors.OKGREEN + "\tShell: " + bcolors.ENDC, de_result[:xstop])

de_result = subprocess.run(['python3', '--version'], stdout=subprocess.PIPE)
de_result = de_result.stdout.decode('utf-8')
de_result = de_result.replace('\n', '')
print( bcolors.OKGREEN + "\tpython3: " + bcolors.ENDC, de_result)

print (bcolors.OKBLUE + "\t---- libs -------" + bcolors.ENDC)
de_result = subprocess.run(['dpkg -l libgtk-*-common | grep -e \'^i\' | grep -e \'libgtk-*[3-6]\''], stdout=subprocess.PIPE, shell=True)
de_result = de_result.stdout.decode('utf-8')
de_result = de_result.replace('ii  ', '')
print( bcolors.OKGREEN + "\tGTK:" + bcolors.ENDC +"\n" + de_result)
de_result = subprocess.run(['dpkg -l qt5* | grep -e \'^i\''], stdout=subprocess.PIPE, shell=True)
de_result = de_result.stdout.decode('utf-8')
de_result = de_result.replace('ii  ', '')
print( bcolors.OKGREEN + "\tQT:" + bcolors.ENDC +"\n" + de_result)
