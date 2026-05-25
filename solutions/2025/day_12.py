from aocd import get_data

input = get_data(day=12, year=2025).split("\n\n")

# WRITE YOUR SOLUTION HERE


def part_1(lines):
    *shape_blocks, region_blocks = lines
    total = 0
    for region in region_blocks.splitlines():
        size, *counts = region.split()
        rows, cols = map(int, size[:-1].split("x"))
        total += (
            sum(int(presses) * shape.count("#") for presses, shape in zip(counts, shape_blocks, strict=False))
            < rows * cols
        )
    return total


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
