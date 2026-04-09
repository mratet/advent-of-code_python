from aocd import get_data

input = get_data(day=11, year=2017)

MOVES = {
    "n": (2, 0),
    "s": (-2, 0),
    "ne": (1, 1),
    "sw": (-1, -1),
    "nw": (1, -1),
    "se": (-1, 1),
}


# WRITE YOUR SOLUTION HERE
def get_dist_array(dirs):
    x, y = 0, 0
    dist = []
    for d in dirs:
        dx, dy = MOVES[d]
        x += dx
        y += dy
        dist.append((abs(x) + abs(y)) // 2)
    return dist


def part_1(lines):
    inst = list(lines.split(","))
    dist_array = get_dist_array(inst)
    return dist_array[-1]


def part_2(lines):
    inst = list(lines.split(","))
    dist_array = get_dist_array(inst)
    return max(dist_array)


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
