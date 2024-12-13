from aocd import get_data, submit
input = get_data(day=12, year=2024).splitlines()

# WRITE YOUR SOLUTION HERE
def count_corner(lines, start):
    x, y = start
    side = 0
    for (dx1, dy1), (dx2, dy2) in zip([(1, 0), (0, -1), (-1, 0), (0, 1)], [(0, -1), (-1, 0), (0, 1), (1, 0)]):
        nx1, ny1 = x + dx1, y + dy1
        nx2, ny2 = x + dx2, y + dy2
        if (nx1 < 0) or (nx1 >= len(lines)) or (ny1 < 0) or (ny1 >= len(lines[0])): continue
        if (nx2 < 0) or (nx2 >= len(lines)) or (ny2 < 0) or (ny2 >= len(lines[0])): continue
        dxa = dx1 if dx1 else dx2
        dya = dy1 if dy1 else dy2
        nxa, nya = x + dxa, y + dya
        if lines[nx1][ny1] == lines[x][y] and lines[nx2][ny2] == lines[x][y] and lines[nxa][nya] != lines[x][y]:
            side += 1
    return side


def dfs(lines, start):
    x, y = start
    color = lines[x][y]
    garden = {(x, y)}
    to_visit = [start]
    perimeter = 0
    side = 0
    while to_visit:
        x, y = to_visit.pop(0)
        neigh = []
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(lines) and 0 <= ny < len(lines[0]) and lines[nx][ny] == color:
                neigh.append((dx, dy))
                if (nx, ny) not in garden:
                    garden.add((nx, ny))
                    to_visit.append((nx, ny))
            else:
                perimeter += 1
        if len(neigh) == 1:
            side += 2
            continue
        if len(neigh) == 2:
            (dx1, dy1), (dx2, dy2) = neigh
            if dx1 != dx2 and dy1 != dy2:
                side += 1
        side += count_corner(lines, (x, y))
    if len(garden) == 1:
        side = 4
    return garden, perimeter, side

def part_1(lines):
    score = 0
    seen = set()
    for x in range(len(lines)):
        for y in range(len(lines[0])):
            if (x, y) not in seen:
                garden, p, _ = dfs(lines, (x, y))
                score += len(garden) * p
                seen.update(garden)
    return score

def part_2(lines):
    score = 0
    seen = set()
    for x in range(len(lines)):
        for y in range(len(lines[0])):
            if (x, y) not in seen:
                garden, _ , s= dfs(lines, (x, y))
                score += len(garden) * s
                seen.update(garden)
    return score

# END OF SOLUTION
print(f'My answer is {part_1(input)}')
print(f'My answer is {part_2(input)}')
