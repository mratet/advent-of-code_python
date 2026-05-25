from aocd import get_data

input = get_data(day=4, year=2023).splitlines()

# WRITE YOUR SOLUTION HERE


def parse_input(lines):
    return [
        len(set(owned.split()) & set(winning.split()))
        for line in lines
        for winning, owned in [line.split(":")[1].split("|")]
    ]


def part_1(lines):
    return sum(int(2 ** (match_count - 1)) for match_count in parse_input(lines))


def part_2(lines):
    card_counts = [1] * len(lines)
    for card_idx, match_count in enumerate(parse_input(lines)):
        for bonus_idx in range(match_count):
            card_counts[card_idx + 1 + bonus_idx] += card_counts[card_idx]
    return sum(card_counts)


# END OF SOLUTION


print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
