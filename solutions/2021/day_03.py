from aocd import get_data
from collections import Counter

input = get_data(day=3, year=2021).splitlines()

# WRITE YOUR SOLUTION HERE
def part_1(lines):
    transposed_bits = ["".join(seq) for seq in zip(*lines)]
    N = len(transposed_bits)
    gamma_rate = int("".join(Counter(bits).most_common(1)[0][0] for bits in transposed_bits), 2)
    return gamma_rate * (2 ** N - 1 - gamma_rate)

def part_2(lines):
    def filter_by_bit_criteria(candidates, position, keep_most_common):
        bit_counts = Counter(bit[position] for bit in candidates)
        ones, zeros = bit_counts['1'], bit_counts['0']
        if keep_most_common:
            target_bit = '1' if ones >= zeros else '0'
        else:
            target_bit = '1' if ones < zeros else '0'
        return [bit for bit in candidates if bit[position] == target_bit]

    def get_rating(keep_most_common):
        candidates = lines.copy()
        position = 0
        while len(candidates) > 1:
            candidates = filter_by_bit_criteria(candidates, position, keep_most_common)
            position += 1
        return int(candidates[0], 2)

    oxygen_rating = get_rating(True)
    co2_rating = get_rating(False)
    return oxygen_rating * co2_rating

# END OF SOLUTION
print(f'My answer is {part_1(input)}')
print(f'My answer is {part_2(input)}')
