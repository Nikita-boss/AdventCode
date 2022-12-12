import os
from typing import List

def read_file(path: str) -> List[tuple]:
    data = []

    with open(path, 'r') as file:
        for f in file:
            f = f.rstrip('\n').split(' ')
            if len(f) == 2:
                data.append((f[0], int(f[1])))
            else: 
                data.append((f[0], 0))

    return data


def find_strength(data: List[tuple]) -> int:
    # Find the signal strength during the 20th, 60th, 100th, 140th, 180th, and 220th cycles
    cycles = [220, 180, 140, 100, 60, 20]
    strength = 0
    cur_cycle = 0
    register = 1
    for i in data:
        if i[0] == 'noop':
            cur_cycle += 1
        else:
            cur_cycle += 2
            register += i[1]

        if cur_cycle >= cycles[-1]:
            strength += cycles.pop() * (register - i[1])

        if len(cycles) == 0:
           break

    return strength


def find_string(data: List[tuple]) -> str:
    res = []
    def draw(res: List[int], cur_crt: int, position: set, steps: int):
        for _ in range(steps):
            if cur_crt in position:
                res.append('#')
            else:
                res.append('.')
            cur_crt += 1

        return cur_crt

    register = 1
    position = {register - 1, register, register + 1}
    cur_crt = 0
    for i in data:
        if i[0] == 'noop':
            if cur_crt + 1 > 40:
                cur_crt = 0
                res.append('\n')
            cur_crt = draw(res, cur_crt, position, 1)
        else:
            if cur_crt + 2 > 41:
                cur_crt = 0
                res.append('\n')
                cur_crt = draw(res, cur_crt, position, 2)
            elif cur_crt + 2 > 40:
                cur_crt = draw(res, cur_crt, position, 1)
                cur_crt = 0
                res.append('\n')
                cur_crt = draw(res, cur_crt, position, 1)
            else:
                cur_crt = draw(res, cur_crt, position, 2)
            register += i[1]
            position = {register - 1, register, register + 1}
    
    return ''.join(res)



if __name__ == '__main__':
    cur_dir = os.getcwd()
    path = cur_dir + '/AdventCode/input10.txt'
    data = read_file(path)
    signal_strength = find_strength(data)
    print(signal_strength)
    string = find_string(data)
    print(string)