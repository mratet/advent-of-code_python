lines = open("input.txt").read().splitlines()

# WRITE YOUR SOLUTION HERE


def galaxie_distance(g1, g2, row_expands, col_expands, expand):
    x1, y1 = g1
    x2, y2 = g2
    x_max, x_min = max(x1, x2), min(x1, x2)
    y_max, y_min = max(y1, y2), min(y1, y2)

    row_expansion = len([1 for y in row_expands if y_min < y < y_max])
    col_expansion = len([1 for x in col_expands if x_min < x < x_max])

    return abs(x_max - x_min + (expand - 1) * row_expansion) + abs(
        y_max - y_min + (expand - 1) * col_expansion
    )


def part_1(lines):
    galaxies = [
        (x, y) for y, line in enumerate(lines) for x, c in enumerate(line) if c == "#"
    ]

    n, m = len(lines), len(lines[0])
    empty_row = list(set(range(m)) - set([g[1] for g in galaxies]))
    empty_col = list(set(range(n)) - set([g[0] for g in galaxies]))

    expansion = 2

    ans = 0

    for gi in galaxies:
        for gj in galaxies:
            ans += galaxie_distance(gi, gj, empty_row, empty_col, expansion)

    return ans // 2


def part_2(lines):
    galaxies = [
        (x, y) for y, line in enumerate(lines) for x, c in enumerate(line) if c == "#"
    ]

    n, m = len(lines), len(lines[0])
    empty_row = list(set(range(m)) - set([g[1] for g in galaxies]))
    empty_col = list(set(range(n)) - set([g[0] for g in galaxies]))

    expansion = 1e6

    ans = 0

    for gi in galaxies:
        for gj in galaxies:
            ans += galaxie_distance(gi, gj, empty_row, empty_col, expansion)

    return ans // 2


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
