import numpy as np
from aocd import get_data

input = get_data(day=21, year=2017).splitlines()


# WRITE YOUR SOLUTION HERE
START = np.array([[False, True, False], [False, False, True], [True, True, True]])


def get_next_pattern(current_pattern, mapping):
    h, _ = current_pattern.shape
    if h % 2 == 0:
        return apply_mapping(current_pattern, 2, mapping)
    return apply_mapping(current_pattern, 3, mapping)


def apply_mapping(array, block_size, mapping):
    h, w = array.shape
    mapped_size = block_size + 1
    mapped_blocks = np.zeros(((h // block_size) * mapped_size, (w // block_size) * mapped_size), dtype=array.dtype)
    for i in range(0, h, block_size):
        for j in range(0, w, block_size):
            block = array[i : i + block_size, j : j + block_size]
            out_row = (i // block_size) * mapped_size
            out_col = (j // block_size) * mapped_size
            mapped_blocks[out_row : out_row + mapped_size, out_col : out_col + mapped_size] = mapping[block.tobytes()]
    return mapped_blocks


def get_mapping(lines):
    mapping = {}
    for row in lines:
        in_pat, out_pat = row.split(" => ")
        in_pat = np.array([[char == "#" for char in line] for line in in_pat.strip().split("/")])
        out_pat = np.array([[char == "#" for char in line] for line in out_pat.strip().split("/")])
        for _ in range(4):
            mapping[in_pat.tobytes()] = out_pat
            mapping[np.fliplr(in_pat).tobytes()] = out_pat
            in_pat = np.rot90(in_pat)
    return mapping


def solve(lines, iterations):
    mapping = get_mapping(lines)
    pattern = START.copy()
    for _ in range(iterations):
        pattern = get_next_pattern(pattern, mapping)
    return pattern.sum()


def part_1(lines):
    return solve(lines, 5)


def part_2(lines):
    return solve(lines, 18)


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
