from aocd import get_data
from collections import Counter

input = get_data(day=10, year=2020).splitlines()


# WRITE YOUR SOLUTION HERE
def get_adapters(lines):
    adapters = sorted([int(n) for n in lines])
    return [0] + adapters + [max(adapters) + 3]


def part_1(lines):
    adapters = get_adapters(lines)
    count_diff = Counter([next - acc for acc, next in zip(adapters, adapters[1:])])
    return count_diff[1] * count_diff[3]


def part_2(lines):
    adapters = get_adapters(lines)
    cnt = {0: 1}
    for adapter in adapters[1:]:
        cnt[adapter] = (
            cnt.get(adapter - 1, 0) + cnt.get(adapter - 2, 0) + cnt.get(adapter - 3, 0)
        )
    return cnt[adapters[-1]]


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
