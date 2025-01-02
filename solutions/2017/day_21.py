from aocd import get_data, submit
input = get_data(day=21, year=2017).splitlines()
import numpy as np

# WRITE YOUR SOLUTION HERE
def get_next_pattern(current_pattern, mapping):
    h, w = current_pattern.shape
    if h % 2 == 0:
        return apply_mapping(current_pattern, 2, mapping)
    elif h % 3 == 0:
        return apply_mapping(current_pattern, 3, mapping)

def apply_mapping(array, bs, mapping):
    h, w = array.shape
    ms = bs + 1
    fh = (h // bs) * ms
    fw = (w // bs) * ms
    mapped_blocks = np.zeros((fh, fw), dtype=array.dtype)
    for i in range(0, h, bs):
        for j in range(0, w, bs):
            block = array[i:i + bs, j:j + bs]
            blocks = mapping[block.tobytes()]
            out_row = (i // bs) * ms
            out_col = (j // bs) * ms
            mapped_blocks[out_row:out_row + ms, out_col:out_col + ms] = blocks
    return mapped_blocks

def get_mapping(lines):
    mapping = {}
    for row in lines:
        in_pat, out_pat = row.split(' => ')
        in_pat = np.array([[char == '#' for char in line] for line in in_pat.strip().split("/")])
        out_pat = np.array([[char == '#' for char in line] for line in out_pat.strip().split("/")])
        for k in range(3):
            mapping[in_pat.tobytes()] = out_pat
            mapping[np.fliplr(in_pat).tobytes()] = out_pat
            in_pat = np.rot90(in_pat)
    return mapping

def part_1(lines):
    mapping = get_mapping(lines)
    pattern = np.array([[False, True, False], [False, False, True], [True, True, True]])
    for _ in range(5):
        pattern = get_next_pattern(pattern, mapping)
    return pattern.sum()

def part_2(lines):
    mapping = get_mapping(lines)
    pattern = np.array([[False, True, False], [False, False, True], [True, True, True]])
    for _ in range(18):
        pattern = get_next_pattern(pattern, mapping)
    return pattern.sum()

# END OF SOLUTION
print(f'My answer is {part_1(input)}')
print(f'My answer is {part_2(input)}')
