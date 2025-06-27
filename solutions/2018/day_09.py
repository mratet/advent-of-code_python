from aocd import get_data
from collections import deque

input = get_data(day=9, year=2018).split()


def parse_input(input_text):
    return map(int, [input_text[0], input_text[-2]])


def compute_best_score(player_count, last_marble):
    scores = [0] * player_count
    marbles = deque([0])

    for marble in range(1, last_marble + 1):
        if marble % 23 == 0:
            marbles.rotate(7)
            scores[marble % player_count] += marble + marbles.pop()
            marbles.rotate(-1)
        else:
            marbles.rotate(-1)
            marbles.append(marble)

    return max(scores)


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    player_count, last_marble = parse_input(lines)
    return compute_best_score(player_count, last_marble)


def part_2(lines):
    player_count, last_marble = parse_input(lines)
    return compute_best_score(player_count, last_marble * 100)


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
