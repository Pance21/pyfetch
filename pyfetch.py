#!/usr/bin/python3

# to run it: python3 pyfetch.py
# cp pyfetch.py /usr/bin/pyfetch
# https://github.com/Pance21/pyfetch

"""Module similar to neofetch."""

import platform
import socket
import os
import os.path
import subprocess
import distro

# declare constants
OKGREEN = '\033[92m'
OKBLUE = '\033[94m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'

print("\t" + OKGREEN + BOLD + os.getlogin() + "@" + socket.gethostname() + ENDC)
print(OKBLUE + "\t---- system/software -------" + ENDC)

PATH = '/etc/lsb-release'        # works with Mint
check_file = os.path.isfile(PATH)
if check_file:
    with open(PATH, "r", encoding="utf8") as f:
        distro = f.read()
    distro = distro.replace('\n', '')
    distro = distro.replace('"', '')
    xstart = distro.find("DISTRIB_DESCRIPTION=") + 20
    print(OKGREEN + BOLD + "\tOS: " + ENDC
          + distro[xstart:] + " " + platform.machine())
else:
    PATH = '/etc/os-release'        # maybe other distros
    check_file = os.path.isfile(PATH)
    if check_file:
        with open(PATH, "r", encoding="utf8") as f:
            distro = f.read()
        distro = distro.replace('\n', '')
        distro = distro.replace('"', '')
        xstart = distro.find("PRETTY_NAME=") + 12
        xstop = distro.find("VERSION_ID")
        print(OKGREEN + BOLD + "\tOS: " + ENDC
              + distro[xstart:xstop] + " " + platform.machine())
    else:
        # place code here for other distros
        print(OKGREEN + BOLD + "\tOS: " + ENDC + "try another method for OS.")

PATH = '/etc/linuxmint/info'        # works with Mint
check_file = os.path.isfile(PATH)
if check_file:
    with open(PATH, "r", encoding="utf8") as f:
        distro = f.read()
    xstart = distro.find("Cinnamon")
    if xstart > 1:
        DE_RESULT = subprocess.run(['/usr/bin/cinnamon', '--version'],
                                   shell=False, stdout=subprocess.PIPE, check=False)
        DE_RESULT = DE_RESULT.stdout.decode('utf-8')
        DE_RESULT = DE_RESULT.replace('\n', '')
    else:
        DE_RESULT = "try another method for DE."

print(OKGREEN + "\tDE: " + ENDC + DE_RESULT)

print(OKGREEN + "\tKernel: " + ENDC + platform.release())
print(OKGREEN + "\tPlatform: " + ENDC + platform.platform())

print(OKBLUE + "\t---- hardware -------" + ENDC)

PATH = '/sys/devices/virtual/dmi/id/product_name'        # works with Mint
check_file = os.path.isfile(PATH)
if check_file:
    with open(PATH, "r", encoding="utf8") as f:
        producthost = f.read()
    producthost = producthost.replace('\n', '')
    with open('/sys/devices/virtual/dmi/id/sys_vendor', "r", encoding="utf8") as f:
        productvnd = f.read()
    productvnd = productvnd.replace('\n', '')
    print(OKGREEN + "\tComputer vendor: " + ENDC + productvnd + " " + producthost)
else:
    DE_RESULT = "try another method for vendor."

DE_RESULT = subprocess.run(['cat /proc/cpuinfo'], stdout=subprocess.PIPE, shell=True, check=False)
DE_RESULT = DE_RESULT.stdout.decode('utf-8')
DE_RESULT = DE_RESULT.replace('\n', '')
DE_RESULT = DE_RESULT.replace('\t', '')
xstart = DE_RESULT.find("model name") + 12
xstop = DE_RESULT.find("stepping")
xstart2 = DE_RESULT.find("siblings") + 10
xstop2 = DE_RESULT.find("core id")
print(OKGREEN + "\tCPU: " + ENDC + DE_RESULT[xstart:xstop] + " ("
      + DE_RESULT[xstart2:xstop2] + " cores)")

DE_RESULT = subprocess.run(['grep MemTotal /proc/meminfo'], stdout=subprocess.PIPE,
                           shell=True, check=False)
DE_RESULT = DE_RESULT.stdout.decode('utf-8')
DE_RESULT = DE_RESULT.replace('MemTotal:       ', '')
DE_RESULT = DE_RESULT.replace(' kB', '')
DE_RESULT = f'{int(DE_RESULT):,}'
print(OKGREEN + "\tRAM: " + ENDC + DE_RESULT + ' kB')

DE_RESULT = subprocess.run(['lspci | grep \'HD Graph\''], stdout=subprocess.PIPE,
                           shell=True, check=False)
DE_RESULT = DE_RESULT.stdout.decode('utf-8')
DE_RESULT = DE_RESULT.replace('VGA compatible controller: ', '')
print(OKGREEN + "\tGraphics: " + ENDC + DE_RESULT[8:])

print(OKBLUE + "\t---- internet -------" + ENDC)

print(OKGREEN + "\tNetwork Host Name: " + ENDC + socket.gethostname())

# IP info
myip = socket.gethostbyaddr(socket.gethostname())[2]
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
internalIP = s.getsockname()[0]
s.close()

# externalIP4  = os.popen('curl -s v4.ident.me').readline()  # slower
externalIP4 = os.popen('curl -s ifconfig.me').readline()   # faster
# externalIP6  = os.popen('curl -s v6.ident.me').readline()    # slower
externalIP6 = os.popen('curl -s icanhazip.com').readline()    # faster
print(OKGREEN + "\tInternal eth0 IP: " + ENDC + internalIP)
print(OKGREEN + "\tInternal lo IP: " + ENDC + " ".join(myip))
print(OKGREEN + "\tExternal v4 IP: " + ENDC + externalIP4)
print(OKGREEN + "\tExternal v6 IP: " + ENDC + externalIP6)

print(OKBLUE + "\t---- apps -------" + ENDC)
DE_RESULT = subprocess.run(['bash', '--version'], stdout=subprocess.PIPE, check=False)
DE_RESULT = DE_RESULT.stdout.decode('utf-8')
DE_RESULT = DE_RESULT.replace('\n', '')
xstop = DE_RESULT.find("Copyright")
print(OKGREEN + "\tShell: " + ENDC, DE_RESULT[:xstop])

DE_RESULT = subprocess.run(['python3', '--version'], stdout=subprocess.PIPE, check=False)
DE_RESULT = DE_RESULT.stdout.decode('utf-8')
DE_RESULT = DE_RESULT.replace('\n', '')
print(OKGREEN + "\tpython3: " + ENDC, DE_RESULT)

print(OKBLUE + "\t---- libs -------" + ENDC)
DE_RESULT = subprocess.run(['dpkg -l libgtk-*-common | grep -e \'^i\' | grep -e \'libgtk-*[3-6]\''],
                           stdout=subprocess.PIPE, shell=True, check=False)
DE_RESULT = DE_RESULT.stdout.decode('utf-8')
DE_RESULT = DE_RESULT.replace('ii  ', '')
print(OKGREEN + "\tGTK:" + ENDC + "\n" + DE_RESULT)
DE_RESULT = subprocess.run(['dpkg -l qt5* | grep -e \'^i\''], stdout=subprocess.PIPE,
                           shell=True, check=False)
DE_RESULT = DE_RESULT.stdout.decode('utf-8')
DE_RESULT = DE_RESULT.replace('ii  ', '')
print(OKGREEN + "\tQT:" + ENDC + "\n" + DE_RESULT)
