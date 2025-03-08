from aocd import get_data, submit
aoc_input = get_data(day=16, year=2019)
import numpy as np
# WRITE YOUR SOLUTION HERE
def build_fft(N):
    fft = np.zeros((N, N), dtype=int)
    base_pattern = [0, 1, 0, -1]
    for i in range(N):
        pattern = [val for val in base_pattern for _ in range(i + 1)]
        pattern = np.tile(pattern, (N // len(pattern)) + 1)
        fft[i, :] = pattern[1:N + 1]
    return fft

def part_1(lines):
    signal = np.array([int(s) for s in str(lines)])
    fft = build_fft(len(signal))
    n_phase = 100
    for _ in range(n_phase):
        signal = abs(signal @ fft.T) % 10
    return ''.join([str(n) for n in signal[:8]])

def part_2(lines):
    for i in range(5, 25, 5):
        print(build_fft(i))
        print()
    return

# END OF SOLUTION
print(f'My answer is {part_1(aoc_input)}')
print(f'My answer is {part_2(aoc_input)}')

