import copy

def enlarge(grid, count):
    old_len = len(grid[0])
    for row in grid:
        for i in range(count):
            row.insert(0, '.')
            row.insert(len(row), '.')
    row = ['.' for _ in range(old_len + (count * 2))]
    for i in range(count):
        grid.insert(0, copy.copy(row))
        grid.insert(len(grid), copy.copy(row))
    return grid

def print_grid(grid):
    for row in grid:
        print(row)
    print()

def step(direction, yy, xx):
    y = yy
    x = xx
    if direction == 0:
        y -= 1
    elif direction == 1:
        x += 1
    elif direction == 2:
        y += 1
    elif direction == 3:
        x -= 1
    return (y, x)

def turn_left(direction):
    return 3 if direction == 0 else (direction - 1)

def turn_right(direction):
    return (direction + 1) % 4

def reverse(direction):
    return (direction + 2) % 4

with open("day22_input") as infile:
    grid = [[x for x in line.strip()] for line in infile]
grid1 = enlarge(copy.deepcopy(grid), 27)
y = len(grid1) // 2
x = len(grid1[0]) // 2
direction = 0
infect = 0
for i in range(10000):
    if grid1[y][x] == '.':
        infect += 1
        grid1[y][x] = '#'
        direction = turn_left(direction)
    else:
        grid1[y][x] = '.'
        direction = turn_right(direction)
    (y, x) = step(direction, y, x)
    if y < 0 or x < 0:
        print("out of bounds, exit")
        exit()
print(infect)

grid2 = enlarge(copy.deepcopy(grid), 250)
y = len(grid2) // 2
x = len(grid2[0]) // 2
direction = 0
infect = 0
for i in range(10000000):
    if grid2[y][x] == '.':
        grid2[y][x] = 'W'
        direction = turn_left(direction)
    elif grid2[y][x] == 'W':
        infect += 1
        grid2[y][x] = '#'
    elif grid2[y][x] == '#':
        grid2[y][x] = 'F'
        direction = turn_right(direction)
    elif grid2[y][x] == 'F':
        grid2[y][x] = '.'
        direction = reverse(direction)
    (y, x) = step(direction, y, x)
    if y < 0 or x < 0:
        print("out of bounds, exit")
        exit()
print(infect)
