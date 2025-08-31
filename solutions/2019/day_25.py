from aocd import get_data
from intcode import IntcodeComputer, MAP_TO_ASCII, MAP_FROM_ASCII

aoc_input = get_data(day=25, year=2019)


# WRITE YOUR SOLUTION HERE
def part_1(lines, wanna_play=False):
    # Change this parameter if you want to play by yourself
    if not wanna_play:
        return 4206594
    pc = IntcodeComputer(lines)
    buffer = pc.run()
    print(MAP_FROM_ASCII(buffer))

    while True:
        buffer = pc.run(MAP_TO_ASCII(f"{input()}\n"))
        print(MAP_FROM_ASCII(buffer))


# END OF SOLUTION
print(f"My answer is {part_1(aoc_input)}")
