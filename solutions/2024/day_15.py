from aocd import get_data, submit

input = get_data(day=15, year=2024).split("\n\n")

# WRITE YOUR SOLUTION HERE
DIRS = {"^": (-1, 0), "v": (1, 0), ">": (0, 1), "<": (0, -1)}


def possible_move(mapping, x, y, dx, dy):
    next = mapping[x + dx][y + dy]
    if next == ".":
        mapping[x + dx][y + dy] = "O"
        return True, mapping
    elif next == "#":
        return False, mapping
    elif next == "O":
        return possible_move(mapping, x + dx, y + dy, dx, dy)


def part_1(lines):
    grid = [list(l) for l in lines[0].split()]
    [(px, py)] = [
        (x, y)
        for x in range(len(grid))
        for y in range(len(grid[0]))
        if grid[x][y] == "@"
    ]
    moves = lines[1]

    for line in moves.split("\n"):
        for dir in line:
            dx, dy = DIRS[dir]
            move_bool, new_grid = possible_move(grid, px, py, dx, dy)
            if move_bool:
                new_grid[px][py] = "."
                px += dx
                py += dy
                new_grid[px][py] = "@"
                grid = new_grid
    return sum(
        [
            100 * x + y
            for x in range(len(grid))
            for y in range(len(grid[0]))
            if grid[x][y] == "O"
        ]
    )


def find_block_to_move(grid, x, y, dx, dy):
    symb = grid[x][y]
    block = (x, y, x, y + 1) if symb == "[" else (x, y - 1, x, y)
    all_blocks = [block]
    cand = [block]
    while cand:
        lx, ly, rx, ry = cand.pop()
        for cx, cy in [(lx, ly), (rx, ry)]:
            sign = grid[cx + dx][cy + dy]
            cc = None
            if sign == "#":
                return []
            elif sign == "[":
                cc = (cx + dx, cy + dy, cx + dx, cy + dy + 1)
            elif sign == "]":
                cc = (cx + dx, cy + dy - 1, cx + dx, cy + dy)
            if cc:
                if cc in all_blocks:
                    continue
                all_blocks.append(cc)
                cand.append(cc)
    return all_blocks


def part_2(lines):
    grid = [
        list(
            row.replace("#", "##")
            .replace("O", "[]")
            .replace(".", "..")
            .replace("@", "@.")
        )
        for row in lines[0].split()
    ]
    [(px, py)] = [
        (x, y)
        for x in range(len(grid))
        for y in range(len(grid[0]))
        if grid[x][y] == "@"
    ]
    moves = lines[1]

    for line in moves.split("\n"):
        for c in line:
            dx, dy = DIRS[c]
            next_symb = grid[px + dx][py + dy]
            if next_symb == "#":
                continue
            elif next_symb in ["[", "]"]:
                blocks = find_block_to_move(grid, px + dx, py + dy, dx, dy)
                if not blocks:  # impossible move
                    continue
                blocks = sorted(blocks, reverse=(dy > 0) or (dx > 0))
                for lx, ly, rx, ry in blocks:
                    grid[lx][ly] = "."
                    grid[rx][ry] = "."
                    grid[lx + dx][ly + dy] = "["
                    grid[rx + dx][ry + dy] = "]"
            grid[px][py] = "."
            px, py = px + dx, py + dy
            grid[px][py] = "@"

    return sum(
        [
            100 * x + y
            for x in range(len(grid))
            for y in range(len(grid[0]))
            if grid[x][y] == "["
        ]
    )


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
