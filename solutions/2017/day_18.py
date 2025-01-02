from aocd import get_data, submit
input = get_data(day=18, year=2017).splitlines()
from collections import defaultdict

# WRITE YOUR SOLUTION HERE
def part_1(lines):
    i = 0
    registers = defaultdict(int)
    get_value = lambda val: int(val) if val.lstrip('-').isdigit() else registers[val]

    while i < len(lines):
        op, *val = lines[i].split()
        if len(val) == 1:
            Z = get_value(val[0])
        if len(val) == 2:
            X, Y = val
            X = int(X) if X.lstrip('-').isdigit() else X
            Y = get_value(Y)

        if op == 'snd':
            frq = Z
        elif op == 'set':
            registers[X] = Y
        elif op == 'add':
            registers[X] += Y
        elif op == 'mul':
            registers[X] *= Y
        elif op == 'mod':
            registers[X] = registers[X] % Y
        elif op == 'rcv':
            if Z != 0:
                return frq
        elif op == 'jgz':
            if registers[X] > 0:
                i += Y - 1
        i += 1

def program_execution(program, state):
    pos = state['pos']
    registers = state['registers']
    snd_queue = state['snd_queue']
    rcv_queue = state['rcv_queue']
    cnt = state['count']

    while pos < len(program):
        op, *val = program[pos].split()
        if len(val) == 1:
            Z = val[0]
        if len(val) == 2:
            X, Y = val
            X = int(X) if X.lstrip('-').isdigit() else X
            Y = int(Y) if Y.lstrip('-').isdigit() else registers[Y]

        if op == 'snd':
            cnt += 1
            snd_queue.append(registers[Z])
        elif op == 'set':
            registers[X] = Y
        elif op == 'add':
            registers[X] += Y
        elif op == 'mul':
            registers[X] *= Y
        elif op == 'mod':
            registers[X] %= Y
        elif op == 'rcv':
            if len(rcv_queue) == 0:
                state['pos'] = pos
                state['registers'] = registers
                state['snd_queue'] = snd_queue
                state['rcv_queue'] = rcv_queue
                state['count'] = cnt
                return state
            registers[Z] = rcv_queue.pop(0)
        elif op == 'jgz':
            if isinstance(X, int) or registers[X] > 0:
                pos += Y - 1
        pos += 1
    assert 1 == 2

def part_2(lines):
    state0 = {'pos': 0, 'registers': defaultdict(int), 'snd_queue': [], 'rcv_queue': [], 'count': 0}
    state1 = {'pos': 0, 'registers': defaultdict(int), 'snd_queue': [], 'rcv_queue': [], 'count': 0}
    state1['registers']['p'] = 1
    while True:
        state0 = program_execution(lines, state0)
        state1 = program_execution(lines, state1)
        snd_q0, snd_q1 = state0['snd_queue'], state1['snd_queue']
        if not snd_q0 and not snd_q1:
            break
        state0['rcv_queue'].extend(snd_q1)
        state1['rcv_queue'].extend(snd_q0)
        state0['snd_queue'], state1['snd_queue'] = [], []
    return state1['count']

# END OF SOLUTION
print(f'My answer is {part_1(input)}')
print(f'My answer is {part_2(input)}')
