from aocd import get_data
from operator import add, mul
from functools import reduce
from itertools import zip_longest

input = get_data(day=6, year=2025).splitlines()


# WRITE YOUR SOLUTION HERE
OPS = {'+': add, '*': mul}

def part_1(lines):
    ops = lines[-1].split()
    columns = [line.split() for line in lines[:-1]]
    return sum(reduce(OPS[op], map(int, vals)) for op, *vals in zip(ops, *columns))


def part_2(lines):
    columns = [''.join(col).strip() for col in zip_longest(*lines, fillvalue=' ')]
    total, current, op = 0, None, None

    for token in columns:
        if not token:
            total += current
            current = None

        elif token[-1] in OPS:
            op = OPS[token[-1]]
            current = int(token[:-1])
        else:
            current = op(current, int(token))

    return total + (current or 0)

# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
