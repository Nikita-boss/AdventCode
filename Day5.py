import os
import collections
from typing import List

cur_dir = os.getcwd()
path = cur_dir + '/AdventCode/input5'

def read_file(path):
    isMove = False
    move, from_crate, to_crate = [], [], []
    cranes = collections.defaultdict(collections.deque)

    with open(path, 'r') as file:
        for f in file:
            f = f.rstrip('\n')
            if not f:
                isMove = True
                continue

            if isMove:
                l = f.split(' ')
                move.append(int(l[1]))
                from_crate.append(int(l[3]))
                to_crate.append(int(l[5]))
            else:
                if f[1] == '1': continue
                counter = 1
                for c in range(1, len(f), 4):
                    if f[c].strip():
                        cranes[counter].append(f[c])
                    counter += 1

    return cranes, move, from_crate, to_crate


def complete_move(cranes: collections.defaultdict(collections.deque), move: List[int], from_crate: List[int], to_crate: List[int]) -> int:
    for i in range(len(move)):
        for j in range(move[i]):
            tmp = cranes[from_crate[i]].popleft()
            cranes[to_crate[i]].appendleft(tmp)
    return 1

def complete_move_2(cranes: collections.defaultdict(collections.deque), move: List[int], from_crate: List[int], to_crate: List[int]) -> int:
    for i in range(len(move)):
        cranes[to_crate[i]].extendleft(reversed([cranes[from_crate[i]].popleft() for _ in range(move[i])]))
    return 1

if __name__ == '__main__':
    cranes, move, from_crate, to_crate = read_file(path)
    #complete_move(cranes, move, from_crate, to_crate)
    complete_move_2(cranes, move, from_crate, to_crate)

    res = ''
    for i in range(1, len(cranes) + 1):
        res += cranes[i].popleft()

    print(res)
