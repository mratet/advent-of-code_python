from aocd import get_data

input = get_data(day=15, year=2020)


# WRITE YOUR SOLUTION HERE
def compute_spoken_number(n, seed):
    memory = {s: turn + 1 for turn, s in enumerate(seed)}
    spoken_number = (
        0  # There ane no duplicates in the seed, so the last spoken number is a 0
    )

    for turn in range(len(seed) + 1, n):
        next_number = turn - memory.get(spoken_number, turn)
        memory[spoken_number] = turn
        spoken_number = next_number
    return spoken_number


def part_1(lines):
    return compute_spoken_number(2020, [int(n) for n in lines.split(",")])


def part_2(lines):
    return compute_spoken_number(30000000, [int(n) for n in lines.split(",")])


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
