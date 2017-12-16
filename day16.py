import string

def spin(x, progs):
    return progs[-x:] + progs[:-x]

def exchange(move, progs):
    l = move[1:].split('/')
    a = int(l[0])
    b = int(l[1])
    tmp = progs[a]
    progs[a] = progs[b]
    progs[b] = tmp
    return progs

def partner(move, progs):
    l = move[1:].split('/')
    a = l[0]
    b = l[1]
    index_a = progs.index(a)
    index_b = progs.index(b)
    tmp = progs[index_a]
    progs[index_a] = progs[index_b]
    progs[index_b] = tmp
    return progs

def make_move(move, progs):
    if move[0] == 's':
        return spin(int(move[1:]), progs)
    if move[0] == 'x':
        return exchange(move, progs)
    if move[0] == 'p':
        return partner(move, progs)

progs = list(string.ascii_lowercase[:16])
progs_orig = progs[:]
moves = []
with open("day16_input") as infile:
    move = ""
    while True:
        c = infile.read(1)
        if not c:
            move = move.strip()
            moves.append(move)
            break
        if c != ',':
            move += c
        else:
            moves.append(move)
            move = ""
for move in moves:
    progs = make_move(move, progs)
print(''.join(progs))
repeat_after = 1
progs_list = []
while progs != progs_orig:
    repeat_after += 1
    for move in moves:
        progs = make_move(move, progs)
    progs_list.append(progs[:])
print(''.join(progs_list[(1000000000 % repeat_after) - 2]))
