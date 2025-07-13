from aocd import get_data
import re

input = get_data(day=17, year=2018).splitlines()


def parse_input(lines):
    clay = set()
    for line in lines:
        n1, n2, n3 = map(int, re.findall(r"\d+", line))
        if line[0] == "x":
            for y in range(n2, n3 + 1):
                clay.add((n1, y))
        elif line[0] == "y":
            for x in range(n2, n3 + 1):
                clay.add((x, n1))
    return clay


def flow(clay, abyss_limit):
    from collections import deque

    source = (500, 0)
    flowing = set()
    still = set()
    queue = deque([source])
    seen = set()

    def is_blocked(p):
        return p in clay or p in still

    while queue:
        x, y = queue.popleft()
        if (x, y) in seen:
            continue
        seen.add((x, y))

        while y <= abyss_limit and not is_blocked((x, y + 1)):
            y += 1
            if (x, y) in seen:
                break
            flowing.add((x, y))
            seen.add((x, y))

        if y > abyss_limit:
            continue

        while True:
            left, right = x, x

            while (left - 1, y) not in clay and is_blocked((left, y + 1)):
                left -= 1

            while (right + 1, y) not in clay and is_blocked((right, y + 1)):
                right += 1

            bounded = (left - 1, y) in clay and (right + 1, y) in clay
            if not bounded:
                break
            still.update((xi, y) for xi in range(left, right + 1))
            y -= 1

        flowing.update((xi, y) for xi in range(left, right + 1))

        for edge_x in (left, right):
            below = (edge_x, y + 1)
            if below not in clay and below not in still:
                queue.append((edge_x, y))

    return flowing, still


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    clay = parse_input(lines)
    min_y = min(y for _, y in clay)
    max_y = max(y for _, y in clay)
    flowing, still = flow(clay, max_y)
    return sum(min_y <= y <= max_y for _, y in flowing | still)


def part_2(lines):
    clay = parse_input(lines)
    min_y = min(y for _, y in clay)
    max_y = max(y for _, y in clay)
    _, still = flow(clay, max_y)
    return sum(min_y <= y <= max_y for _, y in still)


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
