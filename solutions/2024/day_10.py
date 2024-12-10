from collections import defaultdict

from aocd import get_data, submit
input = get_data(day=10, year=2024).splitlines()

# WRITE YOUR SOLUTION HERE
def part_1(lines):

    def dfs(start):
        score = 0
        to_visit = [start]
        seen = set()
        while to_visit:
            x, y, h = to_visit.pop(0)
            if h == 9:
                seen.add((x, y, h))
                score += 1
                continue
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(lines) and 0 <= ny < len(lines[0]) and int(lines[nx][ny]) == h + 1 and (
                nx, ny, h + 1) not in seen:
                    seen.add((nx, ny, h + 1))
                    to_visit.append((nx, ny, h + 1))
        return score

    score = 0
    for x, line in enumerate(lines):
        for y, char in enumerate(line):
            if char == '0':
                score += dfs((x, y, 0))
    return score

def part_2(lines):
    def dfs(start):
        x, y = start
        h = int(lines[x][y])
        if h == 9:
            return 1
        return sum([dfs((x + dx, y + dy)) for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)] if 0 <= x + dx < len(lines) and 0 <= y + dy < len(lines[0]) and int(lines[x + dx][y + dy]) == h + 1])

    score = 0
    for x, line in enumerate(lines):
        for y, char in enumerate(line):
            if char == '0':
                score += dfs((x, y))
    return score

# END OF SOLUTION
print(f'My answer is {part_1(input)}')
print(f'My answer is {part_2(input)}')
