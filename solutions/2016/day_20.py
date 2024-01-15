import itertools, re, collections
from aocd import get_data
input = get_data(day=20, year=2016).splitlines()

R = [0, 4294967295]

def _parse(input):
    intervals = []
    for line in input:
        s, e = line.split('-')
        intervals.append([int(s), int(e)])

    return intervals

def merge_intervals(intervals):
    intervals.sort()
    res = [intervals[0]]

    for start, end in intervals[1:]:
        lastEnd = res[-1][1]
        if start <= lastEnd + 1:
            res[-1][1] = max(lastEnd, end)
        else:
            res.append([start, end])
    return res

def part_1(input):
    intervals = _parse(input)
    return merge_intervals(intervals)[0][1] + 1

def part_2(input):
    intervals = _parse(input)
    intervals = merge_intervals(intervals)
    cnt = sum([s2 - e1 - 1 for (_, e1), (s2, _) in zip(intervals, intervals[1:])])
    return cnt

print(f'My answer is {part_1(input)}')
print(f'My answer is {part_2(input)}')
