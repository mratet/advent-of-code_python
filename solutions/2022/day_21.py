import operator

from aocd import get_data
from sympy import Eq, solve, symbols, sympify

input = get_data(day=21, year=2022).splitlines()

OPERATORS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.floordiv,
}
GET_SYMBOL = {v: k for k, v in OPERATORS.items()}


# WRITE YOUR SOLUTION HERE
def parse_input(lines):
    monkeys = {}
    for line in lines:
        name, stuff = line.split(": ")
        if stuff.isdigit():
            monkeys[name] = int(stuff)
        else:
            v1, symbol, v2 = stuff.split()
            monkeys[name] = (OPERATORS[symbol], v1, v2)
    return monkeys


def eval_monkey(monkeys, name):
    val = monkeys[name]
    if isinstance(val, int):
        return val
    op, m1, m2 = val
    return op(eval_monkey(monkeys, m1), eval_monkey(monkeys, m2))


def build_expr(monkeys, name):
    if name == "humn":
        return "X"
    val = monkeys[name]
    if isinstance(val, int):
        return str(val)
    op, m1, m2 = val
    return f"({build_expr(monkeys, m1)} {GET_SYMBOL[op]} {build_expr(monkeys, m2)})"


def solve_puzzle(lines, part="part_1"):
    monkeys = parse_input(lines)
    if part == "part_1":
        return eval_monkey(monkeys, "root")
    _, lm, rm = monkeys["root"]
    equation = Eq(sympify(build_expr(monkeys, lm)), sympify(build_expr(monkeys, rm)))
    return solve(equation, symbols("X"))[0]


def part_1(lines):
    return solve_puzzle(lines)


def part_2(lines):
    return solve_puzzle(lines, "part_2")


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
