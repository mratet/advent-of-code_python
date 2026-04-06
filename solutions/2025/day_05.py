from aocd import get_data

input = get_data(day=5, year=2025).split("\n\n")


# WRITE YOUR SOLUTION HERE
def parse_intervals(block):
    intervals = [tuple(map(int, line.split("-"))) for line in block.splitlines()]
    intervals.sort()

    merged = []
    for start, end in intervals:
        if not merged or start > merged[-1][1] + 1:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)

    return merged


def part_1(lines):
    fresh_list, available_list = lines
    intervals = parse_intervals(fresh_list)
    ingredient_ids = map(int, available_list.splitlines())

    count = 0
    for ingredient_id in ingredient_ids:
        count += any(f1 <= ingredient_id <= f2 for f1, f2 in intervals)
    return count


def part_2(lines):
    fresh_list, _ = lines
    intervals = parse_intervals(fresh_list)
    return sum(end - start + 1 for start, end in intervals)


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
