from aocd import get_data

input = get_data(day=14, year=2018)


def compute_scoreboard(N):
    scoreboard = [3, 7]

    elf1 = 0
    elf2 = 1
    for _ in range(N + 20):
        next_recipe = scoreboard[elf1] + scoreboard[elf2]
        if next_recipe > 9:
            scoreboard.append(next_recipe // 10)
        scoreboard.append(next_recipe % 10)

        elf1 = (elf1 + 1 + scoreboard[elf1]) % len(scoreboard)
        elf2 = (elf2 + 1 + scoreboard[elf2]) % len(scoreboard)
    return "".join(map(str, scoreboard))


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    N = int(lines)
    scoreboard = compute_scoreboard(N)
    return scoreboard[N : N + 10]


def part_2(lines):
    N = int(lines)
    scoreboard = compute_scoreboard(50 * N)
    return scoreboard.index(str(N))


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
