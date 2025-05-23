from aocd import get_data

input = get_data(day=21, year=2023).splitlines()

# WRITE YOUR SOLUTION HERE
import collections


def _parse(input):
    maze = {(x, y): c for y, line in enumerate(input) for x, c in enumerate(line)}
    s_co = next(co for co, v in maze.items() if v == "S")

    return maze, s_co


def bfs(maze, start, nb):
    q = collections.deque()
    n = 1 + max(maze.keys())[0]

    q.append(start)
    visited = set()

    for i in range(nb):
        visited.clear()
        for _ in range(len(q)):
            x, y = q.popleft()

            for move in (0, 1), (0, -1), (1, 0), (-1, 0):
                nx = x + move[0]
                ny = y + move[1]
                current_car = maze.get((nx % n, ny % n), "#")

                if current_car != "#" and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    q.append((nx, ny))

    return len(q)


def part_1(lines):
    maze, s_co = _parse(lines)
    return bfs(maze, s_co, 64)


def part_2(lines):
    maze, s_co = _parse(lines)
    size = 1 + max(maze.keys())[0]

    steps = 26501365
    x = steps % (2 * size)
    values = []

    while True:
        values.append((bfs(maze, s_co, x)))
        if len(values) == 3:
            break
        x += 2 * size
    # Extrapolation to a second degree polynom
    a = 0.5 * (values[2] - 2 * values[1] + values[0])
    c = values[0]
    b = values[1] - a - c

    def f(x):
        return a * x**2 + b * x + c

    return f(steps // (2 * size))


# END OF SOLUTION


print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
