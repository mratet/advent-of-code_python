from aocd import get_data

input = get_data(day=2, year=2016).splitlines()

S, N, E, W = (0, 1), (0, -1), (1, 0), (-1, 0)
DIR = {"U": N, "D": S, "R": E, "L": W}


def make_pad(grid):
    return {(x, y): val for y, row in enumerate(grid) for x, val in enumerate(row) if val != "."}


PAD_1 = make_pad([["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]])

PAD_2 = make_pad(
    [
        [".", ".", "1", ".", "."],
        [".", "2", "3", "4", "."],
        ["5", "6", "7", "8", "9"],
        [".", "A", "B", "C", "."],
        [".", ".", "D", ".", "."],
    ]
)


def solve(input, pad, start):
    pos = start
    res = ""
    for line in input:
        for c in line:
            dx, dy = DIR[c]
            if (next_pos := (pos[0] + dx, pos[1] + dy)) in pad:
                pos = next_pos
        res += pad[pos]
    return res


def part_1(input):
    return solve(input, pad=PAD_1, start=(1, 1))


def part_2(input):
    return solve(input, pad=PAD_2, start=(0, 2))


print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
