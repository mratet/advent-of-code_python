from aocd import get_data

aoc_input = get_data(day=22, year=2019).splitlines()


# WRITE YOUR SOLUTION HERE
def get_instructions(lines):
    instr = []
    for line in lines:
        if line[:3] == "cut":
            instr.append(("cut", int(line[4:])))
        elif line[:9] == "deal with":
            instr.append(("inc", int(line[-2:])))
        else:
            instr.append(("new", -1))
    return instr


def manual_shuffling(deck, instr):
    for inst, n in instr:
        match inst:
            case "new":
                deck = list(reversed(deck))
            case "cut":
                deck = deck[n:] + deck[:n]
            case "inc":
                N = len(deck)
                new_deck = [0] * N
                deck.reverse()  # to pop easily
                pos = 0
                while deck:
                    new_deck[pos % N] = deck.pop()
                    pos += n
                deck = new_deck
    return deck


def part_1(lines):
    instructions = get_instructions(lines)
    deck = manual_shuffling(list(range(10007)), instructions)
    return deck.index(2019)

def get_linear_params(instr):
    a, b = 1, 0
    for inst, n in instr:
        match inst:
            case "new":
                a, b = -a, -b - 1
            case "cut":
                b -= n
            case "inc":
                a, b = a * n, b * n
    return a, b


def get_position(x, a, b, deck_size, shuffle_count):
    Ma = pow(a, shuffle_count, deck_size)
    Mb = b * (Ma - 1) * pow(a - 1, -1, deck_size)
    return (Ma * x + Mb) % deck_size


def get_card(x, a, b, deck_size, shuffle_count):
    Ma = pow(a, shuffle_count, deck_size)
    Ma_inv = pow(Ma, -1, deck_size)
    Mb = b * (Ma - 1) * pow(a - 1, -1, deck_size)
    return (Ma_inv * (x - Mb)) % deck_size


def part_2(lines):
    DECK_SIZE = 119315717514047
    SHUFFLE_COUNT = 101741582076661

    instructions = get_instructions(lines)
    a, b = get_linear_params(instructions)
    return get_card(
        2020,
        a % DECK_SIZE,
        b % DECK_SIZE,
        DECK_SIZE,
        SHUFFLE_COUNT,
    )


# END OF SOLUTION
print(f"My answer is {part_1(aoc_input)}")
print(f"My answer is {part_2(aoc_input)}")
