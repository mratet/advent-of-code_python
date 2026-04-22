from aocd import get_data

input_data = get_data(day=5, year=2018)


PAIRS = [(chr(ord("a") + i), chr(ord("A") + i)) for i in range(26)]


def polymer_reaction(polymer: str) -> int:
    prev_len = None
    while len(polymer) != prev_len:
        prev_len = len(polymer)
        for lower, upper in PAIRS:
            polymer = polymer.replace(lower + upper, "").replace(upper + lower, "")
    return len(polymer)


# WRITE YOUR SOLUTION HERE
def part_1(polymer: str) -> int:
    return polymer_reaction(polymer)


def part_2(polymer: str) -> int:
    return min(
        polymer_reaction(polymer.replace(chr(i), "").replace(chr(i).upper(), "")) for i in range(ord("a"), ord("z") + 1)
    )


# END OF SOLUTION
print(f"My answer is {part_1(input_data)}")
print(f"My answer is {part_2(input_data)}")
