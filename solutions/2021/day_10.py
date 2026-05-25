from aocd import get_data

input = get_data(day=10, year=2021).splitlines()

MATCHING_CAR = {"(": ")", "[": "]", "{": "}", "<": ">"}
CORRUPTED_SCORE = {")": 3, "]": 57, "}": 1197, ">": 25137}
COMPLETED_SCORE = {")": 1, "]": 2, "}": 3, ">": 4}


# WRITE YOUR SOLUTION HERE
def parse_line(line):
    stack = []
    for c in line:
        if c in MATCHING_CAR:
            stack.append(c)
        elif MATCHING_CAR[stack.pop()] != c:
            return CORRUPTED_SCORE[c], None
    return 0, stack


def compute_stack_score(stack):
    score = 0
    while stack:
        score = score * 5 + COMPLETED_SCORE[MATCHING_CAR[stack.pop()]]
    return score


def part_1(lines):
    return sum(score for score, _ in map(parse_line, lines))


def part_2(lines):
    scores = sorted(compute_stack_score(stack) for score, stack in map(parse_line, lines) if not score)
    return scores[len(scores) // 2]


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
