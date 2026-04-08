from aocd import get_data

input = get_data(day=16, year=2016)


def dragon_curve(a):
    b = "".join("0" if c == "1" else "1" for c in reversed(a))
    return a + "0" + b


def checksum(s):
    while len(s) % 2 == 0:
        s = "".join("1" if s[i] == s[i + 1] else "0" for i in range(0, len(s), 2))
    return s


def solve(input, n):
    s = input
    while len(s) < n:
        s = dragon_curve(s)
    return checksum(s[:n])


def part_1(input):
    return solve(input, 272)


def part_2(input):
    return solve(input, 35651584)


print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
