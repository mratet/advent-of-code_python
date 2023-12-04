import re
import itertools

lines = open('input.txt', 'r').readlines()


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    symbols = '*=/@#$%&+-'
    n, m = len(lines), len(lines[0])
    matrix = [['.' for _ in range(n)] for _ in range(m)]
    for i in range(n):
        for j in range(m):
            if lines[i][j] in symbols:
                for a in (-1, 0, 1):
                    for b in (-1, 0, 1):
                        if (0 <= i + a <= m-1) and (0 <= j + b <= n-1):
                            matrix[i+a][j+b] = '*'
    ans = 0
    num = ''
    flag = False
    for i in range(n):
        for j in range(m):

            if lines[i][j].isnumeric():
                num += lines[i][j]
                if matrix[i][j] == '*':
                    flag = True
            else:
                if flag:
                    ans += int(num)
                num = ''
                flag = False
    return ans

# Second part taken from TurtleSmoke's github
def part_2(lines):
    symbols, numbers = {}, []

    for i, line in enumerate(lines):
        m = re.finditer(r"(\d+)|([^.])", line)
        for match in m:
            if match.group().isdigit():
                numbers.append((int(match.group()), set((i, j) for j in range(*match.span()))))
            else:
                symbols[(i, match.start())] = match.group()

    get_neighbors = lambda x, y: {(x + i, y + j) for i, j in itertools.product((-1, 0, 1), repeat=2)}

    gears = {coord for coord, symbol in symbols.items() if symbol == "*"}
    gears_neighbors = [[n for n, coords in numbers if any(get_neighbors(*gear) & coords)] for gear in gears]

    res2 = sum(gears_ratio[0] * gears_ratio[1] for gears_ratio in gears_neighbors if len(gears_ratio) == 2)
    return res2


# END OF SOLUTION


test_input = open('input-test.txt').read().split("\n")
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
