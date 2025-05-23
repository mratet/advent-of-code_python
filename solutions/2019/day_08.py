from aocd import get_data

aoc_input = get_data(day=8, year=2019)


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    W, H = 25, 6
    size = W * H
    layers = [lines[i : i + size] for i in range(0, len(lines), size)]
    min_layer = min(layers, key=lambda l: l.count("0"))
    return min_layer.count("1") * min_layer.count("2")


def part_2(lines):
    W, H = 25, 6
    size = W * H
    layers = [lines[i : i + size] for i in range(0, len(lines), size)]
    final_image = [
        next(layer[i] for layer in layers if layer[i] != "2") for i in range(size)
    ]
    for h in range(H):
        print(" ".join(final_image[h * W : (h + 1) * W]))
    # PHPEU -> difficile a lire !
    return "PHPEU"


# END OF SOLUTION
print(f"My answer is {part_1(aoc_input)}")
print(f"My answer is {part_2(aoc_input)}")
