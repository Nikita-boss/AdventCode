def read_file(path):
    with open(path, 'r') as file:
        return file.read().rstrip('\n')

class Horizontal:
    def __init__(self):
        self.left = 2
        self.right = 5
        self.height = 1

    def move_horizontally(self, flow, atHeight):
        if flow == '>' and self.right != 6 and grid.grid[atHeight][self.right + 1] == '.':
            self.left += 1
            self.right += 1
        elif flow == '<' and self.left != 0 and grid.grid[atHeight][self.left - 1] == '.':
            self.left -= 1
            self.right -= 1

    def move_vertically(self, atHeight):
        for i in range(self.left, self.right + 1):
            if grid.grid[atHeight][i] != '.':
                return False
        return True

    def fill_grid(self, atHeight):
        for i in range(self.left, self.right + 1):
            grid.grid[atHeight + 1][i] = '#'

    def get_height(self):
        return self.height

    def clear(self):
        self.left = 2
        self.right = 5

class Plus:
    def __init__(self):
        self.left = 2
        self.right = 4
        self.height = 3

    def move_horizontally(self, flow, atHeight):
        if flow == '>' and self.right != 6 and grid.grid[atHeight][self.right] == '.' \
            and grid.grid[atHeight + 1][self.right + 1] == '.' and grid.grid[atHeight + 2][self.right] == '.':
            self.left += 1
            self.right += 1
        elif flow == '<' and self.left != 0 and grid.grid[atHeight][self.left] == '.' \
            and grid.grid[atHeight + 1][self.left -1] == '.' and grid.grid[atHeight + 2][self.left] == '.':
            self.left -= 1
            self.right -= 1

    def move_vertically(self, atHeight):
        if grid.grid[atHeight][self.left + 1] != '.' or grid.grid[atHeight + 1][self.left] != '.' or grid.grid[atHeight + 1][self.right] != '.':
            return False
        return True

    def fill_grid(self, atHeight):
        for i in range(self.left, self.right + 1):
            grid.grid[atHeight + 2][i] = '#'
        grid.grid[atHeight + 1][self.left + 1] = '#'
        grid.grid[atHeight + 3][self.left + 1] = '#'

    def get_height(self):
        return self.height
    
    def clear(self):
        self.left = 2
        self.right = 4

class L_shape:
    def __init__(self):
        self.left = 2
        self.right = 4
        self.height = 3

    def move_horizontally(self, flow, atHeight):
        if flow == '>' and self.right != 6 and grid.grid[atHeight][self.right + 1] == '.' \
            and grid.grid[atHeight + 1][self.right + 1] == '.' and grid.grid[atHeight + 2][self.right + 1] == '.':
            self.left += 1
            self.right += 1
        elif flow == '<' and self.left != 0 and grid.grid[atHeight][self.left - 1] == '.':
            self.left -= 1
            self.right -= 1

    def move_vertically(self, atHeight):
        for i in range(self.left, self.right + 1):
            if grid.grid[atHeight][i] != '.':
                return False
        return True

    def fill_grid(self, atHeight):
        for i in range(self.left, self.right + 1):
            grid.grid[atHeight + 1][i] = '#'
        grid.grid[atHeight + 2][self.right] = '#'
        grid.grid[atHeight + 3][self.right] = '#'

    def get_height(self):
        return self.height

    def clear(self):
        self.left = 2
        self.right = 4

class Vertical:
    def __init__(self):
        self.left = 2
        self.height = 4

    def move_horizontally(self, flow, atHeight):
        if flow == '>' and self.left != 6:
            for i in range(self.height):
                if grid.grid[atHeight + i][self.left + 1] != '.':
                    self.left -= 1
                    break
            self.left += 1
        elif flow == '<' and self.left != 0:
            for i in range(self.height):
                if grid.grid[atHeight + i][self.left - 1] != '.':
                    self.left += 1
                    break
            self.left -= 1

    def move_vertically(self, atHeight):
        if grid.grid[atHeight][self.left] != '.':
            return False
        return True

    def fill_grid(self, atHeight):
        for i in range(self.height):
            grid.grid[atHeight + i + 1][self.left] = '#'

    def get_height(self):
        return self.height

    def clear(self):
        self.left = 2

