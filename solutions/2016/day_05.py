import itertools, re, collections
from aocd import get_data

input = get_data(day=5, year=2016)

from hashlib import md5


def match_md5(input):
    my_hash, i = "2", 0
    p1, p2 = [""] * 8, [""] * 8
    cnt = 0
    while not (all(p1) and all(p2)):
        new_input = input + str(i)
        my_hash = md5(new_input.encode()).hexdigest()
        if my_hash.startswith("00000"):
            c = my_hash[5]

            if cnt < 8:
                p1[cnt] = c
                cnt += 1

            if c.isdigit() and int(c) < 8 and p2[int(c)] == "":
                p2[int(c)] = my_hash[6]
        i += 1

    return "".join(p1), "".join(p2)


def part_1(input):
    p1, _ = match_md5(input)
    return p1


def part_2(input):
    _, p2 = match_md5(input)
    return p2


print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
