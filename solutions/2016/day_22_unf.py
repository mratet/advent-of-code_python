import itertools, re, collections
from aocd import get_data

input = get_data(day=22, year=2016).splitlines()


def _parse_input(input):
    storage = {}
    for line in input[2:]:
        pattern = r"/dev/grid/node-x(\d+)-y(\d+)\s+(\d+)T\s+(\d+)T*"
        X, Y, size, used = map(int, re.findall(pattern, line)[0])
        storage[(X, Y)] = (size, used)
    return storage


def part_1(input):
    storage = _parse_input(input)
    t = 0
    for n1, n2 in itertools.product(storage, storage):
        s1, u1 = storage[n1]
        s2, u2 = storage[n2]
        if u1 > 0 and n1 != n2 and u1 < s2 - u2:
            t += 1
    return t


print(f"My answer is {part_1(input)}")
# print(f'My answer is {part_2(input)}')
