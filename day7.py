def get_weight(name, programs):
    weight = 0
    if len(programs[name]) == 1:
        return programs[name][0]
    else:
        for n in programs[name][1]:
            weight += get_weight(n, programs)
        return weight + programs[name][0]

with open("day7_input") as infile:
    programs = {}
    for line in infile:
        for ch in ['(', ')', ',', '-', '>']:
            if ch in line:
                line = line.replace(ch,'')
        line = line.strip().split(' ')
        if len(line) > 2:
            programs[line[0]] = (int(line[1]), line[3:])
        elif len(line) > 1:
            programs[line[0]] = (int(line[1]),)

# part 1
lists = [v[1] for v in programs.values() if len(v) == 2]
for name in programs:
    uniq = True
    for l in lists:
        if name in l:
            uniq = False
            break
    if uniq:
        print(name)
        break

# part 2
unbalanced_dict = []
unbalanced_programs = []
for n in programs:
    if len(programs[n]) == 1: continue
    weights = []
    for name in programs[n][1]:
        weights.append(get_weight(name, programs))
    if weights.count(weights[0]) != len(weights):
        diff = max(weights) - min(weights)
        unbalanced_programs.append(programs[n][1])
        if weights.count(max(weights)) > 1:
            unbalanced_dict.append((n, programs[programs[n][1][weights.index(min(weights))]][0] - diff))
        else:
            unbalanced_dict.append((n, programs[programs[n][1][weights.index(max(weights))]][0] - diff))
i = 0
for p in unbalanced_programs:
    res = True
    for pp in unbalanced_dict:
        if pp[0] in p:
            res = False
    if res:
        print(unbalanced_dict[i][1])
        break
    i += 1
