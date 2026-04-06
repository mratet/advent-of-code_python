from aocd import get_data

input = get_data(day=2, year=2015).splitlines()


def area(l, w, h):
    return 2 * l * w + 2 * w * h + 2 * l * h + min(w * l, w * h, l * h)


def ribbon_area(l, w, h):
    a, b, _ = sorted([l, w, h])
    return l * w * h + 2 * a + 2 * b


def solve(input, part="part_1"):
    surface_func = area if part == "part_1" else ribbon_area
    return sum(surface_func(*map(int, line.split("x"))) for line in input)


def part_1(input):
    return solve(input, part="part_1")


def part_2(input):
    return solve(input, part="part_2")


print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
