from aocd import get_data

input = get_data(day=3, year=2025).splitlines()

# WRITE YOUR SOLUTION HERE
def max_digits_sequence(s, N):
    result = []
    start = 0
    for remaining in range(N, 0, -1):
        end = len(s) - remaining + 1
        best_digit = max(s[start:end])
        start = s.index(best_digit, start, end) + 1

        result.append(best_digit)

    return int(''.join(result))

def part_1(lines):
    return sum(max_digits_sequence(line, 2) for line in lines)

def part_2(lines):
    return sum(max_digits_sequence(line, 12) for line in lines)

# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
