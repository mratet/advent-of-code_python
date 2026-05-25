import math
import re
from itertools import cycle

from aocd import get_data

input = get_data(day=8, year=2023).splitlines()

binary = {"L": 0, "R": 1}

# WRITE YOUR SOLUTION HERE


def parse_input(lines):
    movements = [binary[c] for c in lines[0]]
    network = {}
    for node in lines[2:]:
        source, target_l, target_r = re.findall(r"\b[A-Z]{3}\b", node)
        network[source] = (target_l, target_r)
    return movements, network


def network_navigation(start, movements, network, end_condition):
    for step, move in enumerate(cycle(movements), 1):
        start = network[start][move]
        if end_condition(start):
            return step


def part_1(lines):
    movements, network = parse_input(lines)
    return network_navigation("AAA", movements, network, lambda s: s == "ZZZ")


def part_2(lines):
    movements, network = parse_input(lines)
    starting_states = [source for source in network if source[2] == "A"]
    cycle_lengths = [network_navigation(state, movements, network, lambda s: s[-1] == "Z") for state in starting_states]
    return math.lcm(*cycle_lengths)


# END OF SOLUTION


print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
