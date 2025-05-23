from aocd import get_data

aoc_input = get_data(day=18, year=2019).splitlines()


# WRITE YOUR SOLUTION HERE
def parse_input(lines):
    dots, doors, keys = [], {}, {}
    for x in range(len(lines)):
        for y in range(len(lines)):
            symb = lines[x][y]
            if symb == "#":
                continue
            elif symb == "@":
                entrance = (x, y)
            elif symb == ".":
                dots.append((x, y))
            elif symb.islower():
                keys[symb] = (x, y)
            else:
                doors[symb] = (x, y)
    return entrance, dots, doors, keys


def part_1(lines):
    start, dots, doors, keys = parse_input(lines)
    return


def part_2(lines):
    return


# END OF SOLUTION
print(f"My answer is {part_1(aoc_input)}")
# submit(part_1(aoc_input), part="a", day=18, year=2019)
print(f"My answer is {part_2(aoc_input)}")
# submit(part_2(aoc_input), part="b", day=18, year=2019)
