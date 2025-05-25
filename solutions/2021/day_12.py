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


def is_valid_path(next_path, part="part_1"):
    small_caves = {cave for cave in next_path if cave.islower()}
    if part == "part_1":
        return not any(next_path.count(cave) > 1 for cave in small_caves)
    elif part == "part_2":
        double_visit = [cave for cave in small_caves if next_path.count(cave) > 1]
        if len(double_visit) > 1:
            return False
        if len(double_visit) == 0:
            return True
        double_cave = double_visit[0]
        if double_cave in ("start", "end"):
            return False
        return next_path.count(double_cave) == 2
    return None


def solve(lines, part):
    graph = parse_input(lines)
    paths = []

    def dfs(current_path):
        last_node = current_path[-1]
        if last_node == "end":
            paths.append(current_path)
            return
        for next_node in graph[last_node]:
            next_path = current_path + [next_node]
            if is_valid_path(next_path, part):
                dfs(next_path)

    dfs(["start"])
    return len(paths)


def part_1(lines):
    return solve(lines, "part_1")


def part_2(lines):
    return solve(lines, "part_2")


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
