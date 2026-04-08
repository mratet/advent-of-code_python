import collections

from aocd import get_data

input = get_data(day=13, year=2016)

FAV_NUMBER = int(input)


def is_a_wall(coord):
    x, y = coord
    i = x * x + 3 * x + 2 * x * y + y + y * y + FAV_NUMBER
    return i.bit_count() % 2 == 1


def is_valid(x, y):
    return x >= 0 and y >= 0 and not is_a_wall((x, y))


def bfs(stop_condition):
    start = (1, 1)
    queue = collections.deque([(start, 0)])
    visited = {start: 0}

    while queue:
        (x, y), distance = queue.popleft()
        if stop_condition(x, y, distance, visited):
            return visited, distance
        for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if (nx, ny) not in visited and is_valid(nx, ny):
                visited[(nx, ny)] = distance + 1
                queue.append(((nx, ny), distance + 1))
    return visited, -1


def part_1(input):
    _, distance = bfs(lambda x, y, d, v: (x, y) == (31, 39))
    return distance


def part_2(input):
    visited, _ = bfs(lambda x, y, d, v: d == 50)
    return len(visited)


print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
