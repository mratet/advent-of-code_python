from aocd import get_data

input = get_data(day=19, year=2017).splitlines()


# WRITE YOUR SOLUTION HERE
def network_routine(lines):
    row, col = 0, lines[0].index("|")
    drow, dcol = 1, 0
    letters, steps = "", 0
    turn_right = lambda dx, dy: (-dy, dx)
    turn_left = lambda dx, dy: (dy, -dx)

    while True:
        steps += 1
        row, col = row + drow, col + dcol
        char = lines[row][col]

        if char == " ":
            break

        if char == "+":
            rdrow, rdcol = turn_right(drow, dcol)
            if lines[row + rdrow][col + rdcol] != " ":
                drow, dcol = rdrow, rdcol
            else:
                drow, dcol = turn_left(drow, dcol)
        elif char not in "-|+":
            letters += char

    return letters, steps


def part_1(lines):
    letters, _ = network_routine(lines)
    return letters


def part_2(lines):
    _, steps = network_routine(lines)
    return steps


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
