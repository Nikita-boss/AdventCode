import os
from collections import deque
from typing import List
from math import inf 

def read_file(path):
    data = []
    row = 0
    with open(path, 'r') as file:
        for f in file:
            f = f.rstrip('\n')
            tmp = []
            for j, i in enumerate(f):
                if i == 'S':
                    start = (row, j)
                    i = 'a'
                if i == 'E':
                    end = (row, j)
                    i = 'z'
                tmp.append(i)
            data.append(tmp)
            row += 1

    return data, start, end


def find_path(data: List[List[str]], start: tuple, end: tuple) -> int:
    queue = deque([(start, 0)])
    n, m = len(data), len(data[0])
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    seen = {start}

    while queue:
        cur_pos, steps = queue.popleft()
        row, col = cur_pos[0], cur_pos[1]
        #print(row, col, steps)
        if row == end[0] and col == end[1]:
            return steps

        for x,y in directions:
            new_row, new_col = row + x, col + y
            if 0 <= new_row < n and 0 <= new_col < m  \
                and (new_row, new_col) not in seen \
                and ord(data[new_row][new_col]) - 1 <= ord(data[row][col]):
                queue.append(((new_row, new_col), steps + 1))
                seen.add((new_row, new_col))
    return inf


if __name__ == '__main__':
    cur_dir = os.getcwd()
    path = cur_dir + '/AdventCode/input12.txt'
    data, start, end = read_file(path)
    # Part 1
    shortest_path = find_path(data, start, end)
    print(shortest_path)
    # Part 2
    all_paths = []
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == 'a':
                all_paths.append(find_path(data, (i, j), end))
    print(min(all_paths))

