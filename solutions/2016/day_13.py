import itertools, re, collections
from aocd import get_data

input = int(get_data(day=13, year=2016))


def is_a_wall(coord, fav_num):
    x, y = coord
    i = x * x + 3 * x + 2 * x * y + y + y * y + fav_num
    return i.bit_count() % 2 == 1


def solve(input, part="part_1"):
    start = (1, 1)
    q = collections.deque()
    q.append(start)
    visited = set()
    cnt = 0

    while q:
        for _ in range(len(q)):
            x, y = q.popleft()
            if (x, y) in visited:
                continue
            visited.add((x, y))

            if part == "part_1" and (x, y) == (31, 39):
                return cnt

            for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy

                if 0 <= nx and 0 <= ny and not is_a_wall((nx, ny), input):
                    q.append((nx, ny))
        cnt += 1
        if part == "part_2" and cnt == 51:
            return len(visited)


def part_1(input):
    return solve(input, "part_1")


def part_2(input):
    return solve(input, "part_2")


print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
