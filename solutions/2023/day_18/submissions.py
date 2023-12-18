
lines = open('input.txt').read().splitlines()

# WRITE YOUR SOLUTION HERE
N, S, W, E = (0, -1), (0, 1), (-1, 0), (1, 0)
dir_dict = {
    'U': N,
    'D': S,
    'R': E,
    'L': W,
}

def corner_identification(maze, pose):
    x, y = pose
    N_symbol = (maze[y - 1][x] == '#')
    S_symbol = (maze[y + 1][x] == '#')
    E_symbol = (maze[y][x + 1] == '#')
    W_symbol = (maze[y][x - 1] == '#')

    return (N_symbol and S_symbol) or (N_symbol and E_symbol) or (N_symbol and W_symbol)



def part_1(lines):
    n, m = 500, 500
    plan = [['.' for _ in range(m)] for _ in range(n)]
    visited = set()
    pt = (250, 250)
    for line in lines:
        direction, distance, color = line.split()
        for _ in range(int(distance)):
            x, y = pt
            next_dir = dir_dict[direction]
            plan[y][x] = '#'
            visited.add((x, y))
            pt = (x + next_dir[0], y + next_dir[1])

    area = 0
    for y in range(n):
        border_count = 0
        for x in range(m):
            # From a horizontal analysis, we can choose either LJ| or F7|
            # I took LJ| because my starting tile is a F
            border_flag = (x, y) in visited
            if border_flag and corner_identification(plan, (x, y)):
                border_count += 1
            elif not border_flag and border_count % 2 == 1:
                area += 1

    return area + len(visited)


second_dir_dict = {
    '0': E,
    '1': N,
    '2': W,
    '3': S,
}

def shoelace_area(points):
    area = 0
    for i in range(len(points) - 1):
        area += points[i][0] * points[i + 1][1] - points[i + 1][0] * points[i][1]
    return area // 2

def part_2(lines):
    point = (0, 0)
    perimeter = 0
    points = [point]

    for line in lines:
        _, _, hexa = line.split()
        direction, distance = second_dir_dict[hexa[-2]], int(hexa[2:-2], 16)
        point = (point[0] + distance * direction[0], point[1] + distance * direction[1])
        perimeter += distance
        points.append(point)

    area = shoelace_area(points)

    return abs(area) + perimeter // 2 + 1
# END OF SOLUTION


test_input = open('input-test.txt').read().splitlines()
test_lines = []
for i, line in enumerate(test_input[3:]):
    if line[0] == '-':
        break
    test_lines.append(line)
solution = test_input[i + 4]

print(f'My answer on test set for the first problem is {part_1(test_lines)}')
print(solution)
print(f'My answer is {part_1(lines)}')

print(f'My answer on test set for the second problem is {part_2(test_lines)}')
print(f'My answer is {part_2(lines)}')
