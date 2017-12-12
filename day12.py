def get_progs_in_group(group_start, progs):
    group = [group_start]
    for p in group:
        for x in progs[p][1:]:
            if x not in group:
                group.append(x)
    return group

progs = []
with open("day12_input") as infile:
    for line in infile:
        line = line.strip().split("<->")
        progs.append([int(x) for x in line[0].strip().split(' ')] + [int(y) for y in line[1].split(',')])
print(len(get_progs_in_group(0, progs)))

groups = [sub[0] for sub in progs]
for g in groups:
    tmp = get_progs_in_group(g, progs)
    for g2 in tmp:
        if g == g2:
            continue
        try:
            groups.remove(g2)
        except:
            pass
print(len((groups)))
