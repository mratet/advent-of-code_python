from functools import cache

from aocd import get_data

input = get_data(day=12, year=2023).splitlines()

# WRITE YOUR SOLUTION HERE


@cache
def solve(string, decoded):
    # Solution from HyperNeutrino
    if string == "":
        return 1 if decoded == () else 0
    if decoded == ():
        return 0 if "#" in string else 1

    result = 0

    if string[0] in ".?":
        result += solve(string[1:], decoded)

    if string[0] in "#?":
        current_len = decoded[0]
        if (
            current_len <= len(string)
            and "." not in string[:current_len]
            and (current_len == len(string) or string[current_len] != "#")
        ):
            result += solve(string[current_len + 1 :], decoded[1:])

    return result


def parse_input(lines, part="part_1"):
    result = []
    for line in lines:
        encoded, decoded_str = line.split()
        decoded = tuple(int(c) for c in decoded_str.split(","))
        if part == "part_2":
            encoded = "?".join([encoded] * 5)
            decoded = decoded * 5
        result.append((encoded, decoded))
    return result


def part_1(lines):
    return sum(solve(encoded, decoded) for encoded, decoded in parse_input(lines))


def part_2(lines):
    return sum(solve(encoded, decoded) for encoded, decoded in parse_input(lines, part="part_2"))


# END OF SOLUTION


print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
