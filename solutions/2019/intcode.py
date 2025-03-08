from collections import deque

read_program = lambda l : list(map(int, l.split(',')))

LOAD = 0
WRITE = 1

INTCODE_OPERATIONS = {
    1: (LOAD, LOAD, WRITE),
    2: (LOAD, LOAD, WRITE),
    3: (WRITE,),
    4: (LOAD,),
    5: (LOAD, LOAD),
    6: (LOAD, LOAD),
    7: (LOAD, LOAD, WRITE),
    8: (LOAD, LOAD, WRITE),
    9: (LOAD,),
    99: (-1,),
}

def apply_mode(v, p_mode, memory, rel_base, operation):
    # WRITE = 1 / LOAD = 0
    if p_mode == 0:
        return v if operation else memory.get(v, 0)
    elif p_mode == 1:
        return v
    elif p_mode == 2:
        rel_v = v + rel_base
        return rel_v if operation else memory.get(rel_v, 0)

def run_program(memory, input_buffer=deque([])):
    memory = {i: m for i, m in enumerate(memory)}
    inst_pointer = 0
    output_buffer = deque([])
    rel_base = 0

    while True:
        opcode = memory[inst_pointer]
        op = opcode % 100
        operations = INTCODE_OPERATIONS[op]
        parameters = [memory[inst_pointer + 1 + i] for i in range(len(operations))]
        get_decomposition = lambda n, a : (n // 10 ** a) % 10
        parameters_mode = [get_decomposition(opcode, i + 2) for i in range(len(operations))]
        parameters = [apply_mode(p, p_mode, memory, rel_base, operations[i]) for i, (p, p_mode) in enumerate(zip(parameters, parameters_mode))]

        if op == 99:
            break
        if op == 1:
            v1, v2, store_pos = parameters
            memory[store_pos] = v1 + v2
        elif op == 2:
            v1, v2, store_pos = parameters
            memory[store_pos] = v1 * v2
        elif op == 3:
            pos = parameters[0]
            if not input_buffer:
                break
            val = input_buffer.popleft()
            memory[pos] = val
        elif op == 4:
            out_val = parameters[0]
            output_buffer.append(out_val)
        elif op == 5:
            v1, v2 = parameters
            if v1:
                inst_pointer = v2
                continue
        elif op == 6:
            v1, v2 = parameters
            if not v1:
                inst_pointer = v2
                continue
        elif op == 7:
            v1, v2, store_pos = parameters
            memory[store_pos] = 1 if v1 < v2 else 0
        elif op == 8:
            v1, v2, store_pos = parameters
            memory[store_pos] = 1 if v1 == v2 else 0
        elif op == 9:
            v = parameters[0]
            rel_base += v

        inst_pointer += 1 + len(operations)
    return memory, output_buffer



