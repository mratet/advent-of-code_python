lines = open("input.txt").read().splitlines()


# WRITE YOUR SOLUTION HERE
def count_match(line):
    win_cards, cards = line.split(":")[1].split("|")
    set_win_cards = set(win_cards.split())
    set_cards = set(cards.split())
    len_winning_numbers = len(set_cards & set_win_cards)
    return len_winning_numbers


def part_1(lines):
    ans = 0
    for line in lines:
        n = count_match(line)
        if n:
            ans += 2 ** (n - 1)
    return ans


def part_2(lines):
    multiplier = [1] * len(lines)
    for i, line in enumerate(lines):
        n = count_match(line)
        for j in range(n):
            multiplier[i + 1 + j] += multiplier[i]
    return sum(multiplier)
    # END OF SOLUTION


test_input = open("input-test.txt").read().splitlines()
test_lines = []
for i, line in enumerate(test_input[3:]):
    if line[0] == "-":
        break
    test_lines.append(line)
solution = test_input[i + 4]

print(f"My answer on test set for the first problem is {part_1(test_lines)}")
print(solution)
print(f"My answer is {part_1(lines)}")

print(f"My answer on test set for the second problem is {part_2(test_lines)}")
print(f"My answer is {part_2(lines)}")
