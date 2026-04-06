from aocd import get_data

input = get_data(day=3, year=2015)

DIRS = {"v": (0, -1), "^": (0, 1), ">": (1, 0), "<": (-1, 0)}


def follow_direction(instructions):
    pos = (0, 0)
    visited = {pos}

    for c in instructions:
        dx, dy = DIRS[c]
        pos = (pos[0] + dx, pos[1] + dy)
        visited.add(pos)

    return visited


def part_1(input):
    return len(follow_direction(input))


def part_2(input):
    santa = follow_direction(input[::2])
    bot_santa = follow_direction(input[1::2])
    return len(santa | bot_santa)


print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
