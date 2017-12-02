import day2_part1

infile = open("day2_part1_input", 'r')

res = []
for line in infile:
    line = line.replace('\n', '')
    if len(line) != 0:
        intlist = day2_part1.get_intlist(line)
        res.append(sum([x // y for x in intlist for y in intlist if x % y == 0 and x != y]))
print(sum(res))
infile.close()
