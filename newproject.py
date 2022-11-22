# imports
import os
from colorama import Fore, init, Style, Back
import time
import sys
import socket
import platform

# os
os.system('title AMIGOS')
os.system('color 0')

# get the hostname & ip-adress
hostname=socket.gethostname()
ip=socket.gethostbyname(hostname)

system = platform.system()

# normal colors
red = Fore.RED
black = Fore.BLACK
white = Fore.WHITE
green = Fore.GREEN
cyan = Fore.CYAN
yellow = Fore.YELLOW
magenta = Fore.MAGENTA
blue = Fore.BLUE
reset = Fore.RESET

# light colors
lred = Fore.LIGHTRED_EX
lblack = Fore.LIGHTBLACK_EX
lwhite = Fore.LIGHTWHITE_EX
lgreen = Fore.LIGHTGREEN_EX
lcyan = Fore.LIGHTCYAN_EX
lmagenta = Fore.LIGHTMAGENTA_EX
lyellow = Fore.LIGHTYELLOW_EX
lblue = Fore.LIGHTBLUE_EX

# back of text colors
bred = Back.RED
bblack = Back.BLACK
bwhite = Back.WHITE
bgreen = Back.GREEN
bcyan = Back.CYAN
byellow = Back.YELLOW
bmagenta = Back.MAGENTA
bblue = Back.BLUE
breset = Back.RESET

# light back of text colors
blred = Back.LIGHTRED_EX
bblack = Back.LIGHTBLACK_EX
blwhite = Back.LIGHTWHITE_EX
blgreen = Back.LIGHTGREEN_EX
blcyan = Back.LIGHTCYAN_EX
blyellow = Back.LIGHTYELLOW_EX
blmagenta = Back.LIGHTMAGENTA_EX
blblue = Back.LIGHTBLUE_EX



# banner
banner = rf"""
{yellow}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀
{yellow}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⡟⠋⠉⠙⠻⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
{yellow}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⣼⡟⣀⣠⣤⣤⣴⣾⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
{yellow}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡿⣿⣿⣿⡟⠻⣿⣿⠇⠙⢷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀      {green}█████  ███    ███ {white}██  ██████   {red}██████  ███████
{yellow}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣟⢀⣹⣿⣿⣤⣤⠾⠿⠶⠟⠛⠻⣆⠀⠀⠀⢀⣀⣀⣀⣀⣀⡀          {green}██   ██ ████  ████ {white}██ ██       {red}██    ██ ██
{yellow}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠛⠛⠉⠉⠀⠀⠀⠀⠀⠀⠀⣀⣀⣽⡿⣿⣟⠛⠉⠉⠉⠉⣙⣿⡆⠀⠀⠀⠀     {green}███████ ██ ████ ██ {white}██ ██   ███ {red}██    ██ ███████
{yellow}⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣤⣴⣿⣴⣦⣤⣤⣤⣤⣤⣶⣶⠶⠞⢻⣿⠏⠀⣈⣻⣦⣤⣴⠶⠛⣿⣿⡇         {green}██   ██ ██  ██  ██ {white}██ ██    ██ {red}██    ██      ██
{yellow}⠀⠀⠀⠀⢀⣴⠾⠛⠋⠉⠉⠀⠀⢀⣼⠟⠁⠈⠻⣯⣉⣁⣀⣠⣤⣶⣶⠿⣿⣿⣛⠉⠉⣹⠏⠻⢦⣾⣇⡿⠁⠀        {green}██   ██ ██      ██ {white}██  ██████   {red}██████  ███████
{yellow}⠀⠀⠀⠀⠸⣿⠷⣶⣦⠤⠶⠴⣶⣾⠿⠾⠿⣿⢿⣟⡛⠛⢋⣿⠻⣦⣀⣴⡟⠀⠙⠳⠾⠋⠀⢀⣠⡼⠟
{yellow}⠀⠀⠀⠀⠀⠻⣶⣟⠙⢷⣤⡾⠋⠙⢷⣤⡾⠋⠀⠉⠛⠶⠟⠁⠀⠈⠙⠋⠀⢀⣀⣠⣤⣶⡶⠟⠻⠁⠀⠀⠀                         {lblue} Made by: {blue}Mischa
{yellow}⠀⠀⠀⠀⠀⠀⠈⠉⠓⠶⠿⢤⣤⣤⣤⣭⣤⣤⣤⣤⣶⣶⣶⣶⠶⠶⠾⠿⠛⠛⠉                                   {lblue} Discord: {blue}miesja#6969
{reset}



{lred}Welcome to AMIGOS! Type {white}help {lred}for a list of commands!
"""

# progressbar
def progressbar(it, prefix="", size=60, out=sys.stdout):
    count = len(it)
    def show(j):
        x = int(size*j/count)
        print("{}[{}{}] {}/{}".format(prefix, "█"*x, " "*(size-x), j, count), 
                end='\r', file=out, flush=True)
    show(0)
    for i, item in enumerate(it):
        yield item
        show(i+1)
    print("\n", flush=True, file=out)


# help
help = rf"""
{lred}     ╔══════════════════════════════════╦═══════════════════════════════════════╗
{lred}     ║            Commands              ║             Description               ║
{lred}     ║                                  ║                                       ║
{lred}     ║  ► Info                          ║        Sends info about you           ║
{lred}     ╚══════════════════════════════════╩═══════════════════════════════════════╝


Type {lwhite}back{lred} to go back!
"""

# pc & network info
info = rf"""
                                                {bred} NETWORK AND COMPUTER INFORMATION{breset}


{green} IP-Adress: {ip}
{lgreen} Pc Name: {hostname}
{green} System: {system}
{lgreen}
"""




# startup
for i in progressbar(range(100), rf"""{red}Starting: """, 50):
    time.sleep(0.01)
os.system('cls')

print(banner)


# commands & prompt
while True:
    command = input(rf"""{cyan}root@windows:~/{green}AM{lwhite}IG{red}OS{cyan}# »{reset} """)
    if command == "help":
        os.system('cls')
        print(help)
    elif command == "info":
        os.system('cls')
        print(info)
    elif command == "back":
        os.system('cls')
        print(banner)
    else:
        print(rf"""{red} !{yellow} Unknown Command{reset}""")