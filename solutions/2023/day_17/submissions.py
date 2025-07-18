lines = open("input.txt").read().splitlines()

# WRITE YOUR SOLUTION HERE

from heapq import heappop, heappush

N, S, W, E = (0, -1), (0, 1), (-1, 0), (1, 0)


def dijkstra(graph, source, target, part):
    # Little bug here, try either S or E
    heap = [(0, source, E, -1)]
    visited = {}

    while heap:
        dist, node, dir_, cnt_dir_ = heappop(heap)
        if (node, dir_, cnt_dir_) in visited:
            continue
        visited[(node, dir_, cnt_dir_)] = dist

        for new_dir in [N, S, W, E]:
            next_node = (node[0] + new_dir[0], node[1] + new_dir[1])
            new_cnt_dir = 1 if new_dir != dir_ else cnt_dir_ + 1
            isnt_reverse = dir_[0] * new_dir[0] + dir_[1] * new_dir[1] != -1

            match part:
                case "part_1":
                    isvalid = new_cnt_dir <= 3
                case "part_2":
                    isvalid = new_cnt_dir <= 10 and (
                        new_dir == dir_ or cnt_dir_ >= 4 or cnt_dir_ == -1
                    )

            if next_node in graph and isnt_reverse and isvalid:
                cost = graph[next_node]
                heappush(heap, (dist + cost, next_node, new_dir, new_cnt_dir))

    return min([v for (node, _, _), v in visited.items() if node == target])


def _parse(input):
    graph = {(x, y): int(c) for y, line in enumerate(input) for x, c in enumerate(line)}
    return graph


def part_1(input):
    graph = _parse(input)
    n, m = len(input), len(input[0])

    return dijkstra(graph, (0, 0), (m - 1, n - 1), "part_1")


def part_2(input):
    graph = _parse(input)
    n, m = len(input), len(input[0])

    return dijkstra(graph, (0, 0), (m - 1, n - 1), "part_2")


# END OF SOLUTION


test_input = open("input-test.txt").read().splitlines()
test_lines = []
for i, line in enumerate(test_input[3:]):
    if line[0] == "-":
        break
    test_lines.append(line)
solution = test_input[i + 4]

print(f"My answer on test set for the first problem is {part_1(test_lines)}")
print(solution)
print(f"My answer is {part_1(lines)}")

print(f"My answer on test set for the second problem is {part_2(test_lines)}")
print(f"My answer is {part_2(lines)}")
