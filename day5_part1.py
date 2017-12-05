with open("day5_input", 'r') as infile:
    inlist = [int(x.strip()) for x in infile if x != '\n']

steps = 0
pos = 0
newpos = 0
try:
    while True:
        newpos = pos + inlist[pos]
        inlist[pos] += 1
        steps += 1
        pos = newpos
except:
    print(steps)
