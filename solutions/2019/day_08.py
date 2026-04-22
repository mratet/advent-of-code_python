from collections import Counter

from advent_of_code_ocr import convert_6
from aocd import get_data

aoc_input = get_data(day=8, year=2019)

W, H = 25, 6


def parse_layers(lines):
    size = W * H
    return [lines[i : i + size] for i in range(0, len(lines), size)]


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    layers = parse_layers(lines)
    min_layer = min(layers, key=lambda l: l.count("0"))
    counts = Counter(min_layer)
    return counts["1"] * counts["2"]


def part_2(lines):
    layers = parse_layers(lines)
    size = len(layers[0])
    final_image = [next(layer[i] for layer in layers if layer[i] != "2") for i in range(size)]
    ascii_art = "\n".join("".join(final_image[row : row + W]) for row in range(0, size, W))
    return convert_6(ascii_art, fill_pixel="1", empty_pixel="0")


# END OF SOLUTION
print(f"My answer is {part_1(aoc_input)}")
print(f"My answer is {part_2(aoc_input)}")
