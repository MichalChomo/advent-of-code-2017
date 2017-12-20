import threading
import queue
import copy

exit_flag = False

def do_instruction_1(inst, reg, val=0):
    global regs
    global ip
    global sound
    ip_changed = False
    if val != 0 and str.isalpha(val):
        if inst == "set":
            regs[reg] = regs[val]
        elif inst == "add":
            regs[reg] += regs[val]
        elif inst == "mul":
            regs[reg] *= regs[val]
        elif inst == "mod":
            regs[reg] %= regs[val]
        elif inst == "rcv":
            if regs[reg] != 0:
                print(sound)
                return True
        elif inst == "snd":
            sound = regs[reg]
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
        elif inst == "add":
            regs[reg] += val
        elif inst == "mul":
            regs[reg] *= val
        elif inst == "mod":
            regs[reg] %= val
        elif inst == "snd":
            if str.isdecimal(reg):
                sound = reg
            else:
                sound = regs[reg]
        elif inst == "rcv":
            if str.isdecimal(reg):
                if reg != 0:
                    print(sound)
                    return True
            else:
                if regs[reg] != 0:
                    print(sound)
                    return True
        elif inst == "jgz":
            if not reg in regs:
                if int(reg) > 0:
                    ip += val
                    ip_changed = True
            elif regs[reg] > 0:
                ip += val
                ip_changed = True
    if not ip_changed:
        ip += 1
    return False

class Prog(threading.Thread):
    def __init__(self, pr_id, my_q, other_q, my_q_lock, other_q_lock, inst, regs):
        threading.Thread.__init__(self)
        self.pr_id = pr_id
        self.my_q = my_q
        self.other_q = other_q
        self.my_q_lock = my_q_lock
        self.other_q_lock = other_q_lock
        self.inst = inst
        self.regs = copy.copy(regs)
        self.regs['p'] = pr_id
        self.ip = 0
        self.send_count = 0

    def do_instruction(self, inst, reg, val=0):
        global exit_flag
        ip_changed = False
        if val != 0 and str.isalpha(val):
            if inst == "set":
                self.regs[reg] = self.regs[val]
            elif inst == "add":
                self.regs[reg] += self.regs[val]
            elif inst == "mul":
                self.regs[reg] *= self.regs[val]
            elif inst == "mod":
                self.regs[reg] %= self.regs[val]
            elif inst == "jgz":
                if not reg in self.regs:
                    if int(reg) > 0:
                        self.ip += val
                        ip_changed = True
                elif self.regs[reg] > 0:
                    self.ip += self.regs[val]
                    ip_changed = True
        else:
            val = int(val)
            if inst == "set":
                self.regs[reg] = val
            elif inst == "add":
                self.regs[reg] += val
            elif inst == "mul":
                self.regs[reg] *= val
            elif inst == "mod":
                self.regs[reg] %= val
            elif inst == "snd":
                self.send_count += 1
                self.other_q_lock.acquire()
                if str.isdecimal(reg):
                    self.other_q.put(reg)
                else:
                    self.other_q.put(self.regs[reg])
                self.other_q_lock.release()
            elif inst == "rcv":
                if self.my_q.empty() and self.other_q.empty():
                    exit_flag = True
                    self.other_q.put(None)
                else:
                    self.regs[reg] = self.my_q.get()
                    if self.regs[reg] == None:
                        exit_flag = True
            elif inst == "jgz":
                if not reg in self.regs:
                    if int(reg) > 0:
                        self.ip += val
                        ip_changed = True
                elif self.regs[reg] > 0:
                    self.ip += val
                    ip_changed = True
        if not ip_changed:
            self.ip += 1

    def run(self):
        global exit_flag
        i = 0
        while self.ip < len(self.inst):
            if exit_flag:
                break
            if len(self.inst[self.ip]) > 2:
                self.do_instruction(self.inst[self.ip][0], self.inst[self.ip][1], self.inst[self.ip][2])
            else:
                self.do_instruction(self.inst[self.ip][0], self.inst[self.ip][1])
        exit_flag = True
        if self.pr_id == 1:
            print(self.send_count)


with open("day18_input") as infile:
    inst = [line.strip().split(' ') for line in infile]
sound = 0
ip = 0
regs = {k[1]: 0 for k in inst if str.isalpha(k[1])} 
while ip < len(inst):
    if len(inst[ip]) > 2:
        if do_instruction_1(inst[ip][0], inst[ip][1], inst[ip][2]):
            break
    else:
        if do_instruction_1(inst[ip][0], inst[ip][1]):
            break

regs = {k[1]: 0 for k in inst if str.isalpha(k[1])} 
q_size = 1000
q0 = queue.Queue(q_size)
q1 = queue.Queue(q_size)
q0_lock = threading.Lock()
q1_lock = threading.Lock()
p0 = Prog(0, q0, q1, q0_lock, q1_lock, inst, regs)
p1 = Prog(1, q1, q0, q1_lock, q0_lock, inst, regs)
p0.start()
p1.start()
p0.join()
p1.join()
