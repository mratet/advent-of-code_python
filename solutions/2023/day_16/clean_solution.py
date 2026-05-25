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


def build_graph(contraption):
    n, m = len(contraption), len(contraption[0])
    graph = {}
    for y in range(n):
        for x in range(m):
            for direction in [N, S, E, W]:
                nexts = []
                for new_dir in next_direction[contraption[y][x]][direction]:
                    nx, ny = x + new_dir[0], y + new_dir[1]
                    if 0 <= ny < n and 0 <= nx < m:
                        nexts.append(((nx, ny), new_dir))
                graph[((x, y), direction)] = nexts
    return graph


def solve(graph, start):
    stack, visited = [start], set()
    while stack:
        state = stack.pop()
        if state in visited:
            continue
        visited.add(state)
        stack.extend(graph[state])
    return len({pos for pos, _ in visited})


def part_1(contraption):
    graph = build_graph(contraption)
    return solve(graph, ((0, 0), E))


def part_2(contraption):
    n, m = len(contraption), len(contraption[0])
    graph = build_graph(contraption)
    starts = (
        [((0, i), E) for i in range(n)]
        + [((m - 1, i), W) for i in range(n)]
        + [((j, 0), S) for j in range(m)]
        + [((j, n - 1), N) for j in range(m)]
    )
    return max(solve(graph, start) for start in starts)


# END OF SOLUTION


print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
