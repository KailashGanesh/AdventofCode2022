#!/usr/bin/env python3

import sys

def printl(list):
    for i in list:
        print(i)

def find_len_of_lists(lines):
    for i in lines:
        if '1' in i:
            answer =  i.split(' ')
            return max(answer)

with open(sys.argv[1]) as f:
    lines = f.readlines()
    # lines = [i.strip() for i in lines]
    f.close()



len_of_list = find_len_of_lists(lines)

count_before = 0
count_after = 0
pos = 0

dict = {}

for i in range(1,int(len_of_list)+1):
    dict[str(i)] = []


for j in lines:
    # j = j.strip()
    count_before = 0
    # count_after = 0
    # print('j',j)
    if '1' not in j:
        # print(j)
        line1 = [i for i in j.split(' ')]
        # print('line1',line1)
        for i in line1:

            if i == '':
                count_before += 1
            elif i != '' and i != '\n':
                index = (count_before / 4) + 1
                # print(count_before,index, i)
                # if index != 0:
                #     index += 1

                dict[str(round(index))].append(i)
                pos += 1
                count_after = count_before

            if count_after == count_before:
                count_before = count_before + 4
                # dict[str(round(index))].append(i)
    else: 
        break



for key in dict:
    dict[key].reverse()
    dict[key] = [k.strip() for k in dict[key]]
    print(key, dict[key])


instructions = [i.strip() for i in lines[lines.index('\n')+1:len(lines)]]

def part_one():
    for i in instructions:
        # this is answer to the first part
        new_line = i.split(' ')

        no_of = new_line[1]
        from_list = new_line[3]
        to_list = new_line[5]

        # print(no_of,from_list,to_list)

        for l in range(int(no_of)):
            dict[to_list].append(dict[from_list].pop())

def part_two():
    for i in instructions:

        new_line = i.split(' ')

        no_of = new_line[1]
        from_list = new_line[3]
        to_list = new_line[5]

        # print(no_of,from_list,to_list)
        things = dict[from_list][len(dict[from_list]) - int(no_of):None]
        for x in things:
            '''
            we gotta reverse the list so the items we want to remove
            are in the start, otherwise .remove() will remove items we
            want to keep but come first in the list
            '''
            dict[from_list].reverse()
            dict[from_list].remove(x)
            dict[from_list].reverse()

            # dict[from_list] = dict[from_list][0:len(dict[from_list]) - int(no_of)]
            dict[to_list].append(x)


part_two()

print('--------')
for key in dict:
    print(key, dict[key])

final = ''
for key in dict:
    final += dict[key][-1].strip('[').strip(']')
print(final)

# counts the number of letters
no_letters = 0
for key in dict:
    no_letters += len(dict[key])
print(no_letters)


#first answer = TGWSMRBPN
# secound anser = TZLTLWRNF

# secound not answer ZCMJLZBNP