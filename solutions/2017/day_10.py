
from aocd import get_data, submit
input = get_data(day=10, year=2017)
from functools import reduce
from operator import xor

# WRITE YOUR SOLUTION HERE
def rotation_step(lengths):
    L = list(range(256))
    current_pos, skip_size = 0, 0
    for l in lengths:
        if l > len(L): continue
        if current_pos + l < len(L):
            L[current_pos : current_pos + l] = list(reversed(L[current_pos : current_pos + l]))
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
    xor_hash = [reduce(xor, L[i:i + 16]) for i in range(0, 256, 16)]
    return ''.join([hex(x)[2:].zfill(2) for x in xor_hash])

def part_1(lines):
    lengths = [int(n) for n in lines.split(',')]
    L = rotation_step(lengths)
    return L[0] * L[1]

def part_2(lines):
    return knot_hash(lines)

# END OF SOLUTION
print(f'My answer is {part_1(input)}')
print(f'My answer is {part_2(input)}')

