from aocd import get_data
import numpy as np
from matplotlib import pyplot as plt

input = get_data(day=10, year=2022).splitlines()


def run_program(lines):
    X = 1
    yield X
    for line in lines:
        if line == "noop":
            yield X
        else:
            _, V = line.split()
            yield X
            yield X
            X += int(V)


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    state = list(run_program(lines))
    return sum(cycle * state[cycle] for cycle in range(20, 221, 40))


def part_2(lines):
    W, H = 40, 6
    state = list(run_program(lines))[1:]  # Skip cycle 0
    screen = np.array(
        [1 if abs((i % W) - x) <= 1 else 0 for i, x in enumerate(state)]
    ).reshape(H, W)
    plt.imshow(screen, cmap="binary")
    # plt.show()
    return None


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
