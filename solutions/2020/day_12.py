from aocd import get_data

input = get_data(day=12, year=2020).splitlines()

DELTA = {"N": (1, 0), "S": (-1, 0), "E": (0, 1), "W": (0, -1)}
TURN = {"L": -1, "R": 1}


def solve(lines, part="part_1"):
    x, y = 0, 0
    wx, wy = (0, 1) if part == "part_1" else (1, 10)
    for line in lines:
        action, n = line[0], int(line[1:])
        if action in DELTA:
            dx, dy = DELTA[action]
            if part == "part_1":
                x, y = x + dx * n, y + dy * n
            else:
                wx, wy = wx + dx * n, wy + dy * n
        elif action in TURN:
            for _ in range(TURN[action] * (n // 90) % 4):
                wx, wy = -wy, wx
        elif action == "F":
            x, y = x + wx * n, y + wy * n
    return abs(x) + abs(y)


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    return solve(lines, "part_1")


def part_2(lines):
    return solve(lines, "part_2")


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
