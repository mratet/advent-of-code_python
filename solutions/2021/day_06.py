from aocd import get_data
from collections import deque

input = get_data(day=6, year=2021)


# WRITE YOUR SOLUTION HERE
def next_step(lanternfish: deque) -> deque:
    next_gen = lanternfish[0]
    lanternfish.rotate(-1)
    lanternfish[6] += next_gen
    lanternfish[8] = next_gen
    return lanternfish


def count_lanternfish(initial_fish: list, n: int) -> int:
    lanternfish = deque([initial_fish.count(i) for i in range(9)])
    for _ in range(n):
        lanternfish = next_step(lanternfish)
    return sum(lanternfish)


def part_1(input_str: str) -> int:
    initial_fish = list(map(int, input_str.split(",")))
    return count_lanternfish(initial_fish, 80)


def part_2(input_str: str) -> int:
    initial_fish = list(map(int, input_str.split(",")))
    return count_lanternfish(initial_fish, 256)


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
