from collections import defaultdict, deque
import heapq

from aocd import get_data

input = get_data(day=7, year=2018).splitlines()


def parse_input(lines):
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    for line in lines:
        line = line.split()
        before, after = line[1], line[-3]
        graph[before].append(after)
        in_degree[after] += 1
    return graph, in_degree


def solve(graph, in_degree, worker_count, step_length):
    workers = [0] * worker_count
    in_progress = [""] * worker_count
    total_sec = 0

    tasks = list(graph.keys())
    queue = [t for t in tasks if in_degree[t] == 0]
    heapq.heapify(queue)
    order = []

    while True:
        for worker_id, worker in enumerate(workers):
            if worker:
                continue
            if queue:
                current = heapq.heappop(queue)
                workers[worker_id] = step_length(current)
                in_progress[worker_id] = current

        if all(worker == 0 for worker in workers):
            break

        for worker_id in range(worker_count):
            if workers[worker_id] > 0:
                workers[worker_id] -= 1

        total_sec += 1

        for worker_id, worker in enumerate(workers):
            current = in_progress[worker_id]
            if worker == 0 and current:
                order.append(current)
                in_progress[worker_id] = ""
                for neighbor in graph[current]:
                    in_degree[neighbor] -= 1
                    if in_degree[neighbor] == 0:
                        heapq.heappush(queue, neighbor)

    return total_sec, "".join(order)


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    graph, in_degree = parse_input(lines)
    step_length = lambda x: 1
    _, step_order = solve(graph, in_degree, 1, step_length)
    return step_order


def part_2(lines):
    graph, in_degree = parse_input(lines)
    step_length = lambda x: 60 + ord(x) - ord("A") + 1
    tot_seconds, _ = solve(graph, in_degree, 5, step_length)
    return tot_seconds


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
