from aocd import get_data

input_data = get_data(day=5, year=2018)


def polymer_one_step(polymer: str) -> str:
    for i in range(26):
        lower = chr(ord("a") + i)
        upper = chr(ord("A") + i)
        polymer = polymer.replace(lower + upper, "").replace(upper + lower, "")
    return polymer


def polymer_reaction(polymer: str) -> int:
    prev = None
    while polymer != prev:
        prev = polymer
        polymer = polymer_one_step(polymer)
    return len(polymer)


# WRITE YOUR SOLUTION HERE
def part_1(polymer: str) -> int:
    return polymer_reaction(polymer)


def part_2(polymer: str) -> int:
    return min(
        polymer_reaction(polymer.replace(chr(i), "").replace(chr(i).upper(), ""))
        for i in range(ord("a"), ord("z") + 1)
    )


# END OF SOLUTION
print(f"My answer is {part_1(input_data)}")
print(f"My answer is {part_2(input_data)}")
