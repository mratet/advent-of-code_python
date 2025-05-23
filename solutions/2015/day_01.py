from aocd import get_data

input = get_data(day=1, year=2015)


def part_1(input):
    sequence = [1 if c == "(" else -1 for c in input]
    return sum(sequence)


def part_2(input):
    t, i = 0, 0
    while t != -1:
        t += 1 if input[i] == "(" else -1
        i += 1

    return i


print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
