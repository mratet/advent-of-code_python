from aocd import get_data

input = get_data(day=2, year=2025).splitlines()

# WRITE YOUR SOLUTION HERE
def is_repeated_pattern(s):
    return any(
        len(s) % pattern_size == 0 and s[:pattern_size] * (len(s) // pattern_size) == s
        for pattern_size in range(1, len(s) // 2 + 1)
    )

def sum_valid_ids(lines, validator):
    ranges = lines[0].split(',')
    total = 0

    for range_ in ranges:
        start, end = map(int, range_.split('-'))
        start, end = min(start, end), max(start, end)

        total += sum(number for number in range(start, end + 1) if validator(str(number)))

    return total

def part_1(lines):
    return sum_valid_ids(lines, lambda x: x[:len(x) // 2] == x[len(x) // 2:])

def part_2(lines):
    return sum_valid_ids(lines, is_repeated_pattern)

# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
