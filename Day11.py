import os
from typing import List
from collections import defaultdict, deque
from heapq import nlargest
from math import prod

def read_file(path: str) -> List[tuple]:
    # dict(monkey) -> items: deque
    #              -> operation: tuple
    #              -> test: int
    #              -> throw: tuple(if true, if false)

    items = defaultdict(deque)
    operation = defaultdict(tuple)
    test = defaultdict(int)
    throw = defaultdict(tuple)

    with open(path, 'r') as file:
        for f in file:
            f = f.rstrip('\n').lstrip(' ').split(' ')
            if f[0] == 'Monkey':
                monkey = int(f[1].rstrip(':'))
            elif f[0] == 'Starting':
                items[monkey] = deque([int(i.rstrip(',')) for i in f[2:]])
            elif f[0] == 'Operation:':
                operation[monkey] = (f[-2], f[-1])
            elif f[0] == 'Test:':
                test[monkey] = int(f[-1])
            elif f[0] == 'If' and f[1] == 'true:':
                true_value = int(f[-1])
            elif f[0] == 'If' and f[1] == 'false:':
                throw[monkey] = (true_value, int(f[-1]))
    return items, operation, test, throw

def monkey_business(items, operation, test, throw, rounds, doDivide) -> int:
    inspection = defaultdict(int)
    reduce_factor = prod(test.values())

    def pass_item(monkey: int):
        while items[monkey]:
            inspection[monkey] = inspection.get(monkey, 0) + 1
            item = items[monkey].popleft()

            # Operation
            sign = operation[monkey][0]
            if operation[monkey][1] != 'old':
                item = item + int(operation[monkey][1]) if sign == '+' else item * int(operation[monkey][1])
            else:
                item = item + item if sign == '+' else item * item

            # Divide by 3
            item = item // 3 if doDivide else item % reduce_factor

            # Test
            if not item % test[monkey]:
                items[throw[monkey][0]].append(item)
            else:
                items[throw[monkey][1]].append(item)

        return inspection


    for j in range(rounds):
        for i in range(len(items)):
            inspection = pass_item(i)


    temp = nlargest(2, inspection.values())
    return prod(temp)
    


if __name__ == '__main__':
    cur_dir = os.getcwd()
    path = cur_dir + '/AdventCode/input11.txt'
    items, operation, test, throw = read_file(path)
    # Part 1
    #rounds, doDivide = 20, True
    #res1 = monkey_business(items, operation, test, throw, rounds, doDivide)
    #print(res1)
    # Part 2
    rounds, doDivide = 10_000, False
    res2 = monkey_business(items, operation, test, throw, rounds, doDivide)
    print(res2)
