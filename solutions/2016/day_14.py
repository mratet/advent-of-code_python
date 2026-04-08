import re
from functools import lru_cache
from hashlib import md5

from aocd import get_data

input = get_data(day=14, year=2016)


def find_password(input, part="part_1"):
    base = md5(input.encode())

    @lru_cache(maxsize=2048)
    def get_hash(i):
        h = base.copy()
        h.update(str(i).encode())
        h = h.hexdigest()
        if part == "part_2":
            for _ in range(2016):
                h = md5(h.encode()).hexdigest()
        return h

    cnt, i = 0, 0
    while cnt < 64:
        my_hash = get_hash(i)
        match = re.search(r"(.)\1\1", my_hash)
        if match:
            target = match.group(1) * 5
            for j in range(i + 1, i + 1001):
                if target in get_hash(j):
                    cnt += 1
                    break
        i += 1
    return i - 1


def part_1(input):
    return find_password(input, "part_1")


def part_2(input):
    return find_password(input, "part_2")


print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
