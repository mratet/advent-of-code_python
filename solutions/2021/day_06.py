from collections import deque

from aocd import get_data

input = get_data(day=6, year=2021)


# WRITE YOUR SOLUTION HERE
def parse_input(data):
    return list(map(int, data.split(",")))


def solve(initial_fish, n):
    fish = deque(initial_fish.count(i) for i in range(9))
    for _ in range(n):
        spawning = fish[0]
        fish.rotate(-1)
        fish[6] += spawning
        fish[8] = spawning
    return sum(fish)


def part_1(data):
    return solve(parse_input(data), 80)


def part_2(data):
    return solve(parse_input(data), 256)


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
