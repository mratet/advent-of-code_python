from aocd import get_data

aoc_input = get_data(day=24, year=2019).splitlines()


# WRITE YOUR SOLUTION HERE
def get_next_state(grid):
    new_grid = []
    for x in range(len(grid)):
        new_line = ""
        for y in range(len(grid[0])):
            symb = []
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                    symb.append(grid[nx][ny])
            match grid[x][y]:
                case "#":
                    new_line += "#" if symb.count("#") == 1 else "."
                case ".":
                    new_line += (
                        "#" if symb.count("#") == 1 or symb.count("#") == 2 else "."
                    )
        new_grid.append("".join(new_line))
    return new_grid


def compute_biodiversity(grid):
    base = "".join(grid)
    return sum(2**i for i in range(len(base)) if base[i] == "#")


def part_1(lines):
    grid = lines
    seen = set()
    while True:
        if tuple(grid) in seen:
            return compute_biodiversity(grid)
        seen.add(tuple(grid))
        next_grid = get_next_state(grid)
        grid = next_grid


def part_2(lines):
    return


# END OF SOLUTION
print(f"My answer is {part_1(aoc_input)}")
print(f"My answer is {part_2(aoc_input)}")
