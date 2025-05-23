from aocd import get_data

input = get_data(day=5, year=2023).splitlines()


# WRITE YOUR SOLUTION HERE
def mapping(category, x):
    for lines in category:
        for line in lines:
            destination, source, rangE = map(int, line.split())
            if source <= x < source + rangE:
                x = destination + x - source
                break
    return x


def _parse(input):
    seeds = list(map(int, input[0].split(":")[1].split()))
    category_transformation = [[] for _ in range(7)]
    i = 0
    for line in input[2:]:
        if line and line[0].isnumeric():
            category_transformation[int(i)].append(line)
        else:
            i += 0.5
    return seeds, category_transformation


def part_1(lines):
    seeds, category_transformation = _parse(input)
    location = [mapping(category_transformation, seed) for seed in seeds]
    return min(location)


def check_mapping(start, end, category):
    # We check at different location if there is a hole into the mapping return or not
    # If the intertal is clean, f(x) - x should be a constant
    # Otherwise, we need to split it

    ref = mapping(category, start) - start
    length = 10  # trade-off between speed and precision
    step = (end - start) // length + 1
    return all([mapping(category, i) - i == ref for i in range(start, end, step)])


def part_2(input):
    seeds, category_transformation = _parse(input)
    intervals = [(seeds[i], seeds[i] + seeds[i + 1]) for i in range(0, len(seeds), 2)]

    flag = False
    while not flag:
        new_intervals = []
        flag = True
        while intervals:
            start, end = intervals.pop()
            if (end - start) >= 2 and not check_mapping(
                start, end, category_transformation
            ):
                mid = (start + end) // 2
                new_intervals.append((start, mid))
                new_intervals.append((mid, end))
                flag = False
            else:
                new_intervals.append((start, end))
        intervals = new_intervals.copy()

    return min([mapping(category_transformation, start) for start, _ in intervals])


"""
Il existe des moyens plus efficaces pour trouver la préférence de chevauchement entre deux intervalles
Mais il est alors plus simple de ne pas passer par une fonction mapping complète (voir hy
"""


# END OF SOLUTION


print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
