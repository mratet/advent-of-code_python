import re
from collections import deque

from aocd import get_data

input = get_data(day=22, year=2020)


# WRITE YOUR SOLUTION HERE
def get_decks(data):
    player_regex = r"Player (\d+):\n((?:\d+\n?)+)"
    players = {}

    for match in re.finditer(player_regex, data):
        player_id = int(match.group(1))
        deck = deque(map(int, match.group(2).strip().split("\n")))
        players[player_id] = deck
    return players


def score(deck):
    return sum(n * m for n, m in zip(deck, range(len(deck), 0, -1), strict=False))


def combat(deck_1, deck_2):
    while deck_1 and deck_2:
        card1, card2 = deck_1.popleft(), deck_2.popleft()
        if card1 > card2:
            deck_1.extend([card1, card2])
        else:
            deck_2.extend([card2, card1])
    return deck_1 if deck_1 else deck_2


def part_1(lines):
    decks = get_decks(lines)
    return score(combat(decks[1], decks[2]))


def recursive_combat(deck_1, deck_2):
    seen = set()
    while deck_1 and deck_2:
        state = tuple(deck_1)
        if state in seen:
            return deck_1, deque()
        seen.add(state)

        card1, card2 = deck_1.popleft(), deck_2.popleft()
        win_condition = card1 > card2
        if card1 <= len(deck_1) and card2 <= len(deck_2):
            d1, _ = recursive_combat(deque(list(deck_1)[:card1]), deque(list(deck_2)[:card2]))
            win_condition = bool(d1)

        if win_condition:
            deck_1.extend([card1, card2])
        else:
            deck_2.extend([card2, card1])
    return deck_1, deck_2


def part_2(lines):
    decks = get_decks(lines)
    d1, d2 = recursive_combat(decks[1], decks[2])
    return score(d1 if d1 else d2)


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
