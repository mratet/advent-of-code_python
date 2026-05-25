from aocd import get_data

input = get_data(day=25, year=2021).splitlines()


# WRITE YOUR SOLUTION HERE
def parse_input(lines):
    rows, cols = len(lines), len(lines[0])
    east = {(x, y) for y, line in enumerate(lines) for x, c in enumerate(line) if c == ">"}
    south = {(x, y) for y, line in enumerate(lines) for x, c in enumerate(line) if c == "v"}
    return east, south, rows, cols


def next_turn(east, south, rows, cols):
    occupied = east | south
    new_east = {(nx, y) if (nx, y) not in occupied else (x, y) for x, y in east for nx in [(x + 1) % cols]}
    new_occupied = new_east | south
    new_south = {(x, ny) if (x, ny) not in new_occupied else (x, y) for x, y in south for ny in [(y + 1) % rows]}
    return new_east, new_south


def part_1(lines):
    east, south, rows, cols = parse_input(lines)
    step_count = 0
    while True:
        new_east, new_south = next_turn(east, south, rows, cols)
        step_count += 1
        if new_east == east and new_south == south:
            break
        east, south = new_east, new_south
    return step_count


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
