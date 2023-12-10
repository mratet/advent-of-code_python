
lines = open('input.txt').read().splitlines()

# WRITE YOUR SOLUTION HERE

next_move_allowed = {
    (1, 0): "-7J",
    (-1, 0): "-FL",
    (0, -1): "|F7",  # The maze is reversed on the y-axis
    (0, 1): "|LJ"
}

def part_1(lines):
    maze = {
        (x, y): c
        for y, line in enumerate(lines)
        for x, c in enumerate(line)
    }

    s_co = next(co for co, v in maze.items() if v == 'S')
    print(s_co)
    q = [s_co]
    visited = []

    while q:
        x, y = q.pop()
        visited.append((x, y))
        for move, char_allowed in next_move_allowed.items():
            nx = x + move[0]
            ny = y + move[1]
            next_move = maze.get((nx, ny), ".")

            if next_move in char_allowed and (nx, ny) not in visited:
                q.append((nx, ny))

    return (len(visited) - 1) // 2


def part_2(lines):
    return 0
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
