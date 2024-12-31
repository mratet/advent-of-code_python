from aocd import get_data, submit
input = get_data(day=24, year=2024)

from operator import and_, or_, xor
from collections import deque
from graphviz import Digraph

class Module:
    def __init__(self, li, ri, op, output):
        self.li = li
        self.ri = ri
        self.output = output
        self.str_op = op
        match op:
            case 'AND': self.op = and_
            case 'OR': self.op = or_
            case 'XOR': self.op = xor

def parse_input(input):
    input = input.split('\n\n')
    state = {}
    init_wires = input[0].split('\n')
    for line in init_wires:
        wires, b = line.split(': ')
        state[wires] = int(b)

    connections = deque()
    gates_connection = input[1].split('\n')
    nodes = set()
    for connection in gates_connection:
        li, op, ri, _, output = connection.split()
        connections.append(Module(li, ri, op, output))
        nodes.update({li, ri, output})
    return state, connections, nodes

# WRITE YOUR SOLUTION HERE
def part_1(lines):
    state, connections, nodes = parse_input(lines)
    while connections:
        module = connections.popleft()
        li = state.get(module.li)
        ri = state.get(module.ri)
        if li is not None and ri is not None:
            state[module.output] = module.op(li, ri)
        else:
            connections.append(module)

    ans = sorted([(k, v) for k, v in state.items() if k[0] == 'z'], reverse=True)
    final_int = ''
    for k, v in ans:
        final_int += str(v)
    return int(final_int, 2)

def part_2(lines):
    state, connections, nodes = parse_input(lines)
    modules = list(connections)
    dot = Digraph()

    nodes = sorted(nodes)
    for input_node in nodes:
        dot.node(input_node, input_node, shape="circle", style="filled", fillcolor="lightblue")

    for module in modules:
        gate_node = f"{module.str_op}_{module.output}"
        dot.node(gate_node, module.str_op, shape="rect", style="filled", fillcolor="lightgray")
        dot.edge(module.li, gate_node)
        dot.edge(module.ri, gate_node)
        dot.node(module.output, module.output, shape="circle", style="filled", fillcolor="lightblue")
        dot.edge(gate_node, module.output)
    # dot.render("complex_circuit_with_gates", format="png", cleanup=True)  # Sauvegarder en PNG
    # dot.view()
    # swap gates
    # nqk - z07
    # fgt - pcp (near z17)
    # fpq - z24
    # srn - z32
    return ','.join(sorted(['z07', 'nqk', 'z32', 'srn', 'z24', 'fpq', 'fgt', 'pcp']))

# END OF SOLUTION
print(f'My answer is {part_1(input)}')
print(f'My answer is {part_2(input)}')
