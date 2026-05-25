from aocd import get_data

input = get_data(day=13, year=2023)

# WRITE YOUR SOLUTION HERE


def parse_input(data):
    patterns = []
    for block in data.split("\n\n"):
        rows = block.splitlines()
        cols = ["".join(col) for col in zip(*rows, strict=False)]
        patterns.append((rows, cols))
    return patterns


def check_mirrors(tab, mismatched):
    n, mirror_pos = len(tab), 0
    while mirror_pos < n - 1:
        mismatch_count, offset = 0, 0
        while mirror_pos - offset >= 0 and mirror_pos + offset + 1 <= n - 1:
            mismatch_count += sum(
                x != y for x, y in zip(tab[mirror_pos + 1 + offset], tab[mirror_pos - offset], strict=False)
            )
            offset += 1
        if mismatch_count == mismatched:
            return mirror_pos + 1
        mirror_pos += 1
    return 0


def solve(data, part="part_1"):
    mismatched = 1 if part == "part_2" else 0
    return sum(
        check_mirrors(rows, mismatched) * 100 + check_mirrors(cols, mismatched) for rows, cols in parse_input(data)
    )


def part_1(data):
    return solve(data)


def part_2(data):
    return solve(data, part="part_2")


# END OF SOLUTION


print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
