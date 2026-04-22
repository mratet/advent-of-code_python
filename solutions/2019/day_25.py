from aocd import get_data
from intcode import MAP_FROM_ASCII, MAP_TO_ASCII, IntcodeComputer

aoc_input = get_data(day=25, year=2019)


PLAY = False  # Set to True to play interactively


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    if not PLAY:
        return 4206594
    pc = IntcodeComputer(lines)
    buffer = pc.run()
    print(MAP_FROM_ASCII(buffer))

    while True:
        buffer = pc.run(MAP_TO_ASCII(f"{input()}\n"))
        print(MAP_FROM_ASCII(buffer))


# END OF SOLUTION
print(f"My answer is {part_1(aoc_input)}")
