import itertools, re, collections
from aocd import get_data

input = get_data(day=14, year=2016)
from hashlib import md5


def extend_hash(hash):
    for _ in range(2017):
        hash = md5(hash.encode()).hexdigest()
    return hash


def match_md5(input, part="part_1"):
    my_hash, i, cnt = "", 0, 0
    visited = {}
    while cnt < 64:
        new_input = input + str(i)
        my_hash = (
            extend_hash(new_input)
            if part == "part_2"
            else md5(new_input.encode()).hexdigest()
        )
        match = re.search(r"(.)\1\1", my_hash)
        if match:
            c = match.group(1)
            for j in range(1, 1001):
                temp_input = input + str(i + j)
                if temp_input in visited:
                    my_hash = visited[temp_input]
                else:
                    my_hash = (
                        extend_hash(temp_input)
                        if part == "part_2"
                        else md5(temp_input.encode()).hexdigest()
                    )
                    visited[temp_input] = my_hash

                if re.search(c * 5, my_hash):
                    cnt += 1
                    break
        i += 1
    return i - 1


def part_1(input):
    return match_md5(input, "part_1")


def part_2(input):
    return match_md5(input, "part_2")


print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
