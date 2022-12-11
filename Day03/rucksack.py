priorty = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def sum_of_priorities():
    common_letters = []
    for i in lines:
        i_striped = i.strip()

        first_comp = i_striped[0:int(len(i_striped)/2)]
        secound_comp = i_striped[int(
            len(i_striped)/2): int(len(i_striped)/2) + int(len(i_striped)/2)]

        for i in set(first_comp):
            if i in set(secound_comp):

                lc_score = priorty.index(i.lower()) + 1

                if i == i.upper():
                    lc_score = lc_score + 26
                print('i & lc = ', i, lc_score)
                common_letters.append(lc_score)
    print(sum(common_letters))


def compare_3_lines():
    lines_striped = [i.strip() for i in lines]
    common_letters = []

    for i in range(len(lines_striped) + 1):
        three_lines = lines_striped[3*i:3*i+3]

        if three_lines:
            # for j in set(three_lines[0]):
            #     if j in set(three_lines[1]):
            #         if j in set(three_lines[2]):

            # Found a easier way to do this:
            for j in set(three_lines[0]) & set(three_lines[1]) & set(three_lines[2]):
                lc_score = priorty.index(j.lower()) + 1

                if j == j.upper():
                    lc_score = lc_score + 26
                common_letters.append(lc_score)
    print(sum(common_letters))


file = 'input.txt'

with open(file) as f:
    lines = f.readlines()
    f.close()

# sum_of_priorities()

compare_3_lines()
