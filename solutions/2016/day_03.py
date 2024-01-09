import itertools, re, collections
from aocd import get_data
input = get_data(day=3, year=2016).splitlines()

def valid_triangle(val):
    a, b, c = sorted(val)
    return a + b > c

def part_1(input):
    return sum(valid_triangle(val) for val in [[int(x) for x in line.split()] for line in input])

def part_2(input):
    t, i, n = 0, 0, len(input)
    while i < n:
        matrix = [map(int, line.split()) for line in input[i:(i+3)]]
        rows = list(zip(*matrix))
        t += sum([valid_triangle(val) for val in rows])
        i += 3
    return t

print(f'My answer is {part_1(input)}')
print(f'My answer is {part_2(input)}')
