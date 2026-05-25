from collections import deque

from aocd import get_data

input = get_data(day=12, year=2022).splitlines()


# WRITE YOUR SOLUTION HERE
def parse_grid(lines):
    grid = {}
    for y, line in enumerate(lines):
        for x, item in enumerate(line):
            if item == "S":
                start = (x, y)
                item = "a"
            elif item == "E":
                end = (x, y)
                item = "z"
            grid[(x, y)] = ord(item)
    return grid, start, end


def bfs(grid, start, end):
    distance = {start: 0}
    to_visit = deque([start])
    while to_visit:
        node = to_visit.popleft()
        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            neigh = (node[0] + dx, node[1] + dy)
            if neigh in grid and grid[neigh] <= grid[node] + 1 and neigh not in distance:
                distance[neigh] = distance[node] + 1
                to_visit.append(neigh)
    return distance.get(end, 1e9)


def solve(lines, part="part_1"):
    grid, start, end = parse_grid(lines)
    if part == "part_1":
        return bfs(grid, start, end)
    return min(bfs(grid, s, end) for s in grid if grid[s] == ord("a"))


def part_1(lines):
    return solve(lines)


def part_2(lines):
    return solve(lines, "part_2")


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
