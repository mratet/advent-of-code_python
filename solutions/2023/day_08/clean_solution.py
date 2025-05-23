from aocd import get_data

input = get_data(day=8, year=2023).splitlines()

# WRITE YOUR SOLUTION HERE
import re
import math

binary = {"L": 0, "R": 1}


def _parse(input):
    movements = [binary[c] for c in input[0]]
    network = {}
    for node in input[2:]:
        source, target_l, target_r = re.findall(r"\b[A-Z]{3}\b", node)
        network[source] = (target_l, target_r)

    return movements, network


def network_navigation(state, movements, network, part):
    i = 0
    while True:
        # We move either L/R and repeat the instruction until we verify our condition
        state = network[state][movements[i % len(movements)]]
        if part == "part_1" and state == "ZZZ":
            return i + 1
        elif part == "part_2" and state[2] == "Z":
            return i + 1

        i += 1


def part_1(input):
    movements, network = _parse(input)
    state = "AAA"
    return network_navigation(state, movements, network, "part_1")


def part_2(input):
    movements, network = _parse(input)

    starting_states = [source for source in network.keys() if source[2] == "A"]
    tab = [
        network_navigation(state, movements, network, "part_2")
        for state in starting_states
    ]

    return math.lcm(*tab)


# END OF SOLUTION


print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
