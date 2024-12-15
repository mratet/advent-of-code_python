from aocd import get_data, submit
input = get_data(day=15, year=2024).split('\n\n')

# WRITE YOUR SOLUTION HERE
def possible_move(mapping, x, y, dx, dy):
    next = mapping[x + dx][y + dy]
    if next == '.':
        mapping[x + dx][y + dy] = 'O'
        return True, mapping
    elif next == '#':
        return False, mapping
    elif next == 'O':
        return possible_move(mapping, x + dx, y + dy, dx, dy)

def part_1(lines):
    grid = [list(l) for l in lines[0].split()]
    (px, py) = [(x, y) for x in range(len(grid)) for y in range(len(grid[0])) if grid[x][y] == '@'][0]
    moves = lines[1]
    dx, dy = 0, 0

    for line in moves.split('\n'):
        for c in line:
            if c == "^":
                dx, dy = -1, 0
            elif c == ">":
                dx, dy = 0, 1
            elif c == "<":
                dx, dy = 0, -1
            elif c == "v":
                dx, dy = 1, 0

            move_bool, new_grid = possible_move(grid, px, py, dx, dy)
            if move_bool:
                new_grid[px][py] = '.'
                px += dx
                py += dy
                new_grid[px][py] = '@'
                grid = new_grid
    return sum([100 * x + y for x in range(len(grid)) for y in range(len(grid[0])) if grid[x][y] == 'O'])

def find_block_to_move(grid, x, y, dx, dy):
    symb = grid[x][y]
    block = (x, y, x, y + 1) if symb == '[' else (x, y - 1, x, y)
    all_blocks = [block]
    cand = [block]
    while cand:
        lx, ly, rx, ry = cand.pop()
        ln = grid[lx + dx][ly + dy]
        rn = grid[rx + dx][ry + dy]
        lc = rc = None
        if ln == '#' or rn == '#':
            return []
        if ln == '[':
            lc = (lx + dx, ly + dy, lx + dx, ly + dy + 1)
        elif ln == ']':
            lc = (lx + dx, ly + dy - 1, lx + dx, ly + dy)

        if rn == '[':
            rc = (rx + dx, ry + dy, rx + dx, ry + dy + 1)
        elif rn == ']':
            rc = (rx + dx, ry + dy - 1, rx + dx, ry + dy)
        for c in (lc, rc):
            if c:
                if c in all_blocks:
                    continue
                cand.append(c)
                all_blocks.append(c)

    return all_blocks


def part_2(lines):
    init_grid = [list(l) for l in lines[0].split()]
    grid = [[] for _ in range(len(init_grid))]
    px, py = 0, 0
    for x in range(len(init_grid)):
        for y in range(len(init_grid[0])):
            c = init_grid[x][y]
            if c == '#':
                grid[x].append('#')
                grid[x].append('#')
            elif c == 'O':
                grid[x].append('[')
                grid[x].append(']')
            elif c == '.':
                grid[x].append('.')
                grid[x].append('.')
            else:
                grid[x].append('@')
                grid[x].append('.')
                px, py = x, 2 * y

    moves = lines[1]
    dx, dy = 0, 0

    for line in moves.split('\n'):
        for c in line:
            if c == "^":
                dx, dy = -1, 0
            elif c == ">":
                dx, dy = 0, 1
            elif c == "<":
                dx, dy = 0, -1
            elif c == "v":
                dx, dy = 1, 0

            next_symb = grid[px + dx][py + dy]
            if next_symb == '#':
                continue
            elif next_symb in ['[', ']']:
                blocks = find_block_to_move(grid, px + dx, py + dy, dx, dy)
                if not blocks: # impossible move
                    continue
                blocks = sorted(blocks, reverse=(dy > 0) or (dx > 0))
                for (lx, ly, rx, ry) in blocks:
                    grid[lx][ly] = '.'
                    grid[rx][ry] = '.'
                    grid[lx + dx][ly + dy] = '['
                    grid[rx + dx][ry + dy] = ']'
            grid[px][py] = '.'
            px, py = px + dx, py + dy
            grid[px][py] = '@'

    return sum([100 * x + y for x in range(len(grid)) for y in range(len(grid[0])) if grid[x][y] == '['])

# END OF SOLUTION
print(f'My answer is {part_1(input)}')
print(f'My answer is {part_2(input)}')
