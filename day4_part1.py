from collections import Counter

def is_valid_line(line):
    c = Counter(line.split())
    for val in c.values():
        if val > 1: return False
    return True

with open("day4_input", 'r') as infile:
    total = 0
    for line in infile:
        line = line.replace('\n', '')
        if len(line) != 0:
            if is_valid_line(line):
                total += 1

print(total)
