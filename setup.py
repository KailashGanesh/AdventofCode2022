#!/usr/bin/env python3

import sys
import shutil
import os


current_working_dir = os.getcwd()

target_dir = current_working_dir + f'/Day{sys.argv[1]}'

print(target_dir)

if os.path.exists(target_dir):
    print('getting input')

    # TODO see if input.txt already exist, ask if they want to get it again
else:
    print('making dir + getting input')
    os.mkdir(target_dir) # make a dir using user input
    shutil.copyfile('./template.py', target_dir + f'/{sys.argv[1]}.py')
