#!/usr/bin/env python3

import sys

def printl(list):
    for i in list:
        print(i)

with open(sys.argv[1]) as f:
    lines = f.readlines()
    lines = [i.strip() for i in lines]
    f.close()