class Square:
    def __init__(self):
        self.left = 2
        self.right = 3
        self.height = 2

    def move_horizontally(self, flow, atHeight):
        if flow == '>' and self.right != 6 and grid.grid[atHeight][self.right + 1] == '.' \
            and grid.grid[atHeight + 1][self.right + 1] == '.':
            self.left += 1
            self.right += 1
        elif flow == '<' and self.left != 0 and grid.grid[atHeight][self.left - 1] == '.' \
            and grid.grid[atHeight + 1][self.left - 1] == '.':
            self.left -= 1
            self.right -= 1

    def move_vertically(self, atHeight):
        for i in range(self.left, self.right + 1):
            if grid.grid[atHeight][i] != '.':
                return False
        return True

    def fill_grid(self, atHeight):
        grid.grid[atHeight + 1][self.left] = '#'
        grid.grid[atHeight + 1][self.right] = '#'
        grid.grid[atHeight + 2][self.left] = '#'
        grid.grid[atHeight + 2][self.right] = '#'

    def get_height(self):
        return self.height

    def clear(self):
        self.left = 2
        self.right = 3

class Grid:
    def __init__(self, width, start_left):
        self.start_left = start_left
        self.width = width
        self.grid = []
        self.grid.append(['-'] * width)
        self.height = 0
        self.heights = []

    def new_rock(self):
        for _ in range(4):
            self.grid.append(['.'] * self.width)

    def print_grid(self):
        tmp = self.grid[::-1]
        s = ''
        for i in tmp:
            s = s + ''.join(i) + '\n'
        print(s)

    def get_height(self):
        return self.height

    def remove(self, r):
        for _ in range(r):
            del grid.grid[-1]

    def clean(self):
        minimum_empty = 0
        for i in range(self.width):
            for h in range(-1, -50, -1):
                if grid.grid[h][i] != '.':
                    minimum_empty = min(minimum_empty, h)
                    break
        floor = len(self.grid) + minimum_empty
        self.grid = [['-'] * self.width] + self.grid[floor + 1:]
        self.heights.append(floor)
        self.height -= floor
        


grid = Grid(width=7, start_left=1) 
        
def tetris(flow):
    hor = Horizontal()
    plus = Plus()
    L = L_shape()
    ver = Vertical()
    square = Square()
    shapes = [hor, plus, L, ver, square]
    flow_counter = 0
    shape_counter = 0
    for _ in range(1_000_000_000_000 // 4 + 1):
    #for _ in range(506):
        for shape in shapes:
            grid.new_rock()
            canMove = True
            atHeight = grid.get_height() + 4
            while canMove:
                #print(flow[flow_counter])
                shape.move_horizontally(flow[flow_counter], atHeight)
                atHeight -= 1
                canMove = shape.move_vertically(atHeight)
                flow_counter += 1
                if flow_counter == len(flow): flow_counter = 0
    
            shape.fill_grid(atHeight)
            shape.clear()
            grid.height = max(atHeight + shape.get_height(), grid.height)
            shape_counter += 1

            if shape_counter == 1_000_000_000_000: 
            #if shape_counter == 2022:
                return grid.get_height() + sum(grid.heights)

            if len(grid.grid) > grid.height + 10:
                grid.remove(len(grid.grid) - grid.height - 10)


            if grid.height > 50:
                grid.clean()
            #print(grid.get_height())
            #grid.print_grid()

    return grid.get_height() + sum(grid.heights)




path = 'AdventCode/input17.txt'
flow = read_file(path)
height = tetris(flow)
print(height)