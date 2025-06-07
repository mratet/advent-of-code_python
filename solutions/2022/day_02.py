from aocd import get_data

input = get_data(day=2, year=2022).splitlines()

to_num = {"A": 0, "X": 0, "B": 1, "Y": 1, "C": 2, "Z": 2}


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    score1 = 0
    for line in lines:
        a, b = map(to_num.get, line.split())
        outcome = (b - a) % 3
        # 0: draw, 1: win, 2: loss
        score1 += [3, 6, 0][outcome] + b + 1
    return score1


def part_2(lines):
    score2 = 0
    for line in lines:
        a, result = line.split()
        a = to_num[a]
        # result: X = lose, Y = draw, Z = win
        outcome = {"X": (a - 1) % 3, "Y": a, "Z": (a + 1) % 3}[result]
        score2 += {"X": 0, "Y": 3, "Z": 6}[result] + outcome + 1
    return score2


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
