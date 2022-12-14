with open('AdventCode/input14.txt', 'r') as file:
    rock = []
    for f in file:
        rock.append([eval(x) for x in f.rstrip('\n').split(' -> ')])

min_row = min(min(i[0] for i in row) for row in rock)
max_row = max(max(i[0] for i in row) for row in rock)
min_col = min(min(i[1] for i in row) for row in rock)
max_col = max(max(i[1] for i in row) for row in rock)


def change_grid(grid, rock, add_cols = 0):
    for row in rock:
        left, right = 0, 1
        while right < len(row):
            if row[left][0] == row[right][0]:   # Same column
                fill_col = row[left][0] - min_row + add_cols
                if row[left][1] <= row[right][1]:
                    for i in range(row[left][1], row[right][1]+1):
                        grid[i][fill_col] = '#'
                else:
                    for i in range(row[left][1], row[right][1]-1, -1):
                       grid[i][fill_col] = '#'
            else:
                fill_row = row[left][1]
                if row[left][0] <= row[right][0]:
                    for i in range(row[left][0] - min_row + add_cols, row[right][0] + 1 - min_row + add_cols):
                        grid[fill_row][i] = '#'
                else:
                    for i in range(row[left][0] - min_row + add_cols, row[right][0] - 1 - min_row + add_cols, -1):
                       grid[fill_row][i] = '#'
            left += 1
            right += 1
    return grid


def print_grid(grid):
    s = ''
    for g in grid:
        s += ''.join(g)
        s += '\n'
    print(s)


def sand_fall(grid, start):
    rows, columns = len(grid), len(grid[0])
    inGrid = True
    counter = 0
    while inGrid:
        cur_col, cur_row = start[0], start[1]
        settled = False
        while not settled:
            if cur_row + 1 < rows and grid[cur_row + 1][cur_col] == '.':
                cur_row += 1
            elif cur_row + 1 < rows and cur_col - 1 >= 0 and grid[cur_row + 1][cur_col - 1] == '.':
                cur_col -= 1
                cur_row += 1
            elif cur_row + 1 < rows and cur_col + 1 < columns and grid[cur_row + 1][cur_col + 1] == '.':
                cur_col += 1
                cur_row += 1
            elif cur_row + 1 < rows and cur_col + 1 < columns and cur_col - 1 >= 0:
                grid[cur_row][cur_col] = 'o'
                counter += 1
                settled = True
                if cur_row == 0: inGrid = False
            else:
                inGrid = False
                settled = True

    return grid, counter


grid = []
for _ in range(max_col + 1):
    grid.append(['.'] * (max_row - min_row + 1))
grid = change_grid(grid, rock)
# Define starting position
grid[0][500 - min_row] = '+'

# Part 1
new_grid, sand_count = sand_fall(grid, (500 - min_row, 0))
print_grid(new_grid)
print(sand_count)


# Part 2
# Extend the grid
grid = []
add_cols = 400
for _ in range(max_col + 1 + 2):
    grid.append(['.'] * (max_row - min_row + 1 + add_cols))

change_grid(grid, rock, add_cols // 2)
grid[0][500 - min_row + add_cols // 2] = '+'
grid[-1] = ['#'] * len(grid[0])
new_grid, sand_count = sand_fall(grid, (500 - min_row + add_cols // 2, 0))
print_grid(grid)
print(sand_count)