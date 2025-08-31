from collections import deque

MAP_FROM_ASCII = lambda s: "".join(map(chr, s))
MAP_TO_ASCII = lambda s: list(map(ord, s))


class IntcodeComputer:
    _LOAD = 0
    _WRITE = 1

    _OPERATIONS = {
        1: (_LOAD, _LOAD, _WRITE),
        2: (_LOAD, _LOAD, _WRITE),
        3: (_WRITE,),
        4: (_LOAD,),
        5: (_LOAD, _LOAD),
        6: (_LOAD, _LOAD),
        7: (_LOAD, _LOAD, _WRITE),
        8: (_LOAD, _LOAD, _WRITE),
        9: (_LOAD,),
        99: (-1,),
    }

    def read_program(self, aoc_input):
        return list(map(int, aoc_input.split(",")))

    def __init__(self, program_file):
        init_program = self.read_program(program_file)
        self.memory = {i: m for i, m in enumerate(init_program)}
        self.input_buffer = deque([])
        self.output_buffer = deque([])
        self.rel_base = 0
        self.ip = 0
        self.hasted = False  # useful for day_13

    def send_output_buffer(self):
        output = list(self.output_buffer)
        self.output_buffer.clear()
        return output

    def apply_mode(self, v, p_mode, operation):
        match p_mode:
            case 0:
                return v if operation else self.memory.get(v, 0)
            case 1:
                return v
            case 2:
                rel_v = v + self.rel_base
                return rel_v if operation else self.memory.get(rel_v, 0)

    def run(self, input_data=None):
        if input_data:
            self.input_buffer.extend(input_data)

        while not self.hasted:
            opcode = self.memory[self.ip]
            op = opcode % 100
            if op == 99:
                self.hasted = True
                break

            operations = self._OPERATIONS[op]
            parameters = [self.memory[self.ip + 1 + i] for i in range(len(operations))]
            get_decomposition = lambda n, a: (n // 10**a) % 10
            parameters_mode = [
                get_decomposition(opcode, i + 2) for i in range(len(operations))
            ]
            params = [
                self.apply_mode(p, p_mode, operations[i])
                for i, (p, p_mode) in enumerate(zip(parameters, parameters_mode))
            ]

            if op == 1:
                v1, v2, store_pos = params
                self.memory[store_pos] = v1 + v2
            elif op == 2:
                v1, v2, store_pos = params
                self.memory[store_pos] = v1 * v2
            elif op == 3:
                pos = params[0]
                if not self.input_buffer:
                    return self.send_output_buffer()

                val = self.input_buffer.popleft()
                self.memory[pos] = val
            elif op == 4:
                out_val = params[0]
                self.output_buffer.append(out_val)
            elif op == 5:
                v1, v2 = params
                if v1:
                    self.ip = v2
                    continue
            elif op == 6:
                v1, v2 = params
                if not v1:
                    self.ip = v2
                    continue
            elif op == 7:
                v1, v2, store_pos = params
                self.memory[store_pos] = 1 if v1 < v2 else 0
            elif op == 8:
                v1, v2, store_pos = params
                self.memory[store_pos] = 1 if v1 == v2 else 0
            elif op == 9:
                v = params[0]
                self.rel_base += v

            self.ip += 1 + len(operations)

        return self.send_output_buffer()
