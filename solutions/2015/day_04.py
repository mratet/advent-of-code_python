from aocd import get_data

input = get_data(day=4, year=2015)

from hashlib import md5


def match_md5(input, match):
    my_hash, i = "2", 0
    while not my_hash.startswith(match):
        new_input = input + str(i)
        my_hash = md5(new_input.encode()).hexdigest()
        i += 1

    return i - 1


def part_1(input):
    return match_md5(input, "00000")


def part_2(input):
    return match_md5(input, "000000")


print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
