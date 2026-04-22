from itertools import cycle, permutations

from aocd import get_data
from intcode import IntcodeComputer

aoc_input = get_data(day=7, year=2019)


def run_amplifiers(lines, perm):
    amplifiers = [IntcodeComputer(lines) for _ in range(5)]
    for p, amplifier in zip(perm, amplifiers, strict=False):
        amplifier.input_buffer.append(p)

    output_signal = 0
    for amplifier in cycle(amplifiers):
        output_buffer = amplifier.run([output_signal])
        if output_buffer:
            output_signal = output_buffer[0]
        if amplifiers[-1].hasted:
            break
    return output_signal


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    return max(run_amplifiers(lines, perm) for perm in permutations(range(5)))


def part_2(lines):
    return max(run_amplifiers(lines, perm) for perm in permutations(range(5, 10)))


# END OF SOLUTION
print(f"My answer is {part_1(aoc_input)}")
print(f"My answer is {part_2(aoc_input)}")
