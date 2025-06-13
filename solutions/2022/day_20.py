from aocd import get_data

input = get_data(day=20, year=2022)


def compute_grove_coordinates(clean_signal):
    idx = clean_signal.index(0)
    n = len(clean_signal)
    return sum(clean_signal[(idx + nb) % n] for nb in (1000, 2000, 3000))


def mix_signal(signal, steps=1):
    n = len(signal)
    original_ids = list(signal.keys())
    next_ids = original_ids.copy()

    for _ in range(steps):
        for id in original_ids:
            signal_value = signal[id]
            curr_idx = next_ids.index(id)
            next_ids.pop(curr_idx)
            new_idx = (curr_idx + signal_value) % (n - 1)
            next_ids.insert(new_idx, id)

    return [signal[id] for id in next_ids]


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    signal = {id: int(s) for id, s in enumerate(lines.splitlines())}
    signal = mix_signal(signal)
    return compute_grove_coordinates(signal)


def part_2(lines):
    decryption_key = 811589153
    signal = {id: int(s) * decryption_key for id, s in enumerate(lines.splitlines())}
    signal = mix_signal(signal, steps=10)
    return compute_grove_coordinates(signal)


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
