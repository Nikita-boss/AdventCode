import os
cur_dir = os.getcwd()
path = cur_dir + '/AdventCode/input4.txt'

# 1 and 2
with open(path, 'r') as file:
    fully_overlap = overlap = 0
    for f in file:
        f = f.rstrip('\n')
        tasks = f.split(',')
        task1, task2 = tasks[0], tasks[1]
        tmp = task1.split('-')
        first_in_task1 = int(tmp[0])
        second_in_task1 = int(tmp[1])
        tmp = task2.split('-')
        first_in_task2 = int(tmp[0])
        second_in_task2 = int(tmp[1])

        if (first_in_task1 <= first_in_task2 and second_in_task1 >= second_in_task2) or \
            first_in_task1 >= first_in_task2 and second_in_task1 <= second_in_task2:
            fully_overlap += 1
        if (second_in_task1 >= first_in_task2 and first_in_task1 <= first_in_task2) or \
            (second_in_task2 >= first_in_task1 and first_in_task2 <= first_in_task1):
            overlap += 1

print(fully_overlap, overlap)