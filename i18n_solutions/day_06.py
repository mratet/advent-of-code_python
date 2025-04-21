input_blocks = open("input.txt").read().split("\n\n")


def solve_crossword_puzzle(crosswords, decoded_words):
    count = 0
    for crossword in crosswords.splitlines():
        crossword = crossword.lstrip()
        n = len(crossword)
        idx, letter = next((i, c) for i, c in enumerate(crossword) if c != ".")
        count += next(
            i
            for i, w in enumerate(decoded_words, start=1)
            if n == len(w) and w[idx] == letter
        )
    return count


def decode_word(word, index):
    def decode_str(s):
        return s.encode("latin-1").decode("utf-8")

    if index % 3 == 0 and index % 5 == 0:
        return decode_str(decode_str(word))
    elif index % 3 == 0 or index % 5 == 0:
        return decode_str(word)
    return word


words, crosswords = input_blocks
decoded_words = [
    decode_word(word, i) for i, word in enumerate(words.splitlines(), start=1)
]
print(solve_crossword_puzzle(crosswords, decoded_words))
