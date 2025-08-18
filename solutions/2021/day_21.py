from functools import lru_cache

from aocd import get_data
import re
from itertools import product, cycle, islice

input = get_data(day=21, year=2021).splitlines()


# Working with a game_board from 0 to 9 instead of 1 to 10
class Player:
    def __init__(self, position):
        self.position = position
        self.score = 0


GAMEBOARD_SIZE = 10


def _parse_input(lines):
    return [int(re.findall(r"(\d+)$", line)[0]) - 1 for line in lines]


def single_player_game(player, dice_gen):
    turn = []
    while player.score < 1000:
        dice = next(dice_gen)
        player.position = (player.position + dice) % GAMEBOARD_SIZE
        player.score += player.position + 1
        turn.append(player.score)
    return turn


@lru_cache(maxsize=None)
def play_quantum_game(p1_position, p1_score, p2_position, p2_score, turn):
    if p1_score >= 21:
        return (1, 0)
    if p2_score >= 21:
        return (0, 1)

    total_wins = (0, 0)
    for die in product([1, 2, 3], repeat=3):
        roll_sum = sum(die)
        if turn == 0:
            new_p1_position = (p1_position + roll_sum) % GAMEBOARD_SIZE
            new_p1_score = p1_score + new_p1_position + 1
            child_wins = play_quantum_game(
                new_p1_position, new_p1_score, p2_position, p2_score, (turn + 1) % 2
            )
        if turn == 1:
            new_p2_position = (p2_position + roll_sum) % GAMEBOARD_SIZE
            new_p2_score = p2_score + new_p2_position + 1
            child_wins = play_quantum_game(
                p1_position, p1_score, new_p2_position, new_p2_score, (turn + 1) % 2
            )
        total_wins = total_wins[0] + child_wins[0], total_wins[1] + child_wins[1]
    return total_wins


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    def sum_by_three(gen):
        while True:
            yield next(gen) + next(gen) + next(gen)

    def even_index(gen):
        return islice(gen, 0, None, 2)

    def odd_index(gen):
        return islice(gen, 1, None, 2)

    p1_position, p2_position = _parse_input(lines)
    p1, p2 = Player(p1_position), Player(p2_position)

    p1_gen = even_index(sum_by_three(cycle(range(1, 101))))
    p2_gen = odd_index(sum_by_three(cycle(range(1, 101))))

    t1 = single_player_game(p1, p1_gen)
    t2 = single_player_game(p2, p2_gen)

    winning_turn = min(len(t1), len(t2)) - 1
    dice_count = winning_turn * 2 * 3 + 3
    p_score = t2[winning_turn - 1] if len(t1) < len(t2) else t1[winning_turn - 1]
    return p_score * dice_count


def part_2(lines):
    p1_position, p2_position = _parse_input(lines)
    return max(play_quantum_game(p1_position, 0, p2_position, 0, 0))


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
