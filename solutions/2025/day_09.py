from itertools import product

from aocd import get_data

input = get_data(day=9, year=2025).splitlines()


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    coords = [list(map(int, line.split(","))) for line in lines]
    dists = []
    for (i1, c1), (i2, c2) in product(enumerate(coords), repeat=2):
        if i1 == i2 or i1 > i2:
            continue
        min_x, max_x = min(c1[0], c2[0]), max(c1[0], c2[0])
        min_y, max_y = min(c1[1], c2[1]), max(c1[1], c2[1])
        _dist = (max_x - min_x + 1) * (max_y - min_y + 1)
        dists.append(_dist)
    return max(dists)


def part_2(lines):
    coords = [list(map(int, line.split(","))) for line in lines]
    n = len(coords)
    edges = [(coords[i], coords[(i + 1) % n]) for i in range(n)]

    def is_inside_or_boundary(px, py):
        for (x1, y1), (x2, y2) in edges:
            if y1 == y2 and py == y1 and min(x1, x2) <= px <= max(x1, x2):
                return True
            if x1 == x2 and px == x1 and min(y1, y2) <= py <= max(y1, y2):
                return True

        crossings = sum(y1 == y2 and y1 > py and min(x1, x2) <= px < max(x1, x2) for (x1, y1), (x2, y2) in edges)
        return crossings % 2 == 1

    xs = sorted({x for x, _ in coords})
    ys = sorted({y for _, y in coords})
    W, H = len(xs), len(ys)

    grid = [[is_inside_or_boundary(xs[i], ys[j]) for i in range(W)] for j in range(H)]

    prefix = [[0] * (W + 1) for _ in range(H + 1)]
    for j in range(H):
        for i in range(W):
            prefix[j + 1][i + 1] = grid[j][i] + prefix[j][i + 1] + prefix[j + 1][i] - prefix[j][i]

    def rect_all_valid(gx1, gy1, gx2, gy2):
        total = (gx2 - gx1 + 1) * (gy2 - gy1 + 1)
        filled = prefix[gy2 + 1][gx2 + 1] - prefix[gy1][gx2 + 1] - prefix[gy2 + 1][gx1] + prefix[gy1][gx1]
        return filled == total

    best = 0
    for i1 in range(n):
        for i2 in range(i1 + 1, n):
            (x1, y1), (x2, y2) = coords[i1], coords[i2]
            x1, x2 = min(x1, x2), max(x1, x2)
            y1, y2 = min(y1, y2), max(y1, y2)

            gx1, gx2 = xs.index(x1), xs.index(x2)
            gy1, gy2 = ys.index(y1), ys.index(y2)

            if rect_all_valid(gx1, gy1, gx2, gy2):
                best = max(best, (x2 - x1 + 1) * (y2 - y1 + 1))

    return best


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
