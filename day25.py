class TM:

    tape = []
    tape_pos = 0
    current_state = ''
    transition_function = {}

    def __init__(self, init_state, transition_function, tape_length):
        self.tape = [0 for _ in range(tape_length)]
        self.tape_pos = len(self.tape) // 2
        self.current_state = init_state
        self.transition_function = transition_function

    def step(self):
        x = (self.current_state, self.tape[self.tape_pos])
        y = self.transition_function[x]
        self.current_state = y[0]
        self.tape[self.tape_pos] = y[1]
        self.tape_pos += y[2]
        self.check_tape()

    def check_tape(self):
        if self.tape_pos < 0 or self.tape_pos >= len(self.tape):
            length = len(self.tape) // 2
            for _ in range(length):
                self.tape.append(0)
                self.tape.insert(0, 0)
            if self.tape_pos < 0:
                self.tape_pos += length
            else:
                self.tape_pos += length + 1

    def checksum(self):
        return self.tape.count(1)

    def run(self, steps):
        for _ in range(steps):
            self.step()
        print(self.checksum())

def get_transition(lines, transition_function):
    state = lines[0][-3]
    move = 1 if lines[3][-4] == 'h' else -1
    transition_function[(state, 0)] = (lines[4][-3], int(lines[2][-3]), move)
    move = 1 if lines[7][-4] == 'h' else -1
    transition_function[(state, 1)] = (lines[8][-3], int(lines[6][-3]), move)

init_state = ''
steps = 0
transition_function = {}
with open("day25_input") as infile:
    init_state = infile.readline()[-3]
    steps = int(infile.readline().split(' ')[5])
    line = infile.readline()
    while line != '':
        transition = []
        for _ in range(9):
            transition.append(infile.readline())
        get_transition(transition, transition_function)
        line = infile.readline()
tm = TM(init_state, transition_function, 1000)
tm.run(steps)
