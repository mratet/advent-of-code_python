from aocd import get_data
import numpy as np

aoc_input = get_data(day=16, year=2019)

NUM_REPETITIONS = 10_000
N_PHASE = 100


# WRITE YOUR SOLUTION HERE
def build_fft(N):
    fft = np.zeros((N, N), dtype=int)
    base_pattern = [0, 1, 0, -1]
    for i in range(N):
        pattern = [val for val in base_pattern for _ in range(i + 1)]
        pattern = np.tile(pattern, (N // len(pattern)) + 1)
        fft[i, :] = pattern[1 : N + 1]
    return fft


def part_1(lines):
    signal = np.array([int(s) for s in str(lines)])
    fft = build_fft(len(signal))
    for _ in range(N_PHASE):
        signal = abs(signal @ fft.T) % 10
    return "".join([str(n) for n in signal[:8]])


def part_2(lines):
    offset = int(lines[:7])
    total_signal_length = len(lines) * NUM_REPETITIONS
    # [...start####][####][####]...
    start, repeat = offset % len(lines), (total_signal_length - offset) // len(lines)
    signal = np.array([int(s) for s in str(lines)])
    repeated_signal = np.tile(signal, repeat + 1)

    cumsum_from_right = lambda x: x[::-1].cumsum()[::-1]
    # In low frequencies (i.e right part of the fft), we're only averaging values
    for _ in range(N_PHASE):
        repeated_signal = abs(cumsum_from_right(repeated_signal)) % 10
    return "".join([str(d) for d in repeated_signal[start : start + 8]])


# END OF SOLUTION
print(f"My answer is {part_1(aoc_input)}")
print(f"My answer is {part_2(aoc_input)}")
