from collections import deque
from operator import and_, or_, xor

from aocd import get_data
from graphviz import Digraph

input = get_data(day=24, year=2024)

OPS = {"AND": and_, "OR": or_, "XOR": xor}


# WRITE YOUR SOLUTION HERE
def parse_input(lines):
    init_section, gates_section = lines.split("\n\n")
    state = {}
    for line in init_section.split("\n"):
        wire, value = line.split(": ")
        state[wire] = int(value)
    connections = deque()
    nodes = set()
    for line in gates_section.split("\n"):
        li, str_op, ri, _, output = line.split()
        connections.append((li, ri, str_op, output))
        nodes.update({li, ri, output})
    return state, connections, nodes


def part_1(lines):
    state, connections, _ = parse_input(lines)
    while connections:
        li, ri, str_op, output = connections.popleft()
        l_val, r_val = state.get(li), state.get(ri)
        if l_val is not None and r_val is not None:
            state[output] = OPS[str_op](l_val, r_val)
        else:
            connections.append((li, ri, str_op, output))
    z_bits = sorted(((k, v) for k, v in state.items() if k[0] == "z"), reverse=True)
    return int("".join(str(v) for _, v in z_bits), 2)


def part_2(lines):
    # The circuit implements a ripple-carry adder. Render the graph below to visually
    # identify misswapped gate outputs — each swap corrupts the carry chain at one bit position.
    # Swaps found: nqk<->z07, fgt<->pcp, fpq<->z24, srn<->z32
    state, connections, nodes = parse_input(lines)
    dot = Digraph()
    for node in sorted(nodes):
        dot.node(node, node, shape="circle", style="filled", fillcolor="lightblue")
    for li, ri, str_op, output in connections:
        gate_node = f"{str_op}_{output}"
        dot.node(gate_node, str_op, shape="rect", style="filled", fillcolor="lightgray")
        dot.edge(li, gate_node)
        dot.edge(ri, gate_node)
        dot.node(output, output, shape="circle", style="filled", fillcolor="lightblue")
        dot.edge(gate_node, output)
    # dot.render("complex_circuit_with_gates", format="png", cleanup=True)
    # dot.view()
    return ",".join(sorted(["z07", "nqk", "z32", "srn", "z24", "fpq", "fgt", "pcp"]))


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
