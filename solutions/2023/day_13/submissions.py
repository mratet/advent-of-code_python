lines = open("input.txt").read().splitlines()


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


def part_1(lines):
    patterns = []
    pattern = []
    for line in lines:
        if not line:
            cols = [
                "".join([pattern[i][j] for i in range(len(pattern))])
                for j in range(len(pattern[0]))
            ]
            patterns.append((pattern, cols))
            pattern = []
        else:
            pattern.append(line)

    # To add the last pattern if it has not been done before
    if pattern:
        cols = [
            "".join([pattern[i][j] for i in range(len(pattern))])
            for j in range(len(pattern[0]))
        ]
        patterns.append((pattern, cols))

    hor_reflec, vert_reflec = 0, 0
    for rows, cols in patterns:
        hor_reflec += check_mirrors(rows, 0)
        vert_reflec += check_mirrors(cols, 0)

    return hor_reflec * 100 + vert_reflec


def part_2(lines):
    patterns = []
    pattern = []
    for line in lines:
        if not line:
            cols = [
                "".join([pattern[i][j] for i in range(len(pattern))])
                for j in range(len(pattern[0]))
            ]
            patterns.append((pattern, cols))
            pattern = []
        else:
            pattern.append(line)

    # To add the last pattern if it has not been done before
    if pattern:
        cols = [
            "".join([pattern[i][j] for i in range(len(pattern))])
            for j in range(len(pattern[0]))
        ]
        patterns.append((pattern, cols))

    hor_reflec, vert_reflec = 0, 0
    for rows, cols in patterns:
        hor_reflec += check_mirrors(rows, 1)
        vert_reflec += check_mirrors(cols, 1)

    return hor_reflec * 100 + vert_reflec


# END OF SOLUTION


test_input = open("input-test.txt").read().splitlines()
test_lines = []
for i, line in enumerate(test_input[3:]):
    if line and line[0] == "-":
        break
    test_lines.append(line)
solution = test_input[i + 4]

print(f"My answer on test set for the first problem is {part_1(test_lines)}")
print(solution)
print(f"My answer is {part_1(lines)}")

print(f"My answer on test set for the second problem is {part_2(test_lines)}")
print(f"My answer is {part_2(lines)}")
