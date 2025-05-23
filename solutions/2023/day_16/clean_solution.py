from aocd import get_data

input = get_data(day=16, year=2023).splitlines()

# WRITE YOUR SOLUTION HERE
W, E, S, N = (-1, 0), (1, 0), (0, 1), (0, -1)

next_direction = {
    ".": {S: [S], N: [N], W: [W], E: [E]},
    "|": {S: [S], N: [N], W: [S, N], E: [S, N]},
    "-": {W: [W], E: [E], N: [E, W], S: [E, W]},
    "\\": {E: [S], W: [N], S: [E], N: [W]},
    "/": {E: [N], W: [S], S: [W], N: [E]},
}


def solve(contraption, start):
    n, m = len(contraption), len(contraption[0])
    q = [start]
    visited = set()

    while q:
        (x, y), dir = q.pop()
        visited.add(((x, y), dir))
        c = contraption[y][x]

        for new_dir in next_direction[c][dir]:
            nx = x + new_dir[0]
            ny = y + new_dir[1]

            if 0 <= ny < n and 0 <= nx < m and ((nx, ny), new_dir) not in visited:
                q.append(((nx, ny), new_dir))

    return len(set((x, y) for (x, y), _ in visited))


def part_1(contraption):
    return solve(contraption, ((0, 0), E))


def part_2(contraption):
    n, m = len(contraption), len(contraption[0])
    west_start = max([solve(contraption, ((0, i), E)) for i in range(n)])
    east_start = max([solve(contraption, ((m - 1, i), W)) for i in range(n)])
    north_start = max([solve(contraption, ((j, 0), S)) for j in range(m)])
    south_start = max([solve(contraption, ((j, n - 1), N)) for j in range(m)])

    return max(west_start, east_start, north_start, south_start)


# END OF SOLUTION


print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
