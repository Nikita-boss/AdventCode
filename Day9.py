import os
from typing import List

def read_file(path: str) -> List[tuple]:
    data = []

    with open(path, 'r') as file:
        for f in file:
            f = f.rstrip('\n').split(' ')
            data.append((f[0], int(f[1])))

    return data


def motions(data: List[tuple]) -> int:
    # x, y moves
    direction_move = {'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)}
    cur_head_pos = (0, 0)
    cur_tail_pos = (0, 0)
    tail_pos = set([cur_tail_pos])

    for cur_move in data:
        for _ in range(cur_move[1]):
            head_x_new = cur_head_pos[0] + direction_move[cur_move[0]][0]
            head_y_new = cur_head_pos[1] + direction_move[cur_move[0]][1]
            
            # Check if tail is not touching head but not diagonally
            # Same x position
            if (cur_tail_pos[0] == head_x_new and abs(cur_tail_pos[1] - head_y_new) == 2):
                cur_tail_pos = (cur_tail_pos[0], cur_tail_pos[1] + direction_move[cur_move[0]][1])
            # Same y position
            elif (cur_tail_pos[1] == head_y_new and abs(cur_tail_pos[0] - head_x_new) == 2):
                cur_tail_pos = (cur_tail_pos[0] + direction_move[cur_move[0]][0], cur_tail_pos[1])
            # Check if tail is not touching head diagonally
            elif (abs(cur_tail_pos[0] - head_x_new) == 1 and abs(cur_tail_pos[1] - head_y_new) == 2) or \
                (abs(cur_tail_pos[1] - head_y_new) == 1 and abs(cur_tail_pos[0] - head_x_new) == 2):
                cur_tail_pos = cur_head_pos

            # Update head position
            cur_head_pos = (head_x_new, head_y_new)
            # Add tail position
            tail_pos.add(cur_tail_pos)

    return len(tail_pos)


def motions_chain(data: List[tuple]) -> int:
    # x, y moves
    direction_move = {'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)}
    cur_head_pos = (0, 0)
    cur_tail_pos = [(0, 0) for _ in range(9)]
    tail_pos = set([(0, 0)])

    def move(head: tuple, cur_move: tuple, tail: tuple) -> tuple:      
        head_x_new, head_y_new = head[0], head[1]
        # Check if tail is not touching head but not diagonally
        # Same x position
        if (tail[0] == head_x_new and abs(tail[1] - head_y_new) == 2):
            tail = (tail[0], tail[1] + 1) if head_y_new > tail[1] else (tail[0], tail[1] - 1)
        # Same y position
        elif (tail[1] == head_y_new and abs(tail[0] - head_x_new) == 2):
            tail = (tail[0] + 1, tail[1]) if head_x_new > tail[0] else (tail[0] - 1, tail[1])
        # Check if tail is not touching head diagonally
        elif (abs(tail[0] - head_x_new) == 1 and abs(tail[1] - head_y_new) == 2):
            tail = (head_x_new, tail[1] + 1) if head_y_new > tail[1] else (head_x_new, tail[1] - 1)
        elif (abs(tail[1] - head_y_new) == 1 and abs(tail[0] - head_x_new) == 2):
            tail = (tail[0] + 1, head_y_new) if head_x_new > tail[0] else (tail[0] - 1, head_y_new)
        # Check if the tail is both two cells away horizontally and vertically from head
        elif (abs(tail[0] - head_x_new) == 2 and abs(tail[1] - head_y_new) == 2):
            x_tmp = head_x_new - 1 if head_x_new > tail[0] else head_x_new + 1
            y_tmp = head_y_new - 1 if head_y_new > tail[1] else head_y_new + 1
            tail = (x_tmp, y_tmp)
        
        return tail


    for cur_move in data:
        for _ in range(cur_move[1]):
            head_x_new = cur_head_pos[0] + direction_move[cur_move[0]][0]
            head_y_new = cur_head_pos[1] + direction_move[cur_move[0]][1]
            
            for i in range(len(cur_tail_pos)):
                if i == 0:
                    tmp_pos = move((head_x_new, head_y_new), cur_move, cur_tail_pos[0])
                    cur_tail_pos[i] = tmp_pos
                else:
                    tmp_pos = move(cur_tail_pos[i - 1], cur_move, cur_tail_pos[i])
                    cur_tail_pos[i] = tmp_pos

            # Update head position
            cur_head_pos = (head_x_new, head_y_new)
            # Add tail position
            tail_pos.add(cur_tail_pos[-1])

    return len(tail_pos)


if __name__ == '__main__':
    cur_dir = os.getcwd()
    path = cur_dir + '/AdventCode/input9.txt'
    data = read_file(path)
    cells = motions(data)
    print(cells)
    cells = motions_chain(data)
    print(cells)
