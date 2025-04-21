from itertools import groupby


input_rows = open("input.txt").read().splitlines()


def compute_levels(calculations):
    LRI_MARKER, RLI_MARKER, PDI_MARKER = "\u2066", "\u2067", "\u2069"
    embedding_level = 0
    levels = []
    for char in calculations:
        left_to_right = embedding_level % 2 == 0

        if char.isdigit():
            levels.append(embedding_level + embedding_level % 2)
            continue

        if char == RLI_MARKER and left_to_right:
            embedding_level += 1
        elif char == LRI_MARKER and not left_to_right:
            embedding_level += 1
        elif char == PDI_MARKER:
            embedding_level -= 1
        levels.append(embedding_level)
    return levels


def remove_lonely_max(nums):
    max_val = max(nums)
    result = nums.copy()

    for i in range(len(nums)):
        if nums[i] == max_val:
            has_max_neighbor = (i > 0 and nums[i - 1] == max_val) or (
                i < len(nums) - 1 and nums[i + 1] == max_val
            )
            if not has_max_neighbor:
                result[i] -= 1
    return result


def find_longest_segments(levels):
    result = {level: (0, 0) for level in set(levels)}
    position = 0
    for level, group in groupby(levels):
        length_group = len(list(group))
        if length_group > result[level][1]:
            result[level] = (position, length_group)
        position += length_group
    return result


def compute_mirror(calculation):
    levels = compute_levels(calculation)
    calculation = list(calculation)
    while max(levels) > 0:
        levels = remove_lonely_max(levels)
        segments = find_longest_segments(levels)
        idx, n = segments[
            next(key for key in sorted(segments, reverse=True) if segments[key][1] > 1)
        ]
        calculation[idx : idx + n] = reversed(calculation[idx : idx + n])
        for j in range(idx, idx + n):
            levels[j] -= 1
            if calculation[j] == ")":
                calculation[j] = "("
            elif calculation[j] == "(":
                calculation[j] = ")"
    return "".join(calculation)


def remove_BiDi_characters(p):
    return "".join((x for x in p if (x.isdigit() or x in "+-*/()")))

sum_differences = 0
for calculation in input_rows:
    rex_val = round(eval(remove_BiDi_characters(calculation)))
    lynx_val = round(eval(remove_BiDi_characters(compute_mirror(calculation))))
    sum_differences += abs(rex_val - lynx_val)
print(sum_differences)
