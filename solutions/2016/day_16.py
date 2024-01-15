import itertools, re, collections
from aocd import get_data
input = get_data(day=16, year=2016)

def dragon_curve(a):
    b = [not elt for elt in a[::-1]]
    a.append(False)
    return a + b

def checksum(s):
    while len(s) % 2 == 0:
        s = [e1 == e2 for e1, e2 in zip(s[::2], s[1::2])]
    return s

def solve(input, N):
    s = [elt == '1' for elt in input]
    while len(s) < N:
        s = dragon_curve(s)
    return ''.join([str(int(elt)) for elt in checksum(s[:N])])

def part_1(input):
    N = 272
    return solve(input, N)

def part_2(input):
    N = 35651584
    return solve(input, N)

print(f'My answer is {part_1(input)}')
print(f'My answer is {part_2(input)}')
