from aocd import get_data

input = get_data(day=17, year=2020).splitlines()
from itertools import product
from collections import Counter


# WRITE YOUR SOLUTION HERE
def count_activ_neighboors(state, pos):
    D, H, W = len(state), len(state[0]), len(state[0])
    cnt_active = 0
    d, h, w = pos
    for dz, dy, dx in product(range(-1, 2), range(-1, 2), range(-1, 2)):
        if (dz, dy, dx) == (0, 0, 0):
            continue
        if 1 <= d + dz < D + 1 and 1 <= h + dy < H + 1 and 1 <= w + dx < W + 1:
            cnt_active += state[d + dz - 1][h + dy - 1][w + dx - 1] == "#"
    return cnt_active


def get_next_state(state):
    D, H, W = len(state), len(state[0]), len(state[0])
    new_D, new_H, new_W = D + 2, H + 2, W + 2
    next_state = [
        [["." for _ in range(new_W)] for _ in range(new_H)] for _ in range(new_D)
    ]
    for d in range(new_D):
        for h in range(new_H):
            for w in range(new_W):
                cnt_active = count_activ_neighboors(state, (d, h, w))
                current_state = (
                    state[d - 1][h - 1][w - 1]
                    if (1 <= d < D + 1 and 1 <= h < H + 1 and 1 <= w < W + 1)
                    else "."
                )
                match current_state:
                    case "#":
                        next_state[d][h][w] = (
                            "#" if (cnt_active == 2 or cnt_active == 3) else "."
                        )
                    case ".":
                        next_state[d][h][w] = "#" if cnt_active == 3 else "."
    return next_state


def part_1(lines):
    state = [lines]
    for _ in range(6):
        state = get_next_state(state)
    return sum([row.count("#") for grid in state for row in grid])


def neighbour_coordinates(p):
    return [
        tuple(a + b for a, b in zip(p, t))
        for t in product([-1, 0, 1], repeat=len(p))
        if any(t)
    ]


def simulate(dimensions, seed):
    active_coordinates = {
        (x, y) + (0,) * (dimensions - 2)
        for y, l in enumerate(seed)
        for x, c in enumerate(l)
        if c == "#"
    }
    for _ in range(6):
        total_neighbours = Counter(
            p
            for coordinate in active_coordinates
            for p in neighbour_coordinates(coordinate)
        )
        active_coordinates = {
            p
            for p, n in total_neighbours.items()
            if (p in active_coordinates and n == 2) or n == 3
        }
    return len(active_coordinates)


def part_2(lines):
    # Beautiful solution taken from warbaque's github
    return simulate(4, lines)


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
