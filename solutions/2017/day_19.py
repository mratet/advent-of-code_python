from aocd import get_data, submit

input = get_data(day=19, year=2017).splitlines()


# WRITE YOUR SOLUTION HERE
def network_routine(lines):
    cx, cy = 0, lines[0].index("|")
    dx, dy = 1, 0
    password = ""
    cnt = 0
    while True:
        cnt += 1
        cx, cy = cx + dx, cy + dy
        symb = lines[cx][cy]
        if symb not in "-|+":
            password += symb
        if symb == "+":
            if lines[cx - dy][cy + dx] != " ":
                dx, dy = -dy, dx  # Right turn
            elif lines[cx + dy][cy - dx] != " ":
                dx, dy = dy, -dx  # Left turn
        elif symb == " ":
            break

    return password, cnt


def part_1(lines):
    password, _ = network_routine(lines)
    return password


def part_2(lines):
    _, cnt = network_routine(lines)
    return cnt


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
