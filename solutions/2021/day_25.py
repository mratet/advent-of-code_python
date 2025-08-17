from aocd import get_data

input = get_data(day=25, year=2021).splitlines()


def get_grid(lines):
    grid = {}
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            grid[(x, y)] = c
    return grid


def get_next_turn(grid):
    X, Y = max(grid)
    EC = [coord for coord, c in grid.items() if c == ">"]
    SC = [coord for coord, c in grid.items() if c == "v"]

    intermediate_grid = grid.copy()
    for x, y in EC:
        nx = (x + 1) % (X + 1)
        if grid[(nx, y)] == ".":
            intermediate_grid[(nx, y)] = ">"
            intermediate_grid[(x, y)] = "."

    final_grid = intermediate_grid.copy()
    for x, y in SC:
        ny = (y + 1) % (Y + 1)
        if intermediate_grid[(x, ny)] == ".":
            final_grid[(x, ny)] = "v"
            final_grid[(x, y)] = "."

    return final_grid


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    grid = get_grid(lines)  # Assurez-vous d'utiliser 'lines' et non 'input' global
    step_count = 0
    while True:
        new_grid = get_next_turn(grid)
        step_count += 1
        if new_grid == grid:
            break
        grid = new_grid

    return step_count


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
# print(f'My answer is {part_2(input)}')
