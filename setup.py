#!/usr/bin/env python3

import sys
import shutil
import os
import requests


def colored(st, color): print(f"\u001b[{30+['black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white'].index(color)}m{st}\u001b[0m")  # replace the termcolor library with one line

def get_input(url, cookie, target_dir):
    response = requests.get(url, cookies=dict(session=cookie),allow_redirects=True)
    if response.status_code == 200:
        with open(target_dir + '/input.txt', 'wb') as f:
            for chunk in response:
                f.write(chunk)
        colored('Finished','green')
    else:
        colored(f'Failed! {response.status_code}','red')

current_working_dir = os.getcwd()

target_dir = current_working_dir + f'/Day{sys.argv[1]}'

url = f"https://adventofcode.com/2022/day/{int(sys.argv[1])}/input"

with open('cookie.txt') as f:
    cookie = f.readlines()
    cookie = [i.strip() for i in cookie]
    f.close()

if os.path.exists(target_dir):
    colored('getting input','cyan')
    get_input(url, cookie[0],target_dir)
else:
    colored('making dir + getting input','cyan')

    os.mkdir(target_dir) # make a dir using user input
    shutil.copyfile('./template.py', target_dir + f'/{sys.argv[1]}.py') # copying over template.py with new file name
    get_input(url, cookie[0],target_dir)