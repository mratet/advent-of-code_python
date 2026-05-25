from collections import deque

from aocd import get_data

input = get_data(day=20, year=2024).splitlines()


# WRITE YOUR SOLUTION HERE
def bfs_distances(lines, start):
    dist = {start: 0}
    queue = deque([start])
    while queue:
        node = queue.popleft()
        row, col = node
        for d_row, d_col in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            n_row, n_col = row + d_row, col + d_col
            neighbor = (n_row, n_col)
            if neighbor not in dist and lines[n_row][n_col] != "#":
                dist[neighbor] = dist[node] + 1
                queue.append(neighbor)
    return dist


def manhattan_neighbors(row, col, max_dist):
    for cheat_dist in range(1, max_dist + 1):
        for d_row in range(-cheat_dist, cheat_dist + 1):
            d_col_abs = cheat_dist - abs(d_row)
            yield row + d_row, col + d_col_abs, cheat_dist
            if d_col_abs != 0:
                yield row + d_row, col - d_col_abs, cheat_dist


def solve(lines, part="part_1"):
    cheat_time = 2 if part == "part_1" else 20
    start = next((row, col) for row in range(len(lines)) for col in range(len(lines[0])) if lines[row][col] == "S")
    dist = bfs_distances(lines, start)
    count = 0
    for (row, col), node_dist in dist.items():
        for n_row, n_col, cheat_dist in manhattan_neighbors(row, col, cheat_time):
            neighbor = (n_row, n_col)
            if neighbor in dist and node_dist - dist[neighbor] - cheat_dist >= 100:
                count += 1
    return count


def part_1(lines):
    return solve(lines)


def part_2(lines):
    return solve(lines, "part_2")


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
