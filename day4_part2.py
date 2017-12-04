from collections import Counter

def is_anagram(x, y):
    cx = Counter(x)
    cy = Counter(y)
    return sorted(cx.most_common()) == sorted(cy.most_common())

def is_valid_line(line):
    c = Counter(line.split())
    if c.most_common(1)[0][1] > 1:
        return False
    l = [is_anagram(x, y) for x in c.keys() for y in c.keys() if x != y]
    return True not in l

with open("day4_input", 'r') as infile:
    total = 0
    for line in infile:
        if is_valid_line(line):
            total += 1

print(total)
