import collections

from aocd import get_data

input = get_data(day=21, year=2023).splitlines()

# WRITE YOUR SOLUTION HERE


def parse_input(lines):
    maze = {(x, y): c for y, line in enumerate(lines) for x, c in enumerate(line)}
    start = next(co for co, v in maze.items() if v == "S")
    return maze, start


def bfs_distances(maze, start, max_nb, n):
    dist = {start: 0}
    q = collections.deque([start])
    while q:
        x, y = q.popleft()
        if dist[(x, y)] >= max_nb:
            continue
        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            nx, ny = x + dx, y + dy
            if (nx, ny) not in dist and maze.get((nx % n, ny % n)) != "#":
                dist[(nx, ny)] = dist[(x, y)] + 1
                q.append((nx, ny))
    return dist


def count_at(dist, nb):
    return sum(1 for d in dist.values() if d <= nb and d % 2 == nb % 2)


def part_1(lines):
    maze, start = parse_input(lines)
    n = len(lines)
    return count_at(bfs_distances(maze, start, 64, n), 64)


def part_2(lines):
    maze, start = parse_input(lines)
    n = len(lines)
    steps = 26501365
    # f(steps % size + k*size) is quadratic in k: each extra size steps adds one full ring
    # of tiles, whose area grows linearly, so the cumulative count grows quadratically.
    # size = 2*n (not n) because n=131 is odd: adding n steps flips parity, so the three
    # sample points must be spaced 2n apart to stay on the same parity as steps=26501365.
    size = 2 * n
    targets = [steps % size + i * size for i in range(3)]
    dist = bfs_distances(maze, start, targets[-1], n)
    values = [count_at(dist, nb) for nb in targets]
    a = (values[2] - 2 * values[1] + values[0]) // 2
    c = values[0]
    b = values[1] - a - c
    x = steps // size
    return a * x**2 + b * x + c


# END OF SOLUTION


print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
