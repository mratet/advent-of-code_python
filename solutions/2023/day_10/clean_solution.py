from aocd import get_data

input = get_data(day=10, year=2023).splitlines()

# WRITE YOUR SOLUTION HERE
N, S, W, E = (0, -1), (0, 1), (-1, 0), (1, 0)

next_move_allowed = {
    "S": [S, E],  # S connects South and East for this input (equivalent to F)
    "|": [S, N],
    "-": [W, E],
    "J": [W, N],
    "F": [S, E],
    "7": [S, W],
    "L": [E, N],
}


def parse_input(lines):
    maze = {(x, y): c for y, line in enumerate(lines) for x, c in enumerate(line)}
    start_coord = next(co for co, v in maze.items() if v == "S")
    return maze, start_coord


def dfs(maze, start):
    stack = [start]
    visited = set()
    while stack:
        x, y = stack.pop()
        visited.add((x, y))
        for move in next_move_allowed[maze.get((x, y))]:
            nx, ny = x + move[0], y + move[1]
            if (nx, ny) not in visited:
                stack.append((nx, ny))
    return visited


def part_1(lines):
    maze, start = parse_input(lines)
    return len(dfs(maze, start)) // 2


def part_2(lines):
    maze, start = parse_input(lines)
    visited = dfs(maze, start)
    # Ray casting (horizontal scan): a point is inside if an odd number of loop borders are crossed.
    # Counting LJ| crossings (equivalent to counting F7|) — chosen because S is treated as F in this input.
    area = 0
    for y in range(len(lines)):
        border_count = 0
        for x in range(len(lines[0])):
            if (x, y) in visited and maze[(x, y)] in "LJ|":
                border_count += 1
            elif (x, y) not in visited and border_count % 2 == 1:
                area += 1
    return area


# END OF SOLUTION


print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
