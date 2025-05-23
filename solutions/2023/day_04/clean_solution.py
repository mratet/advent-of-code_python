from aocd import get_data

input = get_data(day=4, year=2023).splitlines()

# WRITE YOUR SOLUTION HERE


def count_match(line):
    win_cards, cards = line.split(":")[1].split("|")
    set_win_cards, set_cards = set(win_cards.split()), set(cards.split())
    return len(set_cards & set_win_cards)


def part_1(lines):
    # int to avoid counting 1/2 when there are no matches
    return sum([int(2 ** (count_match(line) - 1)) for line in lines])


def part_2(lines):
    counts = [1] * len(lines)
    for i, line in enumerate(lines):
        n = count_match(line)
        for j in range(n):
            counts[i + 1 + j] += counts[i]
    return sum(counts)


# END OF SOLUTION


print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
