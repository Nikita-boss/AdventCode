from functools import cmp_to_key

with open('AdventCode/input13.txt', 'r') as file:
    pairs = [[eval(i) for i in x.split()] for x in file.read().split('\n\n')]


def is_correct_order(pair1, pair2) -> int:
    if isinstance(pair1, int) and isinstance(pair2, int):
        return pair1 - pair2

    if isinstance(pair1, list) and isinstance(pair2, list):
        if len(pair1) == 0 and len(pair2) == 0:
            return 0
        if len(pair1) == 0:
            return -1
        if len(pair2) == 0:
            return 1
        tmp = is_correct_order(pair1[0], pair2[0])
        return tmp if tmp != 0 else is_correct_order(pair1[1:], pair2[1:])

    return is_correct_order([pair1], pair2) if isinstance(pair1, int) else is_correct_order(pair1, [pair2])
    
# Part 1
print(sum(i for i, x in enumerate(pairs, start=1) if is_correct_order(x[0], x[1]) < 0))

# Part 2
tmp = [[[2]], [[6]]]
full_pairs = []
for x in pairs:
    full_pairs.extend(x)
full_pairs.extend(tmp)

pairs_sorted = sorted(full_pairs, key=cmp_to_key(is_correct_order))

i1, i2 = pairs_sorted.index([[2]]) + 1, pairs_sorted.index([[6]]) + 1
print(i1 * i2)
