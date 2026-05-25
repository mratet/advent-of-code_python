from collections import defaultdict, deque

from aocd import get_data

input = get_data(day=22, year=2023).splitlines()

# WRITE YOUR SOLUTION HERE


def parse_input(lines):
    bricks = []
    for line in lines:
        start, end = line.split("~")
        bricks.append([[int(c) for c in start.split(",")], [int(c) for c in end.split(",")]])
    return bricks


def settle(bricks):
    bricks = sorted(bricks, key=lambda brick: brick[0][2])
    max_coord = 1 + max(max(x_s, x_e, y_s, y_e) for (x_s, y_s, _), (x_e, y_e, _) in bricks)
    basis = {(x, y): (0, -1) for x in range(max_coord) for y in range(max_coord)}
    is_supported_by = [[] for _ in range(len(bricks))]
    for i, [(x_s, y_s, z_s), (x_e, y_e, z_e)] in enumerate(bricks):
        if x_s != x_e:
            z_max = max(basis[(x, y_e)][0] for x in range(x_s, x_e + 1))
            for x in range(x_s, x_e + 1):
                curr_z, base_id = basis[(x, y_e)]
                if curr_z == z_max and base_id not in is_supported_by[i]:
                    is_supported_by[i].append(base_id)
                basis[(x, y_e)] = (z_max + 1, i)
        elif y_s != y_e:
            z_max = max(basis[(x_e, y)][0] for y in range(y_s, y_e + 1))
            for y in range(y_s, y_e + 1):
                curr_z, base_id = basis[(x_e, y)]
                if curr_z == z_max and base_id not in is_supported_by[i]:
                    is_supported_by[i].append(base_id)
                basis[(x_e, y)] = (z_max + 1, i)
        else:
            is_supported_by[i].append(basis[(x_e, y_e)][1])
            curr_z, _ = basis[(x_s, y_s)]
            basis[(x_s, y_s)] = (curr_z + z_e - z_s + 1, i)
    return is_supported_by


def unsafe_bricks(is_supported_by):
    not_safe = [False] * len(is_supported_by)
    for tab in is_supported_by:
        if len(tab) == 1 and tab[0] != -1:
            not_safe[tab[0]] = True
    return not_safe


def build_support(is_supported_by):
    support = defaultdict(list)
    for i, tab in enumerate(is_supported_by):
        for neighbor in tab:
            if neighbor != -1:
                support[neighbor].append(i)
    return support


def count_fallen(start, support, is_supported_by):
    fallen = {start}
    q = deque([start])
    while q:
        brick = q.popleft()
        for brick_on in support[brick]:
            if brick_on not in fallen and all(b in fallen for b in is_supported_by[brick_on]):
                fallen.add(brick_on)
                q.append(brick_on)
    return len(fallen) - 1


def solve(lines, part="part_1"):
    bricks = parse_input(lines)
    is_supported_by = settle(bricks)
    not_safe = unsafe_bricks(is_supported_by)
    if part == "part_2":
        support = build_support(is_supported_by)
        return sum(count_fallen(i, support, is_supported_by) for i, ns in enumerate(not_safe) if ns)
    return len(bricks) - sum(not_safe)


def part_1(lines):
    return solve(lines)


def part_2(lines):
    return solve(lines, part="part_2")


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
