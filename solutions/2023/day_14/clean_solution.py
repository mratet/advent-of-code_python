from aocd import get_data

input = get_data(day=14, year=2023).splitlines()

ROTATIONS = {"n": (3, 1), "w": (0, 0), "s": (1, 3), "e": (2, 2)}

# WRITE YOUR SOLUTION HERE


def right_rotation(matrix, n):
    for _ in range(n):
        matrix = list(zip(*matrix[::-1], strict=False))
    return matrix


def west_shift(platform):
    return [
        "#".join("".join(sorted(section, reverse=True)) for section in "".join(line).split("#")) for line in platform
    ]


def shift(entry_platform, direction):
    pre_rot, post_rot = ROTATIONS[direction]
    platform = right_rotation(entry_platform.copy(), pre_rot)
    platform = west_shift(platform)
    return right_rotation(platform, post_rot)


def compute_load(platform):
    n = len(platform)
    return sum(n - row_idx for row_idx, row in enumerate(platform) for c in row if c == "O")


def detect_cycle(sequence):
    visited = {}
    for idx, val in enumerate(sequence):
        if val in visited:
            return visited[val], idx - visited[val]
        visited[val] = idx


def part_1(lines):
    return compute_load(shift(lines, "n"))


def part_2(lines):
    platform = lines.copy()
    sequences, loads = [], []
    for _ in range(200):
        sequences.append(hash(tuple(platform)))
        loads.append(compute_load(platform))
        for c in ROTATIONS:
            platform = shift(platform, c)
    start_cycle, length_cycle = detect_cycle(sequences)
    return loads[start_cycle + (1_000_000_000 - start_cycle) % length_cycle]


# END OF SOLUTION


print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
