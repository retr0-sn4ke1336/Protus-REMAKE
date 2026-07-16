"""Protus - Programmable Recon & Offensive Toolkit for Unified Systems.

Main entry point for the Protus framework.
Developed by RetroGuy1336
"""

from banners import random_banners
import shlex
from intermediate import intermediateFile
import os

# Color codes for terminal output
RED = '\033[1;31m'
BLUE = '\033[1;34m'
RESET = '\033[m'


def ProtusMain():
    """Main application loop for Protus framework."""
    os.system('clear')
    
    # Check for sudo privileges
    if os.geteuid() != 0:
        print("Execute with sudo!")
        exit()
    
    while True:
        print(RED)
        random_banners()
        print(RESET)
        
        print("""
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
[ + ]     --[   Protus, Programmable Recon & Offensive Toolkit for Unified Systems   ]
[ + ] --  -=[   We have only a Port Scanner and a DNS Lookup for attacks D:          ]
[ + ] -  --=[   -- - --- - ---Developed by RetroGuy1336-  --- -- - -- -              ]""")
        
        user = input(BLUE + "PTS >> " + RESET)
        args = shlex.split(user)

        if user == "exit":
            break

        else:
            intermediateFile(args)
            
if __name__ == "__main__":
    ProtusMain()