def get_dir_steps(steps):
    return [
                ("nw", steps.count("nw")),
                ("n", steps.count("n")),
                ("ne", steps.count("ne")),
                ("se", steps.count("se")),
                ("s", steps.count("s")),
                ("sw", steps.count("sw"))
           ]

def rem_opposites(dir_steps):
    new_dir_steps = [('', 0) for _ in range(6)]
    for i in range(3): 
        i2 = i + 3
        if dir_steps[i][1] > dir_steps[i2][1]:
            new_dir_steps[i] = (dir_steps[i][0], dir_steps[i][1] - dir_steps[i2][1])
        else:
            new_dir_steps[i2] = (dir_steps[i2][0], dir_steps[i2][1] - dir_steps[i][1])
    return new_dir_steps

def find_max(dir_steps):
    dir_steps = rem_opposites(dir_steps)
    total = 0
    used = []
    i = -1
    while len(used) < 3:
        for direction, steps in dir_steps:
            i += 1
            if not direction:
                continue
            if len(used) > 0 and direction not in used:
                total += steps
                used += [direction]
                break
            try:
                next_ = dir_steps[(i + 2) % 6]
                if next_[0]:
                    total += max(steps, next_[1])
                    used += [direction, next_[0]]
            except:
                pass
    return total

with open("day11_input") as infile:
    steps = []
    max_dist = 0
    step = ""
    while True:
        c = infile.read(1)
        if not c:
            steps.append(step.strip())
            tmp_max = find_max(get_dir_steps(steps))
            if tmp_max > max_dist:
                max_dist = tmp_max
            break
        if c == ',':
            steps.append(step.strip())
            tmp_max = find_max(get_dir_steps(steps))
            if tmp_max > max_dist:
                max_dist = tmp_max
            step = ""
        elif c != ' ':
            step += c
print(find_max(get_dir_steps(steps)))
print(max_dist)
