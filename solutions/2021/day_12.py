from collections import defaultdict

from aocd import get_data

input = get_data(day=12, year=2021).splitlines()


# WRITE YOUR SOLUTION HERE
def parse_input(lines):
    graph = defaultdict(list)
    for line in lines:
        s, e = line.split("-")
        graph[s].append(e)
        graph[e].append(s)
    return graph


def solve(lines, part="part_1"):
    graph = parse_input(lines)

    def dfs(node, visited, double_used):
        if node == "end":
            return 1
        total = 0
        for next_node in graph[node]:
            if next_node == "start":
                continue
            if next_node.islower() and next_node in visited:
                if not double_used:
                    total += dfs(next_node, visited, True)
            else:
                new_visited = visited | {next_node} if next_node.islower() else visited
                total += dfs(next_node, new_visited, double_used)
        return total

    return dfs("start", {"start"}, part == "part_1")


def part_1(lines):
    return solve(lines, "part_1")


def part_2(lines):
    return solve(lines, "part_2")


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
