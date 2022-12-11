import os
import numpy as np
from typing import List, Union, Dict


def read_file(path: str) -> Union[List[List[int]], List[int], List[int]]:
    data = []
    row = 0
    row_maximum = {}
    column_maximum = {}
    with open(path, 'r') as file:
        for f in file:
            f = f.strip('\n')
            tmp = []
            for c in f:
                tmp.append(int(c))
            tmp = np.array(tmp)
            data.append(tmp)
            row_maximum[row] = max(tmp)
            row += 1

    data = np.array(data)
    for i in range(len(data[0])):
        column_maximum[i] = max(data[:, i])
    
    return data, row_maximum, column_maximum

def find_visible(data: List[List[int]]) -> int:
    counter = 0
    rows = len(data)
    columns = len(data[0])

    for row in range(rows):
        for column in range(columns):
            # On the edge
            if row == 0 or column == 0 or row == rows - 1 or column == columns - 1:
                counter += 1
            else:
                height = data[row][column]
                if height > max(data[0:row, column]):
                    counter += 1
                elif height > max(data[row + 1:, column]):
                    counter += 1
                elif height > max(data[row, 0:column]):
                    counter += 1
                elif height > max(data[row, column + 1:]):
                    counter += 1
            
    return counter 

def find_distance(data: List[List[int]]) -> int:
    rows = len(data)
    columns = len(data[0])
    distances = []

    for row in range(rows):
        tmp = []
        for column in range(columns):
            # On the edge
            if row == 0 or column == 0 or row == rows - 1 or column == columns - 1:
                tmp.append(0)
            else:
                height = data[row][column]
                top = row - 1
                top_distance = 0
                while top >= 0:
                    if height > data[top][column]:
                        top_distance += 1
                        top -= 1
                    else:
                        top_distance += 1
                        break

                bottom = row + 1
                bottom_distance = 0
                while bottom < rows:
                    if height > data[bottom][column]:
                        bottom_distance += 1
                        bottom += 1
                    else:
                        bottom_distance += 1
                        break

                left = column - 1
                left_distance = 0
                while left >= 0:
                    if height > data[row][left]:
                        left_distance += 1
                        left -= 1
                    else:
                        left_distance += 1
                        break

                right = column + 1
                right_distance = 0
                while right < columns:
                    if height > data[row][right]:
                        right_distance += 1
                        right += 1
                    else:
                        right_distance += 1
                        break

                tmp.append(top_distance * bottom_distance * left_distance * right_distance)


        distances.append(tmp)

    return max([max(i) for i in distances])

if __name__ == '__main__':
    cur_dir = os.getcwd()
    path = cur_dir + '/AdventCode/input8.txt'
    data, row_max, col_max = read_file(path)

    # Part 1 
    visible = find_visible(data)
    print(visible)

    # Part 2
    distance = find_distance(data)
    print(distance)

