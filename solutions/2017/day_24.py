from aocd import get_data, submit
input = get_data(day=24, year=2017).splitlines()

# WRITE YOUR SOLUTION HERE
def parse_input(lines):
    wires = set()
    starting_wires = []
    double_wires = set()
    for line in lines:
        a, b = map(int, line.split('/'))
        if a == 0 or b == 0:
            starting_wires.append((a, b))
        elif a == b:
            double_wires.add(a)
        else:
            wires.add((a, b))
    return starting_wires, double_wires, wires

def compute_true_stat(W, path, d):
    connection = set()
    for (a, b) in path:
        connection.add(a)
        connection.add(b)
    double_wires = connection.intersection(d)
    return len(path) + len(double_wires), W + 2 * sum(double_wires)

def build_all_bridges(starting_wires, double_wires, wires):
    connected_wire = lambda a, b, free_slot : (a[1] == b[0] or a[1] == b[1]) if free_slot else (a[0] == b[0] or a[0] == b[1])
    visited = set()
    tab = []
    
    def dfs(last_wire, bridge_strength, path, free_slot):
        for wire in filter(lambda w: connected_wire(last_wire, w, free_slot), wires):
            if wire in visited: continue
            visited.add(wire)
            path.append(wire)
            dfs(wire, bridge_strength + sum(wire), path, 1 if last_wire[free_slot] == wire[0] else 0)
            path.pop()
            visited.remove(wire)
        tab.append(compute_true_stat(bridge_strength, path, double_wires))

    for w in starting_wires:
        free_slot = 1 if w[1] != 0 else 0
        dfs(w, w[free_slot], [w], free_slot)

    return tab

def part_1(lines):
    starting_wires, double_wires, wires = parse_input(lines)
    bridges = build_all_bridges(starting_wires, double_wires, wires)
    return max(bridges, key = lambda w: w[1])[1]

def part_2(lines):
    starting_wires, double_wires, wires = parse_input(lines)
    bridges = build_all_bridges(starting_wires, double_wires, wires)
    return max(bridges)[1]
# END OF SOLUTION
print(f'My answer is {part_1(input)}')
print(f'My answer is {part_2(input)}')

