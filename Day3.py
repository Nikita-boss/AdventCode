import os
cur_dir = os.getcwd()
path = cur_dir + '/AdventCode/input3.txt'

'''
a = 'asvs'
first = set(a[:len(a)//2])
second = set(a[len(a)//2 : ])
print(first, second)
print(type(first.intersection(second)))
print(first.intersection(second).pop())
'''

# 1
with open(path, 'r') as file:
    total = 0
    for f in file:
        f = f.rstrip('\n')
        first = set(f[ : len(f)//2])
        second = set(f[len(f)//2 : ])
        c = first.intersection(second).pop()
        if ord(c) > 96:
            total += ord(c) - 96
        else:
            total += ord(c) - 64 + 26

print(total)

# 2
def get_priority(c: str) -> int:
    if ord(c) > 96:
        res = ord(c) - 96
    else:
        res = ord(c) - 64 + 26
    return res


with open(path, 'r') as file:
    total = 0
    person = 1
    group_sets = []
    for f in file:
        group_sets.append(set(f.rstrip('\n')))
        if person == 3:
            c = group_sets[0].intersection(group_sets[1], group_sets[2]).pop()
            total += get_priority(c)
            group_sets.clear()
            person = 1
        else:
            person += 1

print(total)