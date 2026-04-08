import itertools

from aocd import get_data

input = get_data(day=20, year=2016).splitlines()


def _parse(input):
    return sorted(list(map(int, line.split("-"))) for line in input)


def merge_intervals(intervals):
    res = [intervals[0]]

    for start, end in intervals[1:]:
        last_end = res[-1][1]
        if start <= last_end + 1:
            res[-1][1] = max(last_end, end)
        else:
            res.append([start, end])
    return res


def part_1(input):
    intervals = _parse(input)
    return merge_intervals(intervals)[0][1] + 1


def part_2(input):
    intervals = _parse(input)
    intervals = merge_intervals(intervals)
    return sum(s2 - e1 - 1 for (_, e1), (s2, _) in itertools.pairwise(intervals))


print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
