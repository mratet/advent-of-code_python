from collections import defaultdict

from aocd import get_data
from sympy import isprime

input = get_data(day=23, year=2017).splitlines()


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    registers = defaultdict(int)
    i, mul_cnt = 0, 0
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
            mul_cnt += 1
        elif op == "jnz" and (isinstance(X, int) or registers[X] != 0):
            i += Y - 1
        i += 1
    return mul_cnt


def part_2(lines):
    # Reverse-engineered from the assembly: "set b <val>", then b = b*100+100000, c = b+17000
    b = int(lines[0].split()[-1]) * 100 + 100_000
    c = b + 17_000
    return sum(not isprime(i) for i in range(b, c + 1, 17))


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
