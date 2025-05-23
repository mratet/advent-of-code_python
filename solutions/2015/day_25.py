import re
from aocd import get_data

input = get_data(day=25, year=2015)


def get_coord(r, c):
    # (1, n) -> n (n + 1) / 2
    # (m, 1) -> 1 + m (m - 1) / 2
    # r + c gives our diagonal number
    N = r + c - 1
    start_c = 1 + N * (N - 1) // 2
    return start_c + c - 1


def part_1(input):
    pattern = r"(\d+)+"
    matchs = re.findall(pattern, input)
    r, c = int(matchs[0]), int(matchs[1])
    n = get_coord(r, c)

    state = 20151125
    for _ in range(n - 1):
        state = (state * 252533) % 33554393

    return state


print(f"My answer is {part_1(input)}")
