from aocd import get_data

input = get_data(day=7, year=2015).splitlines()

# Solution from r-sreeram
import functools
import operator as op

OPS = {
    "AND": op.and_,
    "OR": op.or_,
    "LSHIFT": op.lshift,
    "RSHIFT": op.rshift,
    "NOT": op.inv,
    "X": lambda x: x,
}

wires = {}
for line in input:
    match line.split():
        case x, "->", w:
            wires[w] = (OPS["X"], x)
        case *lhs, operation, rhs, "->", w:
            wires[w] = (OPS[operation], *lhs, rhs)


@functools.cache
def solve(w):
    if isinstance(w, int) or w[0].isdigit():
        return int(w) & 0xFFFF
    return wires[w][0](*[solve(arg) for arg in wires[w][1:]]) & 0xFFFF


part1 = solve("a")
wires["b"] = (OPS["X"], part1)
solve.cache_clear()
part2 = solve("a")

########################################

print(f"My answer is {part1}")
print(f"My answer is {part2}")
