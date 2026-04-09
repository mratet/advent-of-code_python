from aocd import get_data

input = get_data(day=24, year=2017).splitlines()


# WRITE YOUR SOLUTION HERE
def parse_input(lines):
    wires = set()
    starting_wires = []
    double_wires = set()
    for line in lines:
        a, b = map(int, line.split("/"))
        if a == 0 or b == 0:
            starting_wires.append((a, b))
        elif a == b:
            double_wires.add(a)
        else:
            wires.add((a, b))
    return starting_wires, double_wires, wires


def build_all_bridges(starting_wires, double_wires, wires):
    connected_wire = (
        lambda a, b, free_slot: (a[1] == b[0] or a[1] == b[1]) if free_slot else (a[0] == b[0] or a[0] == b[1])
    )
    visited = set()
    max_strength = 0
    best_longest = (0, 0)  # (depth, strength)

    def dfs(last_wire, depth, strength, free_slot):
        nonlocal max_strength, best_longest
        for wire in filter(lambda w: connected_wire(last_wire, w, free_slot), wires):
            if wire in visited:
                continue
            visited.add(wire)
            dfs(
                wire,
                depth + 1,
                strength + sum(wire),
                1 if last_wire[free_slot] == wire[0] else 0,
            )
            visited.remove(wire)
        # Account for double wires in depth and strength
        connection = {port for wire in visited for port in wire}
        used_doubles = connection.intersection(double_wires)
        true_depth = depth + len(used_doubles)
        true_strength = strength + 2 * sum(used_doubles)
        max_strength = max(max_strength, true_strength)
        best_longest = max(best_longest, (true_depth, true_strength))

    for w in starting_wires:
        free_slot = 1 if w[1] != 0 else 0
        visited.add(w)
        dfs(w, 1, w[free_slot], free_slot)
        visited.remove(w)

    return max_strength, best_longest[1]


def solve(lines):
    starting_wires, double_wires, wires = parse_input(lines)
    return build_all_bridges(starting_wires, double_wires, wires)


def part_1(lines):
    max_strength, _ = solve(lines)
    return max_strength


def part_2(lines):
    _, longest_strength = solve(lines)
    return longest_strength


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
