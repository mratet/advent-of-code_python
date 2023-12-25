from aocd import get_data
input = get_data(day=13, year=2023).splitlines()

# WRITE YOUR SOLUTION HERE
def check_mirrors(tab, mismatched):
    n, i, index = len(tab), 0, 0
    cnt = 0

    while index < n - 1:
        while 0 <= index - i and index + i + 1 <= n - 1:
            cnt += sum([x != y for x, y in zip(tab[index + 1 + i], tab[index - i])])
            i += 1

        if cnt == mismatched:
            return index + 1

        index += 1
        i = 0
        cnt = 0

    return 0

def _parse(input):
    patterns, pattern = [], []

    for line in input:
        if not line:
            cols = [''.join([pattern[i][j] for i in range(len(pattern))]) for j in range(len(pattern[0]))]
            patterns.append((pattern, cols))
            pattern = []
        else:
            pattern.append(line)

    if pattern:
        cols = [''.join([pattern[i][j] for i in range(len(pattern))]) for j in range(len(pattern[0]))]
        patterns.append((pattern, cols))

    return patterns


def part_1(lines):
    patterns = _parse(lines)
    hor_reflec = sum([check_mirrors(rows, 0) for rows, _ in patterns])
    vert_reflec = sum([check_mirrors(cols, 0) for _, cols in patterns])

    return hor_reflec * 100 + vert_reflec


def part_2(lines):
    patterns = _parse(lines)
    hor_reflec = sum([check_mirrors(rows, 1) for rows, _ in patterns])
    vert_reflec = sum([check_mirrors(cols, 1) for _, cols in patterns])

    return hor_reflec * 100 + vert_reflec

# END OF SOLUTION


print(f'My answer is {part_1(input)}')
print(f'My answer is {part_2(input)}')
