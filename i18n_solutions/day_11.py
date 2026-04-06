from itertools import product

input_rows = open("input.txt").read().splitlines()


GREEK_MAJ = "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"
GREEK_MIN = "αβγδεζηθικλμνξοπρστυφχψω"


def rotate_sentence(phrase):
    def rotate_char(char, alphabet):
        return alphabet[(alphabet.index(char) + 1) % len(alphabet)]

    result = ""
    for char in phrase:
        if char in GREEK_MAJ:
            result += rotate_char(char, GREEK_MAJ)
        elif char in GREEK_MIN:
            result += rotate_char(char, GREEK_MIN)
        else:
            result += char
    return result


odysseus_variants = ["Οδυσσε"]
for _ in range(len(GREEK_MIN) - 1):
    odysseus_variants.append(rotate_sentence(odysseus_variants[-1]))
odysseus_variants.reverse()

line_count = 0
for row, (i, odysseus_variant) in product(input_rows, enumerate(odysseus_variants)):
    if any(word.startswith(odysseus_variant) for word in row.split()):
        line_count += i + 1
print(line_count)
