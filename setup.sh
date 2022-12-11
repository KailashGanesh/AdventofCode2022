#!/bin/bash
set -e
# loads the cookie string into variable
cookie=$(< cookie.txt)

# removes leading zero for numbers
n=$(($1 + 0))

# downloads the input.txt & makes dir if it doesn't exist already
curl -b session="$cookie" https://adventofcode.com/2022/day/$n/input --create-dirs -o Day$1/input.txt

if test -f "Day$1/$1.py"; then
    echo "$1.py already exists. skipping copying"
else
    echo "copying template.py..."
    cp template.py Day$1/$1.py
fi
