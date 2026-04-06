from functools import reduce
from itertools import zip_longest
from operator import add, mul

from aocd import get_data

input = get_data(day=6, year=2025).splitlines()


# WRITE YOUR SOLUTION HERE
OPS = {"+": add, "*": mul}


def part_1(lines):
    ops = lines[-1].split()
    columns = [line.split() for line in lines[:-1]]
    return sum(reduce(OPS[op], map(int, vals)) for op, *vals in zip(ops, *columns, strict=False))


def part_2(lines):
    columns = ["".join(col).strip() for col in zip_longest(*lines, fillvalue=" ")]
    total = 0
    current: int | None = None
    op = add

    for token in columns:
        if not token:
            assert current is not None
            total += current
            current = None

        elif token[-1] in OPS:
            op = OPS[token[-1]]
            current = int(token[:-1])
        else:
            assert current is not None
            current = op(current, int(token))

    return total + (current or 0)


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
