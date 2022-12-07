import os

cur_dir = os.getcwd()
path = cur_dir + '/AdventCode/input6.txt'


with open(path, 'r') as file:
    counter = 0
    for f in file:
        array = f

# For part 2, change 4 to 14 at every encounter below
window = {}
for i, c in enumerate(array):
    if i < 4:
        window[c] = window.get(c, 0) + 1
        continue

    if len(window) == 4:
        index = i
        break
    
    window[c] = window.get(c, 0) + 1
    remove_c = array[i - 4]
    window[remove_c] -= 1
    if window[remove_c] == 0: window.pop(remove_c)


print(index)