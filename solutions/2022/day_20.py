from aocd import get_data

input = get_data(day=20, year=2022)


# WRITE YOUR SOLUTION HERE
def mix_signal(signal, steps=1):
    n = len(signal)
    original_ids = list(signal.keys())
    next_ids = original_ids.copy()
    for _ in range(steps):
        for i in original_ids:
            signal_value = signal[i]
            curr_idx = next_ids.index(i)
            next_ids.pop(curr_idx)
            new_idx = (curr_idx + signal_value) % (n - 1)
            next_ids.insert(new_idx, i)
    return [signal[i] for i in next_ids]


def compute_grove_coordinates(signal):
    n = len(signal)
    idx = signal.index(0)
    return sum(signal[(idx + nb) % n] for nb in (1000, 2000, 3000))


def solve(lines, part="part_1"):
    numbers = list(map(int, lines.splitlines()))
    if part == "part_2":
        numbers = [x * 811589153 for x in numbers]
    signal = dict(enumerate(numbers))
    steps = 1 if part == "part_1" else 10
    return compute_grove_coordinates(mix_signal(signal, steps))


def part_1(lines):
    return solve(lines)


def part_2(lines):
    return solve(lines, "part_2")


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
