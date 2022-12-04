import os
cur_dir = os.getcwd()
path = cur_dir + '/AdventCode/input2.txt'

# 1
play = {'X':'A', 'Y':'B', 'Z':'C'}
score = {'A':1, 'B':2, 'C':3}

with open(path, 'r') as file:
    total_score = 0
    for f in file:
        opponent = f[0]
        strategy = play[f[2]]
        total_score += score[strategy]
        if opponent == strategy:
            total_score += 3
        elif opponent == 'A' and strategy == 'C':
            continue
        elif opponent < strategy or (opponent == 'C' and strategy == 'A'):
            total_score += 6
        
print(total_score)

# 2
#  X - lose, Y - draw, Z - win
win = {'A':'B', 'B':'C', 'C':'A'}
loss = {'A':'C', 'B':'A', 'C':'B'}
with open(path, 'r') as file:
    total_score = 0
    for f in file:
        opponent = f[0]
        if f[2] == 'Z':
            choice = win[opponent]
            total_score += score[choice] + 6
        elif f[2] == 'Y':
            total_score += score[opponent] + 3
        else:
            choice = loss[opponent]
            total_score += score[choice]
        
print(total_score)
