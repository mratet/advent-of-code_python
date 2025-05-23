from aocd import get_data

aoc_input = get_data(day=11, year=2019)
from intcode import read_program, run_program, deque

# WRITE YOUR SOLUTION HERE
N, S, E, W = (0, 1), (0, -1), (1, 0), (-1, 0)
dirs = [N, E, S, W]


def part_1(lines):
    memory = read_program(lines)
    screen_state = {}
    px, py = 0, 0
    direction = 0
    while True:
        in_buff = deque([screen_state.get((px, py), 0)])
        memory, out_buff = run_program(memory, in_buff)
        if not out_buff:
            break
        panel_color, turn = out_buff
        screen_state[(px, py)] = panel_color
        direction = dirs[(direction + 1) % 4] if turn else dirs[(direction - 1) % 4]
        px, py = px + direction[0], py + direction[1]

    return


def part_2(lines):
    return


# END OF SOLUTION
print(f"My answer is {part_1(aoc_input)}")
print(f"My answer is {part_2(aoc_input)}")
