from aocd import get_data
import re
from itertools import product, cycle, islice

input = get_data(day=21, year=2021).splitlines()


# Working with a game_board from 0 to 9 instead of 1 to 10
class Player:
    def __init__(self, position):
        self.position = position
        self.score = 0


GOAL_SCORE = 1000
GAMEBOARD_SIZE = 10
SIZE = 10


def single_player_game(player, dice_gen):
    turn = []
    while player.score < GOAL_SCORE:
        dice = next(dice_gen)
        player.position = (player.position + dice) % GAMEBOARD_SIZE
        player.score += player.position + 1
        turn.append(player.score)
    return turn


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    def sum_by_three(gen):
        while True:
            yield next(gen) + next(gen) + next(gen)

    def even_index(gen):
        return islice(gen, 0, None, 2)

    def odd_index(gen):
        return islice(gen, 1, None, 2)

    pattern = r"Player \d starting position: (\d+)"

    p1 = Player(int(re.findall(pattern, lines[0])[0]) - 1)
    p2 = Player(int(re.findall(pattern, lines[1])[0]) - 1)

    p1_gen = even_index(sum_by_three(cycle(range(1, 101))))
    p2_gen = odd_index(sum_by_three(cycle(range(1, 101))))

    t1 = single_player_game(p1, p1_gen)
    t2 = single_player_game(p2, p2_gen)

    winning_turn = min(len(t1), len(t2)) - 1
    dice_count = winning_turn * 2 * 3 + 3
    p_score = t2[winning_turn - 1] if len(t1) < len(t2) else t1[winning_turn - 1]
    return p_score * dice_count


def part_2(lines):
    return


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
# print(f'My answer is {part_2(input)}')

# die_casting = list(product([1, 2, 3], repeat=3))
# L = [ sum(d) for d in die_casting ]
# 3 1
# 4 3
# 5 6
# 6 7
# 7 6
# 8 3
# 9 1
# die_casting = product(range(3, 10), repeat=SIZE)
# s = 0
# for _ in die_casting:
#     s += 1
# print(s)
# # n = len(die_casting)
# s = 0
# for d in die_casting:
#     p = Player(9)
#     try:
#         t = single_player_game(p, iter(d))
#     except StopIteration:
#         s += 1
# print(s)
