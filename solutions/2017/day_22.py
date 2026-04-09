from aocd import get_data

input = get_data(day=22, year=2017).splitlines()

# WRITE YOUR SOLUTION HERE
DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def parse_input(lines):
    return {(x, y): "I" for x, line in enumerate(lines) for y, c in enumerate(line) if c == "#"}


def solve(lines, transitions, turns, steps):
    nodes = parse_input(lines)
    n = len(lines)
    cx, cy = n // 2, n // 2
    idx = 2
    ans = 0
    for _ in range(steps):
        state = nodes.get((cx, cy), "C")
        idx += turns[state]
        new_state = transitions[state]
        if new_state == "I":
            ans += 1
        if new_state == "C":
            nodes.pop((cx, cy), None)
        else:
            nodes[(cx, cy)] = new_state
        dx, dy = DIRS[idx % len(DIRS)]
        cx, cy = cx + dx, cy + dy
    return ans


def part_1(lines):
    transitions = {"C": "I", "I": "C"}
    turns = {"C": 1, "I": -1}
    return solve(lines, transitions, turns, 10_000)


def part_2(lines):
    transitions = {"C": "W", "W": "I", "I": "F", "F": "C"}
    turns = {"C": 1, "W": 0, "I": -1, "F": 2}
    return solve(lines, transitions, turns, 10_000_000)


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
