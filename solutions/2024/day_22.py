from collections import defaultdict

from aocd import get_data, submit

input = get_data(day=22, year=2024).splitlines()


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    numb = map(int, [int(n) for n in lines])
    ans = 0
    for n in numb:
        for _ in range(2000):
            n = (64 * n ^ n) % 16777216
            n = (n // 32 ^ n) % 16777216
            n = (n * 2048 ^ n) % 16777216
        ans += n
    return ans


def part_2(lines):
    numb = list(map(int, [int(n) for n in lines]))
    count_seq = defaultdict(int)
    for n in numb:
        bananas, diff, seen = [], [], set()
        for j in range(2001):
            bananas.append(n % 10)
            n = (64 * n ^ n) % 16777216
            n = (n // 32 ^ n) % 16777216
            n = (n * 2048 ^ n) % 16777216
        diff = [b2 - b1 for b1, b2 in zip(bananas[:], bananas[1:])]
        for j in range(4, len(diff) + 1):
            seq = tuple(diff[j - 4 : j])
            if seq not in seen:
                count_seq[seq] += bananas[j]
                seen.add(tuple(seq))
    return max(count_seq.values())


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
