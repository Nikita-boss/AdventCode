import os
from itertools import accumulate

cur_dir = os.getcwd()
path = cur_dir + '/AdventCode/input7.txt'


stack, sizes = [], []
with open(path, 'r') as file:
    for f in file:
        f = f.split()
        if f[0] == '$' and f[1] == 'cd' and f[2] == '..':
            s = stack.pop()
            sizes.append(s)
            stack[-1] += s
        elif f[0] == '$' and f[1] == 'cd':
            stack.append(0)
        elif f[0].isdigit():
            stack[-1] += int(f[0])
        
    sizes.extend(accumulate(stack[::-1]))
    res_1 = sum(s for s in sizes if s <= 100_000)
    res_2 = min([s for s in sizes if s >= max(sizes) - 40_000_000])

print(res_1)
print(res_2)
