from aocd import get_data

input = get_data(day=10, year=2024).splitlines()

DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]


# WRITE YOUR SOLUTION HERE
def traverse(start, lines, part="part_1"):
    distinct_trails = 0
    endpoint = set()
    to_visit = [start]
    while to_visit:
        x, y = to_visit.pop()
        h = int(lines[x][y])
        if h == 9:
            endpoint.add((x, y))
            distinct_trails += 1
            continue
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(lines) and 0 <= ny < len(lines[0]) and int(lines[nx][ny]) == h + 1:
                to_visit.append((nx, ny))
    return len(endpoint) if part == "part_1" else distinct_trails


def solve(lines, part="part_1"):
    return sum(
        traverse((x, y), lines, part) for x in range(len(lines)) for y in range(len(lines[0])) if lines[x][y] == "0"
    )


def part_1(lines):
    return solve(lines)


def part_2(lines):
    return solve(lines, part="part_2")


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
