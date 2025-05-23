from aocd import get_data

input = get_data(day=22, year=2020)
import re


# WRITE YOUR SOLUTION HERE
def get_decks(data):
    player_regex = r"Player (\d+):\n((?:\d+\n?)+)"
    players = {}

    for match in re.finditer(player_regex, data):
        player_id = int(match.group(1))
        deck = list(map(int, match.group(2).strip().split("\n")))
        players[player_id] = deck
    return players


def combat(deck_1, deck_2):
    while deck_1 and deck_2:
        card1, card2 = deck_1.pop(0), deck_2.pop(0)
        if card1 > card2:
            deck_1.extend([card1, card2])
        else:
            deck_2.extend([card2, card1])
    return deck_1 if deck_1 else deck_2


def part_1(lines):
    decks = get_decks(lines)
    deck = combat(decks[1], decks[2])
    return sum([n * (len(deck) - i) for i, n in enumerate(deck)])


def recursive_combat(deck_1, deck_2):
    mem = set()
    while deck_1 and deck_2:
        p1_mem, p2_mem = tuple([1] + deck_1), tuple([2] + deck_2)
        if p1_mem in mem or p2_mem in mem:
            return (["Winner"], [])
        else:
            mem.add(p1_mem)
            mem.add(p2_mem)

        card1, card2 = deck_1.pop(0), deck_2.pop(0)
        win_condition = card1 > card2
        if card1 <= len(deck_1) and card2 <= len(deck_2):
            (d1, d2) = recursive_combat(deck_1[:card1], deck_2[:card2])
            win_condition = True if d1 else False

        if win_condition:
            deck_1.extend([card1, card2])
        else:
            deck_2.extend([card2, card1])
    return (deck_1, deck_2)


def part_2(lines):
    decks = get_decks(lines)
    (d1, d2) = recursive_combat(decks[1], decks[2])
    deck = d1 if d1 else d2
    return sum([n * (len(deck) - i) for i, n in enumerate(deck)])


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
