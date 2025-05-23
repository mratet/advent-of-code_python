from aocd import get_data, submit

input = get_data(day=15, year=2017).splitlines()


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    N = 40000000
    A = int(lines[0].split()[-1])
    B = int(lines[1].split()[-1])
    ans = 0
    for i in range(N):
        A = (A * 16807) % 2147483647
        B = (B * 48271) % 2147483647
        if (A - B) % 2**16 == 0:
            ans += 1
    return ans


def get_next_value(current_value, C, mod):
    current_value = (current_value * C) % 2147483647
    while current_value % mod != 0:
        current_value = (current_value * C) % 2147483647
    return current_value


def part_2(lines):
    N = 5000000
    A = int(lines[0].split()[-1])
    B = int(lines[1].split()[-1])
    ans = 0
    for i in range(N):
        A = get_next_value(A, 16807, 4)
        B = get_next_value(B, 48271, 8)
        assert A % 4 == 0 and B % 8 == 0
        if (A - B) % 2**16 == 0:
            ans += 1
    return ans


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
