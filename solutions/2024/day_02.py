from aocd import get_data, submit
input = get_data(day=2, year=2024).splitlines()
from itertools import combinations

# WRITE YOUR SOLUTION HERE
def is_safe_level(level):
    return all([(l1 < l2 and 1 <= abs(l2 - l1) <= 3) for l1, l2 in zip(level, level[1:])]) or all(
        [(l1 > l2 and 1 <= abs(l2 - l1) <= 3) for l1, l2 in zip(level, level[1:])])

def part_1(lines):
    levels = [[int(l) for l in levels.split()] for levels in lines]
    return sum([is_safe_level(level) for level in levels])

def part_2(lines):
    levels = [[int(l) for l in levels.split()] for levels in lines]
    # combinations keep the order,
    return sum([any(map(is_safe_level, combinations(level, len(level) - 1))) for level in levels])

# END OF SOLUTION
print(f'My answer is {part_1(input)}')
print(f'My answer is {part_2(input)}')
