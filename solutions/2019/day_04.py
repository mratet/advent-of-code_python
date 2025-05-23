from aocd import get_data

input = get_data(day=4, year=2019)
# WRITE YOUR SOLUTION HERE


def part_1(lines):
    adjacent_digit = lambda s: any(s[i] == s[i + 1] for i in range(len(s) - 1))
    increasing_order = lambda s: all(s[i] <= s[i + 1] for i in range(len(s) - 1))
    l, r = map(int, input.split("-"))
    return sum(
        1 for n in range(l, r) if adjacent_digit(str(n)) and increasing_order(str(n))
    )


def part_2(lines):
    small_cluster = lambda s: any(
        s[i + 1] == s[i + 2] and s[i] != s[i + 1] and s[i + 2] != s[i + 3]
        for i in range(len(s) - 3)
    )
    increasing_order = lambda s: all(s[i] <= s[i + 1] for i in range(len(s) - 1))
    l, r = map(int, input.split("-"))
    return sum(
        1
        for n in range(l, r)
        if small_cluster("-" + str(n) + "-") and increasing_order(str(n))
    )


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
