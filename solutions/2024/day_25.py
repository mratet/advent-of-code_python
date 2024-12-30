# from aocd import get_data, submit
# input = get_data(day=23, year=2024).splitlines()
from collections import defaultdict
from itertools import combinations, product

input = open('input.txt').read().split('\n\n')
keys = set()
pins = set()
def turn_counter_clockwise(grid):
    return list(zip(*grid))[::-1]
grid = input[0].splitlines()

for schema in input:
    grid = turn_counter_clockwise(schema.splitlines())
    idx = 'pins' if grid[0][0] == '#' else 'keys'
    symb = '.' if idx == 'pins' else '#'
    seq = []
    if idx == 'pins':
        for t in grid:
            seq.append(t.index(symb) - 1)
        seq = tuple(reversed(seq))
        pins.add(seq)
    elif idx == 'keys':
        for t in grid:
            seq.append(6 - t.index(symb))
        seq = tuple(reversed(seq))
        keys.add(seq)

ans = 0
for g1, g2 in product(keys, pins):
    ans += all([t1 + t2 < 6 for t1, t2 in zip(g1, g2)])

print(ans)
print(keys)
print(pins)
# END OF SOLUTION
# print(f'My answer is {part_1(input)}')
# print(f'My answer is {part_2(input)}')
