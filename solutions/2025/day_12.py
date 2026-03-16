from aocd import get_data

input = get_data(day=12, year=2025).split('\n\n')

# WRITE YOUR SOLUTION HERE

def part_1(lines):
    *shape_blocks, region_blocks  = lines
    res = 0
    for region in region_blocks.splitlines():
        size, *counts = region.split()
        a, b = map(int, size[:-1].split('x'))
        res += sum(int(c) * int(shape.count('#')) for c, shape in zip(counts, shape_blocks)) < a * b
    return res

def part_2(lines):
    return 0

# END OF SOLUTION
print(f"My answer is {part_1(input)}")
# print(f"My answer is {part_2(input)}")
