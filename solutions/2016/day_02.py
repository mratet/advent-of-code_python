from aocd import get_data

input = get_data(day=2, year=2016).splitlines()

N, S, E, W = (0, 1), (0, -1), (1, 0), (-1, 0)
dir = {"U": S, "D": N, "R": E, "L": W}


def part_1(input):
    PAD = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    res = ""
    state = (1, 1)

    for l in input:
        for c in l:
            dx, dy = dir[c]
            state = (state[0] + dx, state[1] + dy)
            state = (min(max(state[0], 0), 2), min(max(state[1], 0), 2))
        res += str(PAD[state[1]][state[0]])
    return res


def part_2(input):
    PAD = [
        ["x", "x", "1", "x", "x"],
        ["x", "2", "3", "4", "x"],
        ["5", "6", "7", "8", "9"],
        ["x", "A", "B", "C", "x"],
        ["x", "x", "D", "x", "x"],
    ]

    res = ""
    state = (0, 2)

    for l in input:
        for c in l:
            dx, dy = dir[c]
            state = (state[0] + dx, state[1] + dy)
            state = (min(max(state[0], 0), 4), min(max(state[1], 0), 4))
            if PAD[state[1]][state[0]] == "x":
                # Undo the last move
                state = (state[0] - dx, state[1] - dy)
        res += PAD[state[1]][state[0]]
    return res


print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
