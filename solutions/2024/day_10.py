
from aocd import get_data

input = get_data(day=10, year=2024).splitlines()


# WRITE YOUR SOLUTION HERE
def iterative_dfs(start, lines, part):
    distinct_trails = 0
    endpoint = set()
    to_visit = [start]
    while to_visit:
        x, y = to_visit.pop(0)
        h = int(lines[x][y])
        if h == 9:
            endpoint.add((x, y))
            distinct_trails += 1
            continue
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if (
                0 <= nx < len(lines)
                and 0 <= ny < len(lines[0])
                and int(lines[nx][ny]) == h + 1
            ):
                to_visit.append((nx, ny))
    return len(endpoint) if part == "part_1" else distinct_trails


def part_1(lines):
    return sum(
        [
            iterative_dfs((x, y), lines, "part_1")
            for x in range(len(lines))
            for y in range(len(lines[0]))
            if lines[x][y] == "0"
        ]
    )


def part_2(lines):
    return sum(
        [
            iterative_dfs((x, y), lines, "part_2")
            for x in range(len(lines))
            for y in range(len(lines[0]))
            if lines[x][y] == "0"
        ]
    )


# def part_2(lines):
#     def dfs(start):
#         x, y = start
#         h = int(lines[x][y])
#         if h == 9:
#             return 1
#         return sum([dfs((x + dx, y + dy)) for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)] if 0 <= x + dx < len(lines) and 0 <= y + dy < len(lines[0]) and int(lines[x + dx][y + dy]) == h + 1])
#
#     score = 0
#     for x, line in enumerate(lines):
#         for y, char in enumerate(line):
#             if char == '0':
#                 score += dfs((x, y))
#     return score

# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
