#!/usr/bin/env python3

import sys

def printl(list):
    for i in list:
        print(i)

with open(sys.argv[1]) as f:
    lines = f.readlines()
    lines = [i.strip() for i in lines]
    f.close()

# how_many_letters = 4
how_many_letters = 14

for line in lines:
    letters = ''
    count = ''
    no = 0
    for letter in line:
        letters += letter
        if len(letters) == how_many_letters:
            no += 1
            if len(set(letters)) == how_many_letters:
                print('yay!',letters)
                print((line,no + 3))
            else:
                count += letter[0]
                letters = letters[1:None]
                # print('count',count)
    # print((line,no + 3))

# it seems like I need to add 10 to the answers