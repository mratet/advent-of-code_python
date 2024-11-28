from aocd import get_data
input = get_data(day=11, year=2020).splitlines()
from itertools import product

# WRITE YOUR SOLUTION HERE
def get_adjacent_state(grid, pos, part):
    L, C = len(grid), len(grid[0])
    x, y  = pos
    neighboors_symb = []
    for dx, dy in product((-1, 0, 1), repeat=2):
        if (dx, dy ) == (0, 0):
            continue
        if part == 'part_1':
            nx, ny = x + dx, y + dy
            if  0 <= nx < L and 0 <= ny < C:
                neighboors_symb.append(grid[nx][ny])
        elif part == 'part_2':
            dist = 1
            nx, ny = x + dist * dx, y + dist * dy
            while 0 <= nx < L and 0 <= ny < C:
                next_symb = grid[nx][ny]
                if next_symb != '.':
                    neighboors_symb.append(next_symb)
                    break
                dist += 1
                nx, ny = x + dist * dx, y + dist * dy
    return neighboors_symb

def get_next_state(grid, part):
    OCCUPIED_TOLERANCE = 4 if part == 'part_1' else 5
    new_grid = []
    for i in range(len(grid)):
        new_line = ''
        for j in range(len(grid[0])):
            view = get_adjacent_state(grid, (i, j), part)
            match grid[i][j]:
                case 'L':
                    new_line += '#' if '#' not in view else 'L'
                case '#':
                    new_line += 'L' if view.count('#') >= OCCUPIED_TOLERANCE else '#'
                case '.':
                    new_line += '.'
        new_grid.append(''.join(new_line))
    return new_grid

def get_occuped_seat(lines, part):
    grid = lines
    while True:
        next_grid = get_next_state(grid, part)
        if next_grid == grid:
            return ''.join(grid).count('#')
        grid = next_grid

def part_1(lines):
    return get_occuped_seat(lines, 'part_1')

def part_2(lines):
    return get_occuped_seat(lines, 'part_2')

# END OF SOLUTION
print(f'My answer is {part_1(input)}')
print(f'My answer is {part_2(input)}')
