from sympy import symbols, Eq, solve, sympify
import operator
import re

from aocd import get_data

input = get_data(day=21, year=2022).splitlines()

OPERATORS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.floordiv,
}
GET_SYMBOL = {v: k for k, v in OPERATORS.items()}


def parse_input(lines):
    monkeys = {}
    for monkey in lines:
        monkey_name, stuff = monkey.split(": ")
        if stuff.isdigit():
            monkeys[monkey_name] = int(stuff)
        else:
            v1, symbol, v2 = re.search(r"(\w+) ([+-/*]) (\w+)", stuff).groups()
            monkeys[monkey_name] = (OPERATORS[symbol], v1, v2)
    return monkeys


def eval_monkey(monkeys, monkey):
    val = monkeys[monkey]
    if isinstance(val, int):
        return val
    op, m1, m2 = val
    return op(eval_monkey(monkeys, m1), eval_monkey(monkeys, m2))


def get_full_expression_from_monkey(start_monkey, monkeys):
    to_visit = [start_monkey]
    full_expression = start_monkey
    while to_visit:
        monkey = to_visit.pop(0)
        if monkey == "humn":
            full_expression = full_expression.replace("humn", "X")
        elif isinstance(monkeys[monkey], int):
            full_expression = full_expression.replace(f"{monkey}", str(monkeys[monkey]))
        else:
            op, m1, m2 = monkeys[monkey]
            expression = f"({m1} {GET_SYMBOL[op]} {m2})"
            full_expression = full_expression.replace(f"{monkey}", expression)
            to_visit.append(m1)
            to_visit.append(m2)
    return full_expression


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    monkeys = parse_input(lines)
    return eval_monkey(monkeys, "root")


def part_2(lines):
    monkeys = parse_input(lines)
    _, lm, rm = monkeys["root"]
    lhs = get_full_expression_from_monkey(lm, monkeys)
    rhs = get_full_expression_from_monkey(rm, monkeys)
    equation = Eq(sympify(lhs), sympify(rhs))
    solution = solve(equation, symbols("X"))
    return solution[0]


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
