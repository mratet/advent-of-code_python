from aocd import get_data

input = get_data(day=10, year=2021).splitlines()

MATCHING_CAR = {"(": ")", "[": "]", "{": "}", "<": ">"}
CORRUPTED_SCORE = {")": 3, "]": 57, "}": 1197, ">": 25137}
COMPLETED_SCORE = {")": 1, "]": 2, "}": 3, ">": 4}


def is_corrupted_chunk(line):
    curr_stack = []
    for c in line:
        if c in MATCHING_CAR:
            curr_stack.append(c)
        else:
            last_opening_car = curr_stack.pop()
            if MATCHING_CAR[last_opening_car] != c:
                return CORRUPTED_SCORE[c]
    return 0


def get_incomplete_stack(line):
    curr_stack = []
    for c in line:
        if c in MATCHING_CAR:
            curr_stack.append(c)
        else:
            curr_stack.pop()
    return curr_stack


def compute_stack_score(stack):
    score = 0
    while len(stack) > 0:
        score = score * 5 + COMPLETED_SCORE[MATCHING_CAR[stack.pop()]]
    return score


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    return sum(is_corrupted_chunk(line) for line in lines)


def part_2(lines):
    scores = [
        compute_stack_score(get_incomplete_stack(line))
        for line in lines
        if not is_corrupted_chunk(line)
    ]
    scores.sort()
    return scores[len(scores) // 2]


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
