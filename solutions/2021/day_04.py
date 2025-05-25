from aocd import get_data

input = get_data(day=4, year=2021).split("\n\n")


# WRITE YOUR SOLUTION HERE
class Grid:
    def __init__(self, grid):
        self.grid = [list(map(int, row.split())) for row in grid.splitlines()]

    def check_bingo(self, nums):
        return any(all(n in nums for n in row) for row in self.grid) or any(
            all(n in nums for n in col) for col in zip(*self.grid)
        )

    def compute_score(self, nums):
        return sum(n for row in self.grid for n in row if n not in nums)


def parse_input(input_data):
    numbers = [int(n) for n in input_data[0].split(",")]
    bingo_grids = [Grid(grid) for grid in input_data[1:]]
    return numbers, bingo_grids


def compute_grid_scores(numbers, bingo_grids):
    grid_ids = list(range(len(bingo_grids)))
    grid_scores = []
    for turn in range(len(numbers)):
        current_markers = numbers[:turn]
        for grid_id in grid_ids:
            bingo_grid = bingo_grids[grid_id]
            if bingo_grid.check_bingo(current_markers):
                grid_ids.remove(grid_id)
                grid_scores.append(
                    bingo_grid.compute_score(current_markers) * numbers[turn - 1]
                )
    return grid_scores


def part_1(lines):
    numbers, bingo_grids = parse_input(lines)
    grid_scores = compute_grid_scores(numbers, bingo_grids)
    return grid_scores[0]


def part_2(lines):
    numbers, bingo_grids = parse_input(lines)
    grid_scores = compute_grid_scores(numbers, bingo_grids)
    return grid_scores[-1]


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
