from aocd import get_data, submit
input = get_data(day=1, year=2024).split()
from collections import Counter

# WRITE YOUR SOLUTION HERE
def parse_input(lines):
    data = [int(n) for n in lines]
    return sorted(data[::2]), sorted(data[1::2])

def part_1(lines):
    left, right = parse_input(lines)
    return sum([abs(r - l) for l, r in zip(left, right)])

def part_2(lines):
    left, right = parse_input(lines)
    right_count = Counter(right)
    return sum([right_count[l] * l for l in left])

# END OF SOLUTION
print(f'My answer is {part_1(input)}')
print(f'My answer is {part_2(input)}')
