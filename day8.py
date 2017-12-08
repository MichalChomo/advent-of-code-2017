def check_reg_val(reg, op, val, registers):
    if op == '<':
        return registers[reg] < int(val)
    elif op == '>':
        return registers[reg] > int(val)
    elif op == '<=':
        return registers[reg] <= int(val)
    elif op == '>=':
        return registers[reg] >= int(val)
    elif op == '==':
        return registers[reg] == int(val)
    elif op == '!=':
        return registers[reg] != int(val)

with open("day8_input") as infile:
    inlist = [line.replace('if ', '').strip().split(' ') for line in infile if line != '\n']

registers = {line[0]: 0 for line in inlist if line[0]}
max_during = 0
for line in inlist:
    if check_reg_val(line[3], line[4], line[5], registers):
        if line[1] == "inc":
            registers[line[0]] += int(line[2])
        elif line[1] == "dec":
            registers[line[0]] -= int(line[2])
    current_max = max(registers.values())
    if current_max > max_during:
        max_during = current_max
print(max(registers.values())) # part 1
print(max_during) # part 2
