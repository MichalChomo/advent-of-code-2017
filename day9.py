with open("day9_input") as infile:
    garbage = False
    garbage_count = 0
    nesting = 0
    total = 0
    while True:
        c = infile.read(1)
        if not c:
            break
        if c == '!':
            infile.read(1)
            continue
        if garbage:
            if c == '>':
                garbage = False
            else:
                garbage_count += 1
            continue
        if c == '<':
            garbage = True
            continue
        if c == '{':
            nesting += 1
        if c == '}':
            total += nesting
            nesting -= 1
print(total)
print(garbage_count)
