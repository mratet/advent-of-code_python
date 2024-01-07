from aocd import get_data
input = get_data(day=14, year=2015).splitlines()

import re
pattern = re.compile(r"(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.")

def compute_distances(time, input):
    distances = []
    for line in input:
        speed, fly_time, rest_time = list(map(int, pattern.findall(line)[0][1:]))
        total_time = fly_time + rest_time
        cycle, r = time // total_time, time % total_time
        distance = cycle * speed * fly_time + min(r, fly_time) * speed
        distances.append(distance)
    return distances

def part_1(input):
    return max(compute_distances(2503, input))
def part_2(input):
    end_time = 2503
    scores = [0] * 10
    for time in range(1, end_time + 1):
        distances = compute_distances(time, input)
        index = distances.index(max(distances))
        scores[index] += 1
    return max(scores)


print(f'My answer is {part_1(input)}')
print(f'My answer is {part_2(input)}')
