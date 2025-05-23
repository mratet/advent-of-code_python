from aocd import get_data

input = get_data(day=7, year=2023).splitlines()


# WRITE YOUR SOLUTION HERE
def part_1(input):
    inputs = []
    for line in input:
        hand, value = line.split()
        inputs.append((hand, int(value)))

    cards = "--23456789TJQKA"

    def key(item):
        hand, _ = item
        return (
            sum(hand.count(card) for card in hand),
            [cards.index(card) for card in hand],
        )

    inputs.sort(key=key)
    return sum([rank * value for rank, (hand, value) in enumerate(inputs, 1)])


def part_2(inpu):
    inputs = []
    for line in input:
        hand, value = line.split()
        inputs.append((hand, int(value)))

    cards = "-J23456789TQKA"

    def key(item):
        hand, _ = item
        if hand == "JJJJJ":
            return (25, [1, 1, 1, 1, 1])
        mode = max([card for card in hand if card != "J"], key=hand.count)
        sub = hand.replace("J", mode)
        return (
            sum(sub.count(card) for card in sub),
            [cards.index(card) for card in hand],
        )

    inputs.sort(key=key)
    return sum([rank * value for rank, (hand, value) in enumerate(inputs, 1)])
    return 0


# END OF SOLUTION


print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
