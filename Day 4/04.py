import sys

# A B
# C D

def compare(a,b,c,d):

    if c >= a and c <= b:
        if d >= a and d <= b:
            return col1,col2,'1'

    if a >= c and a <= d:
        if b >= c and b >= d:
            return col1,col2,'2'


    

with open(sys.argv[1]) as f:
    lines = f.readlines()
    lines = [i.strip() for i in lines]
    f.close()
# print(lines)

# list = lines()

total = []
for i in lines:
    two_col = i.split(',') # gives ['2-4', '6-8']

    col1 = two_col[0].split('-') # gives ['2', '4']
    col2 = two_col[1].split('-') # gives ['6', '8']

    answer = compare(col1[0],col1[1],col2[0],col2[1])
    if answer:
        total.append(answer)

for i in total:
    print(i)
# print(len(total))