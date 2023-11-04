#!/usr/bin/python
from os import system
from sys import platform

purple = '\033[95m'
blue = '\033[94m'
cyan = '\033[96m'
green = '\033[92m'
yellow = '\033[93m'
red = '\033[91m'
end = '\033[0m'
bold = '\033[1m'
u = '\033[4m'

if platform == 'win32':
    system('color')

from random import choice
x = '''
        /\\
        \\ \\
       \\ \\ \\
      \\ \\ \\
    /  \\ \\  /
   / /  \\/ / /
  / / /\\  / / /\\
  \\/ / /  \\/ / /
    / / /\\  / /
     /  \\ \\  /
       \\ \\ \\    # Coded by Zeerx7 @ XploitSec-ID
      \\ \\ \\     # zeerx7@gmail.com
       \\ \\      # Last updated: 02-03-2023
        \\/      # Version 2.2

    { Laravel Environment Scanner + PHPUnit Rce }
'''
logo_color = choice([red, blue, cyan, purple, yellow])
banner = x.replace('/', logo_color+'/').replace('\\',logo_color+'\\').replace('#', green+'#').replace('{',cyan+'{')
