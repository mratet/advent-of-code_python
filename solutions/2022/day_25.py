from aocd import get_data

input = get_data(day=25, year=2022).splitlines()

SNAFU = "=-012"
SNAFU_VAL = {c: i - 2 for i, c in enumerate(SNAFU)}


# WRITE YOUR SOLUTION HERE
def snafu_to_decimal(snafu):
    return sum(5**i * SNAFU_VAL[c] for i, c in enumerate(reversed(snafu)))


def decimal_to_snafu(n):
    digits = []
    while n:
        n, r = divmod(n + 2, 5)
        digits.append(SNAFU[r])
    return "".join(reversed(digits))


def part_1(lines):
    return decimal_to_snafu(sum(map(snafu_to_decimal, lines)))


def part_2(lines):
    return


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
