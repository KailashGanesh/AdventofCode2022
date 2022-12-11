import sys

# A B
# C D

def overlap_fully(a,b,c,d):

    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)

    # print(max(a,c))
    # print(min(b,d))
    # print(max(a,c) - min(b,d) + 1)

    if a >= c and b <= d:
        return a,b,c,d,'new'
    elif c >= a and d <= b:
        return a,b,c,d,'new2'
    
    # so it turns out I was right all along, I just did't convert the string into ints T_T

    # if c >= a and c <= b:
    #     if d >= a and d <= b:
    #         return col1,col2,'1'

    # if a >= c and a <= d:
    #     if b >= c and b >= d:
    #         return col1,col2,'2'

def overlap_at_all(a,b,c,d):
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)

    if a <= c and c <= b:
        return a,b,c,d,'1'
    elif c <= b and d >= a:
        return a,b,c,d,'2'

    

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

    # answer = overlap_fully(col1[0],col1[1],col2[0],col2[1])
    answer = overlap_at_all(col1[0],col1[1],col2[0],col2[1])
    if answer:
        total.append(answer)

for i in total:
    print(i)
print(len(total))