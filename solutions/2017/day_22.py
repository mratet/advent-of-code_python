from aocd import get_data, submit
input = get_data(day=22, year=2017).splitlines()

# WRITE YOUR SOLUTION HERE
DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
def parse_input(lines):
    infected_nodes = {}
    for x, l in enumerate(lines):
        for y, c in enumerate(l):
            if c == '#':
                infected_nodes[(x, y)] = 'I'
    return infected_nodes

def part_1(lines):
    infected_nodes = parse_input(lines)
    n = len(lines)
    cx, cy = n // 2, n // 2
    idx = 2
    ans = 0
    for _ in range(10000):
        if (cx, cy) in infected_nodes:
            idx -= 1
            infected_nodes.pop((cx, cy))
        else:
            idx += 1
            infected_nodes[(cx, cy)] = 'I'
            ans += 1
        dx, dy = DIRS[idx % len(DIRS)]
        cx, cy = cx + dx, cy + dy

    return ans

def part_2(lines):
    infected_nodes = parse_input(lines)
    n = len(lines)
    cx, cy = n // 2, n // 2
    cs = infected_nodes.get((cx, cy), 'C')
    idx = 2
    ans = 0
    for _ in range(10000000):
        if cs == 'C':
            idx += 1
            infected_nodes[(cx, cy)] = 'W'
        elif cs == 'W':
            idx = idx
            infected_nodes[(cx, cy)] = 'I'
            ans += 1
        elif cs == 'I':
            idx -= 1
            infected_nodes[(cx, cy)] = 'F'
        elif cs == 'F':
            idx += 2
            infected_nodes.pop((cx, cy))
        dx, dy = DIRS[idx % len(DIRS)]
        cx, cy = cx + dx, cy + dy
        cs = infected_nodes.get((cx, cy), 'C')

    return ans
# END OF SOLUTION
print(f'My answer is {part_1(input)}')
print(f'My answer is {part_2(input)}')
