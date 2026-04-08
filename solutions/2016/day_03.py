from aocd import get_data

input = get_data(day=3, year=2016).splitlines()


def valid_triangle(val):
    a, b, c = sorted(val)
    return a + b > c


def solve(input, part):
    matrix = [map(int, line.split()) for line in input]
    triangles = (
        matrix
        if part == "part_1"
        else [col[i : i + 3] for col in zip(*matrix, strict=False) for i in range(0, len(matrix), 3)]
    )
    return sum(valid_triangle(t) for t in triangles)


def part_1(input):
    return solve(input, "part_1")


def part_2(input):
    return solve(input, "part_2")


print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
