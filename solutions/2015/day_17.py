import itertools

from aocd import get_data

input = get_data(day=17, year=2015).splitlines()

EGGNOG_LITERS = 150


def find_combinations(containers):
    return [
        comb
        for comb_size in range(2, len(containers) + 1)
        for comb in itertools.combinations(containers, comb_size)
        if sum(comb) == EGGNOG_LITERS
    ]


def part_1(input):
    containers = list(map(int, input))
    return len(find_combinations(containers))


def part_2(input):
    containers = list(map(int, input))
    combs = find_combinations(containers)
    min_numb = min(map(len, combs))
    return sum(len(comb) == min_numb for comb in combs)


print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
