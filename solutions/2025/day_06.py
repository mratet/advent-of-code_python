from functools import reduce
from itertools import zip_longest
from operator import add, mul

from aocd import get_data

input = get_data(day=6, year=2025).splitlines()

OPS = {"+": add, "*": mul}


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    ops = lines[-1].split()
    columns = [line.split() for line in lines[:-1]]
    return sum(reduce(OPS[op], map(int, vals)) for op, *vals in zip(ops, *columns, strict=False))


def part_2(lines):
    columns = ["".join(col).strip() for col in zip_longest(*lines, fillvalue=" ")]
    total = 0
    current = 0
    op = add

    for token in columns:
        if not token:
            total += current
            current = 0
        elif token[-1] in OPS:
            op = OPS[token[-1]]
            current = int(token[:-1])
        else:
            current = op(current, int(token))

    return total + current


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
