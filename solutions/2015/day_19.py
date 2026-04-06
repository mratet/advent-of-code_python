import re

from aocd import get_data

input = get_data(day=19, year=2015).splitlines()


def kmp_partial(pattern):
    ret = [0]
    for i in range(1, len(pattern)):
        j = ret[i - 1]
        while j > 0 and pattern[j] != pattern[i]:
            j = ret[j - 1]
        ret.append(j + 1 if pattern[j] == pattern[i] else j)
    return ret


def kmp_search(text, pattern):
    partial, ret, j = kmp_partial(pattern), [], 0
    for i in range(len(text)):
        while j > 0 and text[i] != pattern[j]:
            j = partial[j - 1]
        if text[i] == pattern[j]:
            j += 1
        if j == len(pattern):
            ret.append(i - (j - 1))
            j = partial[j - 1]
    return ret


def _parse(input):
    replacements = []
    for line in input[:-2]:
        src, dest = line.split(" => ")
        replacements.append((src, dest))
    return replacements, input[-1]


def part_1(input):
    replacements, molecule = _parse(input)
    synthesis = set()
    for src, dest in replacements:
        for i in kmp_search(molecule, src):
            synthesis.add(molecule[:i] + dest + molecule[i + len(src) :])
    return len(synthesis)


def part_2(input):
    # One letters always change into 2 letters
    # Rn, Ar always come in pair and can't be transform
    # Y can't be transform and is surround by two carac
    _, molecule = _parse(input)
    tokens = re.findall(r"[A-Z][a-z]*", molecule)
    return len(tokens) - 2 * tokens.count("Ar") - 2 * tokens.count("Y") - 1


print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
