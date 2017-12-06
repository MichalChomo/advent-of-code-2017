with open("day6_input") as infile:
    cycles = [[int(x) for x in infile.readline().split('\t') if x != '\n']]

steps = 0
while True:
    current_cycle = cycles[-1]
    max_ = max(current_cycle)
    maxindex = current_cycle.index(max_)
    new_cycle = current_cycle[:]
    new_cycle[maxindex] = 0
    for i in range(maxindex + 1, maxindex + 1 + max_):
        new_cycle[i % len(new_cycle)] += 1
    cycles.append(new_cycle)
    steps += 1
    if steps > 1 and new_cycle in cycles[:-1]: break
print(steps)
print(steps - cycles[:-1].index(cycles[-1]))
