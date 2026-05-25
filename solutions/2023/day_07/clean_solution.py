from collections import Counter

from aocd import get_data

input = get_data(day=7, year=2023).splitlines()

# WRITE YOUR SOLUTION HERE


def parse_input(lines):
    return [(hand, int(value)) for line in lines for hand, value in [line.split()]]


def solve(lines, part="part_1"):
    hands = parse_input(lines)
    cards = {c: i for i, c in enumerate("--23456789TJQKA" if part == "part_1" else "-J23456789TQKA")}

    def key(item):
        hand, _ = item
        if part == "part_2" and "J" in hand and hand != "JJJJJ":
            mode = max((c for c in hand if c != "J"), key=hand.count)
            hand = hand.replace("J", mode)
        return (
            sorted(Counter(hand).values(), reverse=True),
            [cards[c] for c in item[0]],
        )

    hands.sort(key=key)
    return sum(rank * value for rank, (hand, value) in enumerate(hands, 1))


def part_1(lines):
    return solve(lines)


def part_2(lines):
    return solve(lines, part="part_2")


# END OF SOLUTION


print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
