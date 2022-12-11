col1 = {
    'A':"rock",
    'B':"paper",
    'C':"scissors",
}

col2 = {
    'X':"rock",
    'Y':"paper",
    'Z':"scissors",
}

shape_score = {
    'rock':1,
    'paper':2,
    'scissors':3
}

win_score = {
    0:0,
    'Draw':3,
    1:6
}

part_two_col_2 = {
    'X':0,
    'Y':'Draw',
    'Z':1
}


# paper > rock > scissors > paper

def who_won(playerA, playerB):
    key_wins = {
        'paper':'rock',
        'scissors':'paper',
        'rock':'scissors',
    }

    if playerA == playerB:
        return 'Draw'
    elif key_wins[playerA] == playerB:
        return 0
    elif key_wins[playerB] == playerA:
        return 1

def return_key_from_value(dict, value):
    for i in dict:
        if dict[i] == value:
            return i
# print(who_won(col1['A'],col2['Y']))

def part_one():
    score_for_each_round = []
    for i in lines:
        array = i.strip().split(' ')
        shape = shape_score[col2[array[1]]] # gets the shape score
        result = who_won(col1[array[0]],col2[array[1]])
        win = win_score[result] # gets the win score

        this_round_score = shape + win

        score_for_each_round.append(this_round_score)
        
    print(score_for_each_round)
    print(sum(score_for_each_round))

new_file = []
def part_two():
    for i in lines:
        array = i.strip().split(' ')
        player_1_move = col1[array[0]]
        outcome = part_two_col_2[array[1]]

        our_move = ''
        for j in ['rock','paper','scissors']:
            if outcome == who_won(col1[array[0]], j):
                our_move = return_key_from_value(col2,j)
                break
        
        new_line = f'{array[0]} {our_move}'
        new_file.append(new_line)
    for i in new_file:
        print(i)

# file = 'input.txt'
file = 'part_2.txt'

with open(file) as f:
    lines = f.readlines()
    f.close()

part_one()
# part_two()