from aocd import get_data

input = get_data(day=12, year=2018).split("\n\n")


def parse_input(lines):
    transition_dict = {}
    init_state, transitions = lines[0].split(": ")[1], lines[1]
    for transition in transitions.splitlines():
        input, output = transition.split(" => ")
        transition_dict[input] = output
    return init_state, transition_dict


def simulate(state, transition_dict, n):
    idx = 0
    MAX_CYCLE = 1000
    for _ in range(min(n, MAX_CYCLE)):
        state = "...." + state + "...."
        next_state = ""
        for i in range(len(state) - 4):
            entry = state[i : i + 5]
            next_state += transition_dict[entry]
        idx += next_state.index("#") - 2
        state = next_state.lstrip(".").rstrip(".")
    pot_sum = sum(i + idx for i, plant in enumerate(state) if plant == "#")
    if n > MAX_CYCLE:
        # If you wait long enough, each pot is on its own and moves in a given direction.
        return pot_sum + state.count("#") * (n - MAX_CYCLE)
    return pot_sum


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    init_state, transition_dict = parse_input(lines)
    return simulate(init_state, transition_dict, 20)


def part_2(lines):
    init_state, transition_dict = parse_input(lines)
    return simulate(init_state, transition_dict, 50000000000)


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
