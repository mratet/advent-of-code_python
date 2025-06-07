from aocd import get_data

input = get_data(day=12, year=2022).splitlines()


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


def dfs(grid, start, end):
    distance = {start: 0}
    to_visit = [start]
    while to_visit:
        node = to_visit.pop(0)
        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            neigh_node = (node[0] + dx, node[1] + dy)
            if (
                neigh_node in grid
                and grid[neigh_node] <= grid[node] + 1
                and neigh_node not in distance
            ):
                distance[neigh_node] = distance[node] + 1
                to_visit.append(neigh_node)
    return distance.get(end, 1e9)


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    grid, start, end = parse_grid(lines)
    return dfs(grid, start, end)


def part_2(lines):
    grid, start, end = parse_grid(lines)
    starts = [node for node in grid if grid[node] == ord("a")]
    return min(dfs(grid, start, end) for start in starts)


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
