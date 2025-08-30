from aocd import get_data
from intcode import IntcodeComputer
from itertools import permutations

aoc_input = get_data(day=7, year=2019)


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    tab = []
    for perm in permutations(range(5)):
        output_signal = 0
        for p in perm:
            pc = IntcodeComputer(lines)
            [output_signal] = pc.run([p, output_signal])
        tab.append(output_signal)
    return max(tab)


def part_2(lines):
    tab = []
    for perm in permutations(range(5, 10)):
        amplifiers = [IntcodeComputer(lines) for _ in range(5)]
        for p, amplifier in zip(perm, amplifiers):
            amplifier.input_buffer.append(p)

        cnt = 0
        output_signal = 0
        while True:
            output_buffer = amplifiers[cnt % 5].run([output_signal])
            if output_buffer:
                output_signal = output_buffer[0]
            if not output_buffer and (cnt % 5) == 4:
                break
            cnt += 1
        tab.append(output_signal)
    return max(tab)


# END OF SOLUTION
print(f"My answer is {part_1(aoc_input)}")
print(f"My answer is {part_2(aoc_input)}")
