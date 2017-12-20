def get_coords(y, x, lines):
    global direction
    if direction == 0 and y > 0:
        if not str.isspace(lines[y-1][x]):
            return (y-1, x)
    elif direction == 1 and x < (len(lines[y]) - 1):
        if not str.isspace(lines[y][x+1]):
            return (y, x+1)
    elif direction == 2 and y < (len(lines) - 1):
        if not str.isspace(lines[y+1][x]):
            return (y+1, x)
    elif direction == 3 and x > 0:
        if not str.isspace(lines[y][x-1]):
            return (y, x-1)
    for yy in [y-1, y+1]:
        if yy < 0 or yy >= len(lines):
            continue
        if not str.isspace(lines[yy][x]):
            if yy == (y-1) and direction != 2:
                direction = 0
                return (yy, x)
            if yy == (y+1) and direction != 0:
                direction = 2
                return (yy, x)
    for xx in [x-1, x+1]:
        if xx < 0 or xx >= len(lines[y]):
            continue
        if not str.isspace(lines[y][xx]):
            if xx == (x-1) and direction != 1:
                direction = 3
                return (y, xx)
            if xx == (x+1) and direction != 3:
                direction = 1
                return (y, xx)
    return (-1, -1)


with open("day19_input") as infile:
    lines = [line.replace('\n', '') for line in infile]
y = 0
x = len(lines[0]) - len(lines[0].lstrip())
direction = 2 # 0 up, 1 right, 2 down, 3 left
steps = 0
while True:
    if str.isalpha(lines[y][x]):
        print(lines[y][x], end='')
    (y, x) = get_coords(y, x, lines)
    steps += 1
    if y == -1:
        break
print('\n' + str(steps))
