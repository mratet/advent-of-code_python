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


def remove_bom(bytes_word):
    BOMS = (b"\xef\xbb\xbf", b"\xfe\xff", b"\xff\xfe")
    for BOM in BOMS:
        if bytes_word.startswith(BOM):
            return bytes_word[len(BOM):]
    return bytes_word


def decode_word(word):
    bytes_word = remove_bom(bytes.fromhex(word))

    if bytes_word[0] == 0:
        return bytes_word.decode("utf-16be")
    elif bytes_word[1] == 0:
        return bytes_word.decode("utf-16le")
    else:
        try:
            return bytes_word.decode("utf-8")
        except UnicodeDecodeError:
            return bytes_word.decode("latin-1")


words, crosswords = input_blocks
decoded_words = [decode_word(word) for word in words.splitlines()]
print(solve_crossword_puzzle(crosswords, decoded_words))
