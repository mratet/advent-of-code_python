lines = open("input.txt").read().splitlines()

# WRITE YOUR SOLUTION HERE

next_move_allowed = {
    "S": [
        (1, 0),
        (0, 1),
    ],  # [(0, 1), (0, -1), (1, 0), (-1, 0)] we use a F to debug here
    "|": [(0, 1), (0, -1)],
    "-": [(-1, 0), (1, 0)],
    "J": [(-1, 0), (0, -1)],
    "F": [(1, 0), (0, 1)],
    "7": [(0, 1), (-1, 0)],
    "L": [(0, -1), (1, 0)],
}


def part_1(lines):
    maze = {(x, y): c for y, line in enumerate(lines) for x, c in enumerate(line)}

    s_co = next(co for co, v in maze.items() if v == "S")
    q = [s_co]
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

    return len(visited) / 2


def part_2(lines):
    maze = {(x, y): c for y, line in enumerate(lines) for x, c in enumerate(line)}

    s_co = next(co for co, v in maze.items() if v == "S")
    q = [s_co]
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

    area = 0
    n, m = len(lines), len(lines[0])
    for y in range(n):
        border_count = 0
        for x in range(m):
            # From a horizontal analysis, we can choose either LJ| or F7|
            # I took LJ| because my starting tile is F
            border_flag = (x, y) in visited
            if border_flag and maze[(x, y)] in "LJ|":
                border_count += 1

            elif not border_flag and border_count % 2 == 1:
                area += 1

    return area


# END OF SOLUTION


test_input = open("input-test.txt").read().splitlines()
test_lines = []
for i, line in enumerate(test_input[3:]):
    if line[0] == "-":
        break
    test_lines.append(line)
solution = test_input[i + 4]

print(f"My answer on test set for the first problem is {part_1(test_lines)}")
print(solution)
print(f"My answer is {part_1(lines)}")

print(f"My answer on test set for the second problem is {part_2(test_lines)}")
print(f"My answer is {part_2(lines)}")
