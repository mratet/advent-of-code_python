from aocd import get_data

input = get_data(day=22, year=2023).splitlines()

from collections import deque, defaultdict


def parse_input(lines):
    bricks = []
    for line in lines:
        start, end = line.split("~")
        start = [int(c) for c in start.split(",")]
        end = [int(c) for c in end.split(",")]
        bricks.append([start, end])
    return bricks


def get_is_supported_by_dict(bricks):
    bricks = sorted(bricks, key=lambda brick: brick[0][2])
    len_basis = 10
    basis = {(x, y): (0, -1) for x in range(len_basis) for y in range(len_basis)}

    is_supported_by = [[] for _ in range(len(bricks))]

    for i, [(x_s, y_s, z_s), (x_e, y_e, z_e)] in enumerate(bricks):
        if x_s != x_e:
            z_max = max([basis[(x, y_e)][0] for x in range(x_s, x_e + 1)])
            for x in range(x_s, x_e + 1):
                curr_z, base_id = basis[(x, y_e)]
                if curr_z == z_max and base_id not in is_supported_by[i]:
                    is_supported_by[i].append(base_id)
                basis[(x, y_e)] = (z_max + 1, i)
        elif y_s != y_e:
            z_max = max([basis[(x_e, y)][0] for y in range(y_s, y_e + 1)])
            for y in range(y_s, y_e + 1):
                curr_z, base_id = basis[(x_e, y)]
                if curr_z == z_max and base_id not in is_supported_by[i]:
                    is_supported_by[i].append(base_id)
                basis[(x_e, y)] = (z_max + 1, i)
        else:  # z_s != z_e
            is_supported_by[i].append(basis[(x_e, y_e)][1])
            curr_z, _ = basis[(x_s, y_s)]
            basis[(x_s, y_s)] = (curr_z + z_e - z_s + 1, i)

    return is_supported_by


def get_unsafe_brick(is_supported_by):
    not_safe = [False for _ in range(len(is_supported_by))]
    for tab in is_supported_by:
        if len(tab) == 1 and tab[0] != -1:
            not_safe[tab[0]] = True
    return not_safe


def compute_support(is_supported_by):
    support = defaultdict(list)
    for i, tab in enumerate(is_supported_by):
        for neighboor in tab:
            if neighboor != -1:
                support[neighboor].append(i)
    return support


def fallen_bricks(start, support, is_supported_by):
    fallen_bricks = set()
    q = deque()
    q.append(start)

    while q:
        brick = q.popleft()
        fallen_bricks.add(brick)

        for brick_on in support[brick]:
            if brick_on in fallen_bricks:
                continue
            if all(b in fallen_bricks for b in is_supported_by[brick_on]):
                q.append(brick_on)

    return len(fallen_bricks) - 1


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    bricks = parse_input(lines)
    is_supported_by = get_is_supported_by_dict(bricks)
    not_safe = get_unsafe_brick(is_supported_by)
    return len(bricks) - sum(not_safe)


def part_2(input):
    bricks = parse_input(input)
    is_supported_by = get_is_supported_by_dict(bricks)
    not_safe = get_unsafe_brick(is_supported_by)
    support = compute_support(is_supported_by)
    return sum(
        fallen_bricks(i, support, is_supported_by)
        for i, not_safe_bool in enumerate(not_safe)
        if not_safe_bool
    )


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
