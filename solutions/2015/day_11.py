import itertools

from aocd import get_data

input = get_data(day=11, year=2015)

FORBIDDEN = "ilo"


def get_next_password(password):
    has_straight = lambda s: any(ord(a) + 2 == ord(b) + 1 == ord(c) for a, b, c in zip(s, s[1:], s[2:], strict=False))
    has_two_pairs = lambda s: len({a for a, b in itertools.pairwise(s) if a == b}) >= 2
    next_char = lambda c: chr(ord(c) + 1)

    while True:
        password = password.rstrip("z")
        idx, char_to_change = next(((i, c) for i, c in enumerate(password) if c in FORBIDDEN), (-1, password[-1]))
        password = password[:idx] + next_char(char_to_change)
        password = password.ljust(8, "a")
        if has_straight(password) and has_two_pairs(password):
            return password


def part_1(password):
    return get_next_password(password)


def part_2(password):
    return get_next_password(get_next_password(password))


print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
