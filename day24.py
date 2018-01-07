def get_common_ports(c1, c2):
    if c1 == c2:
        return c1
    elif c1[0] == c2[0] or c1[0] == c2[1]:
        return c1[0]
    elif c1[1] == c2[0] or c1[1] == c2[1]:
        return c1[1]
    else:
        return None

with open("day24_input") as infile:
    components = [[int(x) for x in line.split('/')] for line in infile]
bridges = [[c] for c in components if 0 in c]
components = [c for c in components if 0 not in c]
for b in bridges:
    next_possible_comps = []
    for c in components:
        common_last = get_common_ports(b[-1], c)
        common_before_last = None
        try:
            common_before_last = get_common_ports(b[-2], c)
        except:
            pass
        if (c not in b
            and common_last is not None
            and (common_last != common_before_last or b[-1][0] == b[-1][1])):
            next_possible_comps.append(c)
    for nc in next_possible_comps:
        new_b = list(b)
        new_b.append(nc)
        bridges.append(new_b)
print(max([sum([sum(x) for x in b]) for b in bridges]))
maxlen = max([len(b) for b in bridges])
print(max([sum([sum(x) for x in b]) for b in bridges if len(b) == maxlen]))
