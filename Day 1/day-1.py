
with open('input.txt') as f:
    lines = f.readlines()
    f.close()

dict = {} 

index = 1

temp = []

for i in lines:
    if i == '\n':
        dict[index] = sum(temp)
        index = index + 1
        temp = []
    else:
        temp.append(int(i.strip()))

print("index order dict = ",dict)

res = {key: val for key, val in sorted(dict.items(), key = lambda ele: ele[1], reverse = True)}

print('sorted dict = ',res)