from aocd import get_data

input = get_data(day=7, year=2025).splitlines()

# WRITE YOUR SOLUTION HERE
def solve(lines, *, is_part_1: bool):
    splitters = [[j for j, c in enumerate(line) if c == '^'] for i, line in enumerate(lines) if i % 2 == 0]
    start_beam = lines[0].index('S')
    cache = {}

    def count(beam, split_idx):
        if (beam, split_idx) in cache:
            return 0 if is_part_1 else cache[(beam, split_idx)]

        if split_idx >= len(splitters):
            return 0 if is_part_1 else 1

        if beam not in splitters[split_idx]:
            result = count(beam, split_idx + 1)
        else:
            result = count(beam - 1, split_idx + 1) + count(beam + 1, split_idx + 1) + is_part_1

        cache[(beam, split_idx)] = result
        return result

    return count(start_beam, 1)

def part_1(lines):
    return solve(lines, is_part_1=True) # count splitters

def part_2(lines):
    return solve(lines, is_part_1=False) # count paths

# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
