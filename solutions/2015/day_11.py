from aocd import get_data
input = get_data(day=11, year=2015)


def part_1(password):

    sequence = lambda s: any(ord(a) + 2 == ord(b) + 1 == ord(c) for a, b, c in zip(s, s[1:], s[2:]))
    doublets = lambda s: len(set(a for a, b in zip(password, password[1:]) if a == b)) > 1

    while True:
        password = password.rstrip("z")

        if password:
            index, char = next(((i, c) for i, c in enumerate(password) if c in "ilo"), (-1, password[-1]))
            password = password[0:index] + ("jmp"[q] if (q := "hkn".find(char)) != -1 else chr(ord(char) + 1))

        password = password.ljust(8, "a")

        if sequence(password) and doublets(password):
            return password

def part_2(password):
    return part_1(part_1(password))

print(f'My answer is {part_1(input)}')
print(f'My answer is {part_2(input)}')
