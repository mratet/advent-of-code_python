from aocd import get_data

input = get_data(day=23, year=2017).splitlines()


def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0 or n % 3 == 0:
        return False
    if n < 9:
        return True
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n % f == 0:
            return False
        if n % (f + 2) == 0:
            return False
        f += 6
    return True


from collections import defaultdict


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    i = 0
    registers = defaultdict(int)
    ans = 0
    while i < len(lines):
        op, X, Y = lines[i].split()
        X = int(X) if X.lstrip("-").isdigit() else X
        Y = int(Y) if Y.lstrip("-").isdigit() else registers[Y]

        if op == "set":
            registers[X] = Y
        elif op == "sub":
            registers[X] -= Y
        elif op == "mul":
            registers[X] *= Y
            ans += 1
        elif op == "jnz":
            if type(X) == int or registers[X] != 0:
                i += Y - 1
        i += 1
    return ans


def part_2(lines):
    # You have to add your own value here, look at the program initialisation
    b = 106700
    c = 123700
    ans = 0
    for i in range(b, c + 1, 17):
        if not is_prime(i):
            ans += 1
    return ans


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
