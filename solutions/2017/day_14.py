from functools import reduce
from operator import xor

from aocd import get_data

input = get_data(day=14, year=2017).splitlines()


# WRITE YOUR SOLUTION HERE
def knot_rounds(lengths, n=256):
    L = list(range(n))
    current_pos = 0
    for skip_size, length in enumerate(lengths):
        indices = [i % n for i in range(current_pos, current_pos + length)]
        values = reversed([L[i] for i in indices])
        for i, v in zip(indices, values, strict=False):
            L[i] = v
        current_pos = (current_pos + length + skip_size) % n
    return L


def knot_hash(word):
    length = [ord(c) for c in word] + [17, 31, 73, 47, 23]
    L = knot_rounds(64 * length)
    xor_hash = [reduce(xor, L[i : i + 16]) for i in range(0, 256, 16)]
    return "".join(f"{x:02x}" for x in xor_hash)


def dfs(x, y, squares, visited):
    visited.add((x, y))
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if (nx, ny) in squares and (nx, ny) not in visited:
            dfs(nx, ny, squares, visited)


def compute_connected_components(squares):
    nodes = set(squares)
    connected_components = []
    while nodes:
        visited = set()
        x, y = nodes.pop()
        dfs(x, y, squares, visited)
        connected_components.append(visited)
        nodes = nodes - visited
    return connected_components


def solve(lines, part="part_1"):
    word = lines[0]
    squares = {
        (i, j)
        for i in range(128)
        for j, b in enumerate(bin(int(knot_hash(f"{word}-{i}"), 16))[2:].zfill(128))
        if b == "1"
    }
    if part == "part_1":
        return len(squares)
    return len(compute_connected_components(squares))


def part_1(lines):
    return solve(lines, "part_1")


def part_2(lines):
    return solve(lines, "part_2")


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
