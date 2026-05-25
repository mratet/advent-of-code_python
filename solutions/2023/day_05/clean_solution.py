from aocd import get_data

input = get_data(day=5, year=2023).split("\n\n")

# WRITE YOUR SOLUTION HERE


def parse_input(sections):
    seeds = list(map(int, sections[0].split(": ")[1].split()))
    mappings = [[tuple(map(int, line.split())) for line in section.splitlines()[1:]] for section in sections[1:]]
    return seeds, mappings


def mapping(categories, value):
    for category in categories:
        for dest, src, range_len in category:
            if src <= value < src + range_len:
                value = dest + value - src
                break
    return value


def check_mapping(start, end, mappings):
    ref = mapping(mappings, start) - start
    return mapping(mappings, end - 1) - (end - 1) == ref


def part_1(lines):
    seeds, mappings = parse_input(lines)
    return min(mapping(mappings, seed) for seed in seeds)


def part_2(lines):
    seeds, mappings = parse_input(lines)
    intervals = [(seeds[i], seeds[i] + seeds[i + 1]) for i in range(0, len(seeds), 2)]
    stage1_boundaries = sorted({b for dest, src, range_len in mappings[0] for b in (src, src + range_len)})
    stable = False
    while not stable:
        new_intervals = []
        stable = True
        while intervals:
            start, end = intervals.pop()
            if end - start >= 2 and not check_mapping(start, end, mappings):
                split = next((b for b in stage1_boundaries if start < b < end), (start + end) // 2)
                new_intervals.append((start, split))
                new_intervals.append((split, end))
                stable = False
            else:
                new_intervals.append((start, end))
        intervals = new_intervals
    return min(mapping(mappings, start) for start, _ in intervals)


# END OF SOLUTION


print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
