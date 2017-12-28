def to_val(x):
    global regs
    if str.isalpha(x):
        return regs[x]
    else:
        return int(x)

def do_instruction(inst, reg, val=0):
    global regs
    global ip
    ip_changed = False
    muls = 0
    if val != 0 and str.isalpha(val):
        if inst == "set":
            regs[reg] = regs[val]
        elif inst == "sub":
            regs[reg] -= regs[val]
        elif inst == "mul":
            regs[reg] *= regs[val]
            muls += 1
        elif inst == "jgz":
            if not reg in regs:
                if int(reg) > 0:
                    ip += val
                    ip_changed = True
            elif regs[reg] > 0:
                ip += regs[val]
                ip_changed = True
    else:
        val = int(val)
        if inst == "set":
            regs[reg] = val
        elif inst == "sub":
            regs[reg] -= val
        elif inst == "mul":
            regs[reg] *= val
            muls += 1
        elif inst == "jnz":
            if not reg in regs:
                if int(reg) != 0:
                    ip += val
                    ip_changed = True
            elif regs[reg] != 0:
                ip += val
                ip_changed = True
    if not ip_changed:
        ip += 1
    return muls

def is_prime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n%f == 0: return False
        if n%(f+2) == 0: return False
        f +=6
    return True 

with open("day23_input") as infile:
    inst = [line.strip().split(' ') for line in infile]
ip = 0
regs = {k[1]: 0 for k in inst if str.isalpha(k[1])} 

muls = 0
while ip < len(inst):
    muls += do_instruction(inst[ip][0], inst[ip][1], inst[ip][2])
print(muls)

b = to_val(inst[0][2]) * to_val(inst[4][2]) - to_val(inst[5][2])
c = b - to_val(inst[7][2])
step = -to_val(inst[30][2])
not_primes = 0
for b in range(b, c, step):
    if not is_prime(b):
        not_primes += 1
print(not_primes)
