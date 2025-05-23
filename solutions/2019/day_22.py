from aocd import get_data, submit

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


def shuffle_deck(deck, instr):
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
    instr = get_instructions(lines)
    deck = shuffle_deck(list(range(10007)), instr)
    return deck.index(2019)


def compute_cycle(val, mapping):
    cycle = []
    while val not in cycle:
        cycle.append(val)
        val = mapping[val]
    return cycle


def decompose_deck_shuffling(mapping):
    deck_composition = set(mapping)
    cycles = []
    while deck_composition:
        p = deck_composition.pop()
        cycle = compute_cycle(p, mapping)
        cycles.append(cycle)
        deck_composition -= set(cycle)
    return cycles


def part_2(lines):
    instr = get_instructions(lines)
    prime_list = (10007, 10009, 10037, 10039, 10061, 10067, 10069, 10079)
    for P in prime_list:
        init_deck = list(range(P))
        mapping = [0] * P
        hist = [0] * P
        for i, val in enumerate(shuffle_deck(init_deck, instr)):
            mapping[val] = i

        cycles = decompose_deck_shuffling(mapping)
        for c in cycles:
            print(c)
        print()
    # k = 9437 # 2 The deck seems to create 2 unif cycle
    # for _ in range(1000000):
    #     k = mapping[k]
    #     hist[k] += 1
    # print(hist)
    return mapping[2019]


# END OF SOLUTION
# print(f'My answer is {part_1(aoc_input)}')
print(f"My answer is {part_2(aoc_input)}")
