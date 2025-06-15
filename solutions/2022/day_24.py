from aocd import get_data
from collections import deque, defaultdict

DIRECTIONS = {">": (1, 0), "<": (-1, 0), "v": (0, 1), "^": (0, -1)}
MOVES = [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)]

input = get_data(day=24, year=2022).splitlines()
H, W = len(input), len(input[0])


def parse_input(lines):
    blizzards = defaultdict(list)
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c in DIRECTIONS:
                blizzards[c].append((x, y))
    return blizzards


def get_next_blizzard(blizzard):
    next_blizzard = defaultdict(list)
    for c, positions in blizzard.items():
        dx, dy = DIRECTIONS[c]
        for x, y in positions:
            nx, ny = x + dx, y + dy
            if dx:
                if nx == W - 1:
                    nx = 1
                elif nx == 0:
                    nx = W - 2
            if dy:
                if ny == H - 1:
                    ny = 1
                elif ny == 0:
                    ny = H - 2
            next_blizzard[c].append((nx, ny))
    return next_blizzard


def blizzard_state(blizzards):
    return tuple((c, tuple(sorted(blizzards[c]))) for c in sorted(blizzards))


def build_blizzard_states(blizzards):
    seen = set()
    state = blizzard_state(blizzards)
    states = []
    while state not in seen:
        seen.add(state)

        forbidden = set()
        for positions in blizzards.values():
            forbidden.update(positions)
        states.append(forbidden)

        blizzards = get_next_blizzard(blizzards)
        state = blizzard_state(blizzards)
    return states, len(states)


def build_graph(blizzard_states, cycle_length, start, end):
    graph = defaultdict(list)
    for t in range(cycle_length):
        forbidden_now = blizzard_states[t]
        forbidden_next = blizzard_states[(t + 1) % cycle_length]
        for y in range(H):
            for x in range(W):
                if (x, y) in forbidden_now:
                    continue
                for dx, dy in MOVES:
                    nx, ny = x + dx, y + dy
                    if (
                        (nx, ny) == start
                        or (nx, ny) == end
                        or (1 <= nx < W - 1 and 1 <= ny < H - 1)
                    ):
                        if (nx, ny) not in forbidden_next:
                            graph[(x, y, t)].append((nx, ny, (t + 1) % cycle_length))
    return graph


def bfs(graph, start, end, start_time, cycle_length):
    queue = deque()
    seen = set()
    t_mod = start_time % cycle_length
    queue.append((start[0], start[1], t_mod, start_time))
    seen.add((start[0], start[1], t_mod))

    while queue:
        x, y, t_mod, t_abs = queue.popleft()
        if (x, y) == end:
            return t_abs
        for nx, ny, next_t_mod in graph[(x, y, t_mod)]:
            state = (nx, ny, next_t_mod)
            if state not in seen:
                seen.add(state)
                queue.append((nx, ny, next_t_mod, t_abs + 1))
    return -1


def solve(lines, part):
    blizzards = parse_input(lines)
    start = (1, 0)
    end = (W - 2, H - 1)

    blizzard_states, cycle_length = build_blizzard_states(blizzards)
    graph = build_graph(blizzard_states, cycle_length, start, end)

    t1 = bfs(graph, start, end, 0, cycle_length)
    if part == "part_1":
        return t1
    t2 = bfs(graph, end, start, t1, cycle_length)
    t3 = bfs(graph, start, end, t2, cycle_length)
    return t3


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    return solve(lines, part="part_1")


def part_2(lines):
    return solve(lines, part="part_2")


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
