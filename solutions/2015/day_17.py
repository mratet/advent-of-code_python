import itertools
from aocd import get_data

input = get_data(day=17, year=2015).splitlines()


def find_combinations(containers, eggnog):
    combs = []
    for i in range(2, len(containers) + 1):
        combs += list(itertools.combinations(containers, i))
    valid_combs = [i for i in combs if sum(i) == eggnog]
    return valid_combs


def part_1(input):
    containers = list(map(int, input))
    liters = 25 if len(containers) == 5 else 150
    return len(find_combinations(containers, liters))


def part_2(input):
    containers = list(map(int, input))
    liters = 25 if len(containers) == 5 else 150
    combs = find_combinations(containers, liters)
    containers_numb = list(map(len, combs))
    min_numb = min(containers_numb)
    return sum([1 for comb in containers_numb if comb == min_numb])


print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
