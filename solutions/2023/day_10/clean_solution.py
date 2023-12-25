from aocd import get_data
input = get_data(day=10, year=2023).splitlines()

# WRITE YOUR SOLUTION HERE
N, S, W, E = (0, -1), (0, 1), (-1, 0), (1, 0)

next_move_allowed = {
    "S": [S, E], # [(0, 1), (0, -1), (1, 0), (-1, 0)] we use a F to debug here
    "|": [S, N],
    "-": [W, E],
    "J": [W, N],
    "F": [S, E],
    "7": [S, W],
    "L": [E, N]
}


def _parse(input):

    maze = {
        (x, y): c
        for y, line in enumerate(input)
        for x, c in enumerate(line)
    }
    s_co = next(co for co, v in maze.items() if v == 'S')

    return maze, s_co

def dfs(maze, start):

    q = [start]
    visited = set()

    while q:
        x, y = q.pop()
        current_car = maze.get((x, y))
        visited.add((x, y))

        for move in next_move_allowed[current_car]:
            nx = x + move[0]
            ny = y + move[1]

            if (nx, ny) not in visited:
                q.append((nx, ny))

    return visited

def part_1(lines):

    maze, s_co = _parse(lines)
    visited = dfs(maze, s_co)

    return len(visited) // 2


def part_2(lines):

    maze, s_co = _parse(lines)
    visited = dfs(maze, s_co)

    area = 0
    n, m = len(lines), len(lines[0])
    for y in range(n):
        border_count = 0
        for x in range(m):
            # From a horizontal analysis, we can choose either LJ| or F7|
            # I took LJ| because my starting tile is a F
            border_flag = (x, y) in visited
            if border_flag and maze[(x, y)] in "LJ|":
                border_count += 1
            elif not border_flag and border_count % 2 == 1:
                area += 1

    return area
# END OF SOLUTION


print(f'My answer is {part_1(input)}')
print(f'My answer is {part_2(input)}')
