lines = open("input.txt").read().splitlines()

# WRITE YOUR SOLUTION HERE
L, R, U, D = (-1, 0), (1, 0), (0, 1), (0, -1)

next_direction = {
    ".": {U: [U], D: [D], L: [L], R: [R]},
    "|": {U: [U], D: [D], L: [U, D], R: [U, D]},
    "-": {L: [L], R: [R], D: [R, L], U: [R, L]},
    "\\": {R: [U], L: [D], U: [R], D: [L]},
    "/": {R: [D], L: [U], U: [L], D: [R]},
}


def solve(contraption, start):
    n, m = len(contraption), len(contraption[0])
    q = [start]
    visited = []

    while q:
        (x, y), dir = q.pop()
        visited.append(((x, y), dir))
        c = contraption[y][x]

        for new_dir in next_direction[c][dir]:
            nx = x + new_dir[0]
            ny = y + new_dir[1]

            if 0 <= ny < n and 0 <= nx < m and ((nx, ny), new_dir) not in visited:
                q.append(((nx, ny), new_dir))

    ans = 0
    maze = [["." for _ in range(m)] for j in range(n)]
    for (x, y), dir in visited:
        if maze[y][x] == ".":
            maze[y][x] = "#"
            ans += 1

    return ans


def part_1(contraption):
    return solve(contraption, ((0, 0), R))


def part_2(lines):
    n, m = len(lines), len(lines[0])
    start = []
    for i in range(n):
        start.append(((0, i), R))
        start.append(((m - 1, i), L))
    for j in range(m):
        start.append(((j, 0), U))
        start.append(((j, n - 1), D))

    ans = 0
    for starting_pos in start:
        ans = max(ans, solve(lines, starting_pos))

    return ans


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
