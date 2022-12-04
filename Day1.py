import os

cur_dir = os.getcwd()
path = cur_dir + '/AdventCode/input'

# 1
max_calories = 0
calories = 0
with open(path, 'r') as file:
    for f in file:
        f = f.rstrip('\n')
        if f:
            calories += int(f)
        else:
           max_calories = max(max_calories, calories)
           calories = 0

print(max_calories)

# 2
max_calories = []
calories = 0
with open(path, 'r') as file:
    for f in file:
        f = f.rstrip('\n')
        if f:
            calories += int(f)
        else:
            max_calories.append(calories)
            if len(max_calories) > 3:
                max_calories.sort(reverse=True)
                max_calories.pop()
            calories = 0
print(sum(max_calories))