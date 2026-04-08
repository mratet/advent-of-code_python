from hashlib import md5

from aocd import get_data

input = get_data(day=5, year=2016)


def find_password(input, part="part_1"):
    password, count, i = [""] * 8, 0, 0
    base = md5(input.encode())
    while not all(password):
        h = base.copy()
        h.update(str(i).encode())
        digest = h.digest()
        if digest[0] == 0 and digest[1] == 0 and digest[2] < 16:
            c = f"{digest[2]:x}"

            if part == "part_1":
                password[count] = c
                count += 1
            elif c.isdigit() and int(c) < 8 and password[int(c)] == "":
                password[int(c)] = f"{digest[3] >> 4:x}"
        i += 1

    return "".join(password)


def part_1(input):
    return find_password(input, "part_1")


def part_2(input):
    return find_password(input, "part_2")


print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
