from aocd import get_data

input = get_data(day=22, year=2023).splitlines()

# WRITE YOUR SOLUTION HERE
from collections import deque


def _parse(input):
    bricks = []
    for line in input:
        start, end = line.split("~")
        start = [int(c) for c in start.split(",")]
        end = [int(c) for c in end.split(",")]
        bricks.append([start, end])

    return bricks


def support_graph(bricks):
    len_basis = 10
    basis = {(x, y): (0, -1) for x in range(len_basis) for y in range(len_basis)}

    is_supported_by = [[] for _ in range(len(bricks) + 1)]

    for i, [(x_s, y_s, z_s), (x_e, y_e, z_e)] in enumerate(bricks):
        if x_s == x_e and y_s == y_e:
            is_supported_by[i + 1].append(basis[(x_e, y_e)][1])
            basis[(x_s, y_s)] = (basis[(x_s, y_s)][0] + z_e - z_s + 1, i)

        elif x_s == x_e:
            z_max = max([basis[(x_e, y)][0] for y in range(y_s, y_e + 1)])
            for y in range(y_s, y_e + 1):
                if (
                    basis[(x_e, y)][0] == z_max
                    and basis[(x_e, y)][1] not in is_supported_by[i + 1]
                ):
                    is_supported_by[i + 1].append(basis[(x_e, y)][1])
                basis[(x_e, y)] = (z_max + 1, i)

        elif y_s == y_e:
            z_max = max([basis[(x, y_e)][0] for x in range(x_s, x_e + 1)])
            for x in range(x_s, x_e + 1):
                if (
                    basis[(x, y_e)][0] == z_max
                    and basis[(x, y_e)][1] not in is_supported_by[i + 1]
                ):
                    is_supported_by[i + 1].append(basis[(x, y_e)][1])
                basis[(x, y_e)] = (z_max + 1, i)
        else:
            print("There are square in the input !")

    return is_supported_by


def part_1(lines):
    bricks = _parse(lines)
    bricks.sort(key=lambda x: x[0][2])

    is_supported_by = support_graph(bricks)

    not_safe = [False for _ in range(len(bricks))]

    for tab in is_supported_by:
        if len(tab) == 1 and tab[0] != -1:
            not_safe[tab[0]] = True

    return len(bricks) - sum(not_safe)


def dfs(start, graph):
    visited = set()
    q = deque()
    q.append(start)

    while q:
        node = q.popleft()
        visited.add(node)

        for neighboor in graph[node]:
            if neighboor not in visited:
                q.append(neighboor)

    return len(visited)


def part_2(input):
    bricks = _parse(input)
    bricks.sort(key=lambda x: x[0][2])

    is_supported_by = support_graph(bricks)

    not_safe = [False for _ in range(len(bricks))]
    print(is_supported_by)

    support = [[] for _ in range(len(bricks) + 1)]
    for i, tab in enumerate(is_supported_by):
        for neighboor in tab:
            support[neighboor + 1].append(i - 1)

    for tab in is_supported_by:
        if len(tab) == 1 and tab[0] != -1:
            not_safe[tab[0]] = True
    ans = 0
    print(support)
    print(not_safe)
    for i in range(len(not_safe)):
        if not not_safe[i]:
            ans += dfs(i + 1, support)
    print(dfs(0, support))

    return ans


# END OF SOLUTION


print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
