from aocd import get_data

input = get_data(day=20, year=2024).splitlines()


# WRITE YOUR SOLUTION HERE
def generateManhattanPoint(x, y, R):
    points = []
    for r in range(1, R + 1):
        for offset in range(r):
            invOffset = r - offset  # Inverse offset
            points.append((x + offset, y + invOffset))
            points.append((x + invOffset, y - offset))
            points.append((x - offset, y - invOffset))
            points.append((x - invOffset, y + offset))
    return points


def dist_dfs(lines, S):
    dist = {}
    dist_count = 0
    points = [S]
    while points:
        (x, y) = points.pop()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if lines[nx][ny] != "#" and (nx, ny) not in dist:
                points.append((nx, ny))
                dist[(nx, ny)] = dist_count
        dist_count += 1
    return dist


def solve(lines, part):
    cheat_time = 2 if part == "part_1" else 20
    S = [
        (x, y)
        for x in range(len(lines))
        for y in range(len(lines[0]))
        if lines[x][y] == "S"
    ][0]
    start_pos = [
        (x, y)
        for x in range(len(lines))
        for y in range(len(lines[0]))
        if lines[x][y] != "#"
    ]
    dist = dist_dfs(lines, S)
    scores = []
    for node in start_pos:
        cheats = generateManhattanPoint(*node, cheat_time)
        for point in cheats:
            dist_point = abs(point[0] - node[0]) + abs(point[1] - node[1])
            if point in dist and dist[point] + dist_point < dist[node]:
                scores.append(dist[node] - dist[point] - dist_point)
    return sum(c >= 100 for c in scores)


def part_1(lines):
    return solve(lines, "part_1")


def part_2(lines):
    return solve(lines, "part_2")


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
