import queue

lines = open("input.txt").read().splitlines()

# WRITE YOUR SOLUTION HERE
import collections


def _parse(input):
    maze = {(x, y): c for y, line in enumerate(input) for x, c in enumerate(line)}
    s_co = next(co for co, v in maze.items() if v == "S")

    return maze, s_co


def bfs(maze, start, nb):
    q = collections.deque()
    q.append(start)
    visited = set()

    for i in range(nb):
        visited.clear()
        for _ in range(len(q)):
            x, y = q.popleft()

            for move in (0, 1), (0, -1), (1, 0), (-1, 0):
                nx = x + move[0]
                ny = y + move[1]
                current_car = maze.get((nx, ny), "#")

                if current_car != "#" and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    q.append((nx, ny))

    return len(q)


def part_1(lines):
    maze, s_co = _parse(lines)
    for i in range(1000):
        print(bfs(maze, s_co, i))
    return 0


def part_2(lines):
    return 0


# END OF SOLUTION


test_input = open("input-test.txt").read().splitlines()
test_lines = []
for i, line in enumerate(test_input[3:]):
    if line[0] == "-":
        break
    test_lines.append(line)
solution = test_input[i + 4]

# print(f'My answer on test set for the first problem is {part_1(test_lines)}')
print(solution)
print(f"My answer is {part_1(lines)}")

print(f"My answer on test set for the second problem is {part_2(test_lines)}")
print(f"My answer is {part_2(lines)}")
