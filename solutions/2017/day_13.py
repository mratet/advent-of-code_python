from aocd import get_data

input = get_data(day=13, year=2017).splitlines()


# WRITE YOUR SOLUTION HERE
def get_security_scanner(lines):
    L = [0] * 100
    for l in lines:
        depth, R = l.split(": ")
        L[int(depth)] = int(R)
    return L


def part_1(lines):
    L = get_security_scanner(lines)
    return sum([i * L[i] for i in range(100) if L[i] and i % (2 * (L[i] - 1)) == 0])


def easy_path(C, L):
    for i in range(100):
        if L[i] and (C + i) % (2 * (L[i] - 1)) == 0:
            return False
    return True


def part_2(lines):
    L = get_security_scanner(lines)
    c = 0
    while True:
        if easy_path(c, L):
            break
        c += 1
    return c


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
