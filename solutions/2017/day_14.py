from functools import reduce
from operator import xor

from aocd import get_data, submit

input = get_data(day=14, year=2017).splitlines()


# WRITE YOUR SOLUTION HERE
def rotation_step(lengths):
    L = list(range(256))
    current_pos, skip_size = 0, 0
    for l in lengths:
        if l > len(L):
            continue
        if current_pos + l < len(L):
            L[current_pos : current_pos + l] = list(
                reversed(L[current_pos : current_pos + l])
            )
        else:
            l1, r1 = current_pos, len(L)
            l2, r2 = 0, l - (len(L) - current_pos)
            R = list(reversed(L[l1:r1] + L[l2:r2]))
            C = r1 - l1
            L[l1:r1], L[l2:r2] = R[:C], R[C:]
        current_pos = (current_pos + l + skip_size) % len(L)
        skip_size = (skip_size + 1) % len(L)
    return L


def knot_hash(word):
    length = [ord(c) for c in word] + [17, 31, 73, 47, 23]
    L = rotation_step(64 * length)
    xor_hash = [reduce(xor, L[i : i + 16]) for i in range(0, 256, 16)]
    return "".join([hex(x)[2:].zfill(2) for x in xor_hash])


def part_1(lines):
    word = lines[0]
    ans = 0
    for i in range(128):
        hash_input = f"{word}-{i}"
        for c in knot_hash(hash_input):
            binary_c = bin(int("0x" + c, 16))[2:].zfill(4)
            ans += binary_c.count("1")
    return ans


def compute_connected_components(squares):
    nodes = set(squares)
    connected_components = []
    while nodes:
        visited = set()

        def dfs(node):
            visited.add(node)
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = node[0] + dx, node[1] + dy
                if (nx, ny) in squares and (nx, ny) not in visited:
                    dfs((nx, ny))

        N = nodes.pop()
        dfs(N)
        connected_components.append(visited)
        nodes = nodes - visited
    return connected_components


def part_2(lines):
    word = lines[0]
    squares = set()
    for i in range(128):
        hash_input = f"{word}-{i}"
        for j, c in enumerate(knot_hash(hash_input)):
            binary_c = bin(int("0x" + c, 16))[2:].zfill(4)
            for k, b in enumerate(binary_c):
                if b == "1":
                    squares.add((i, 4 * j + k))
    cc = compute_connected_components(squares)
    return len(cc)


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
