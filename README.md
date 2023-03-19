# pyfetch
A small, terminal based, module for learning Python, and posting information about my system. Similar to neofetch, but it prints info I need.

I've tested it on my Linux Mint computer, and it works with python3. There's no error checking, so it will probably crash in other distros (good learning experience). I just wrote it to learn about Python on my computer.
My next version will be GUI.

run it like this: python3 pyfetch.py

or make it executable: chmod +x pyfetch.py and then run it like this: ./pyfetch.py
even better: echo $PATH
and then copy the file somewhere in the path, maybe /usr/bin
and then rename it to "pyfetch" - and now it will run from anywhere as "pyfetch".

Here's a sample of what it displays:  
  **---- software -------**  
  OS: Linux Mint 21.1 Vera x86_64  
  DE: Cinnamon 5.6.7  
  Kernel: 5.15.0-67-generic  
  Platform: Linux-5.15.0-67-generic-x86_64-with-glibc2.35  
  **---- hardware -------**  
  Computer vendor: Dell Inc. OptiPlex 7050  
  CPU: Intel(R) Core(TM) i7-6700 CPU @ 3.40GHz (8 cores)  
  **---- internet -------**  
  Network Host Name: i7  
  Internal eth0 IP: 10.0.0.1  
  Internal lo IP:  127.0.1.1  
  External v4 IP: xx.xx.xx.xx  
  External v6 IP: yyyy.yyyy.....  
