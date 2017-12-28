import numpy as np
import math

def get_square(hashdot):
    l = [
            list(x) for x in (
                row.replace('#', '1').replace('.', '0')
                for row in hashdot.strip().split('/')
            )
        ]
    return np.array(l, int)

def breakup(square):
    height = square.shape[0]
    if height != 2 and (height % 2) == 0:
        nrows = 2
        ncols = 2
    elif height != 3 and (height % 3) == 0:
        nrows = 3
        ncols = 3
    else:
        return square
    return (square.reshape(height // nrows, nrows, -1, ncols)
                .swapaxes(1,2)
                .reshape(-1, nrows, ncols))

def get_rule_variations(rule):
    if (np.count_nonzero(rule[0]) == 0
        or np.count_nonzero(rule[0]) == np.size(rule[0])):
            return [rule[0]]
    variations = []
    rot = rule[0]
    for i in range(4):
        rot = np.rot90(rot)
        if True in [np.array_equal(rot, a) for a in variations]:
            i += 1
            continue
        variations.append(rot)
        lr = np.fliplr(rot)
        if True in [np.array_equal(lr, a) for a in variations]:
            i += 1
            continue
        variations.append(lr)
        ud = np.flipud(rot)
        if True in [np.array_equal(ud, a) for a in variations]:
            i += 1
            continue
        variations.append(ud)
    return variations


def find_match(square, variations, rules):
    i = 0
    for v in variations:
        for vv in v:
            if np.array_equal(square, vv):
                return rules[i][1]
        i += 1

def join_square(square):
    rows = []
    lensqrt = int(math.sqrt(len(square)))
    for i in range(0, len(square)-1, lensqrt):
        tmp = np.concatenate((tuple([square[j] for j in range(i, i+lensqrt)])), 1)
        rows.append(tmp)
    return np.concatenate(tuple([row for row in rows]), 0)

with open("day21_input") as infile:
    rules = [
                [get_square(rule[0]), get_square(rule[1])] for rule in
                (line.strip().split("=>") for line in infile)
            ]
variations = []
for rule in rules:
    variations.append(get_rule_variations(rule))
square = get_square(".#./..#/###")
for i in range(18):
    square = breakup(square)
    if len(square.shape) == 3:
        subs = []
        for subsquare in square:
            subs.append(find_match(subsquare, variations, rules))
        square = join_square(np.array(subs))
    else:
        square = find_match(square, variations, rules)
print(np.count_nonzero(square))
