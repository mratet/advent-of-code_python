
lines = open('input.txt').read().splitlines()

# WRITE YOUR SOLUTION HERE
# Prestation terrible aujourd'hui pour traiter le cas numéro 2 : A REPRENDRE AU PROPRE
def get_hand_type(hand):
    d = {}
    for c in hand:
        d[c] = 1 + d.get(c, 0)
    dict_hand = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
    keys = list(dict_hand.keys())
    if len(keys) == 1:
        return 7

    jokers_numbers = dict_hand.get(1, 0)

    main_figure, second_figure = keys[0], keys[1]
    if jokers_numbers > 0:
        if main_figure != 1:
            dict_hand[main_figure] += jokers_numbers
            dict_hand.pop(1, 'None')
        else:
            dict_hand[second_figure] += jokers_numbers
            dict_hand.pop(1, 'None')

    dict_hand = dict(sorted(dict_hand.items(),key=lambda item: item[1], reverse=True))
    keys = list(dict_hand.keys())
    main_figure = keys[0]
    if len(keys) > 1:
       second_figure = keys[1]
    if dict_hand[main_figure] == 5:
        return 7
    elif dict_hand[main_figure] == 4:
        return 6
    elif dict_hand[main_figure] == 3 and dict_hand[second_figure] == 2:
        return 5
    elif dict_hand[main_figure] == 3:
        return 4
    elif dict_hand[main_figure] == 2 and dict_hand[second_figure] == 2:
        return 3
    elif dict_hand[main_figure] == 2:
        return 2
    else:
        return 1


def part_1(lines):
    tab = []
    for line in lines:
        hand, rank = line.split()
        hand = [2 + '23456789TJQKA'.index(i) for i in hand]
        hand_type = get_hand_type(hand)
        tab.append((hand_type, hand, rank))
    tab.sort()
    rank = [int(x[2]) * (i + 1) for i, x in enumerate(tab)]
    return sum(rank)

def part_2(lines):
    tab = []
    for line in lines:
        hand, rank = line.split()
        hand = [1 + 'J23456789TXQKA'.index(i) for i in hand]
        hand_type = get_hand_type(hand)
        tab.append((hand_type, hand, rank))
    tab.sort()
    rank = [int(x[2]) * (i + 1) for i, x in enumerate(tab)]
    return sum(rank)
# END OF SOLUTION


test_input = open('input-test.txt').read().splitlines()
test_lines = []
for i, line in enumerate(test_input[3:]):
    if line[0] == '-':
        break
    test_lines.append(line)
solution = test_input[i + 4]

print(f'My answer on test set for the first problem is {part_1(test_lines)}')
print(solution)
print(f'My answer is {part_1(lines)}')

print(f'My answer on test set for the second problem is {part_2(test_lines)}')
print(f'My answer is {part_2(lines)}')

# https://topaz.github.io/paste/#XQAAAQCvAQAAAAAAAAAzHIoib6pXbueH4X9F244lVRDcOZab5q16fMXrmVEJ7EiuJnp+HR8bmweKL0bsshOVWHltyIIdHUY+gVL+xHllAL24MbI947OUlxsYVwxg1xBD/pKBZtfv/cKpi+wgrXdqsSqA/Gbidv/sx+wOJ3VyL4dE7GgLeZuk62GJ9mLI4C8tJ9p4Ur0HDygQrkYeKMxR6TFgiEh0QeKF2FRdKpXciFVQ3p5mSj89QRt758HGVQcERrzhJxQhwsayHSIQ7/eOLXmc/pCGU+Kaid03qI5Ae2MYbwi/8PJ4qe749ykLLFBVsZnvdyf02h9g/iRrI8TfTLbe0TBNr3TEL5P+pPy4x+1PEeShV4z9nmKPTmzbK0tlRmtk8s+u8x7OH7/4GA+lArR7L6Dy51F1FS3/ieXCbg==
# https://topaz.github.io/paste/#XQAAAQCHAgAAAAAAAAA0m0pnuFI8c82uPD0wiI6r5tRSAsbZgUzJOvgVEBkQ2k90k6LJItRUlOHkf0diy+sGU6CgxJAruK8MX7dpc+hmo2Qk8oecFpWt/StP10UJ3KMjLdvJQbsokGLTL3L2SZvwYchPlbADL5H93c9eI5TRle/OkDd6V8agOZlVKjQK9xtUOxDDzWeyhQiTfu5oNRsHtogsVuUxux+apOFej9l6edRvNn8nLKg9uRHRzWP0l0GmB/dOVhaGFJtxZeDZVCuP1BIuEX+nlyL26pOIaHHnQZylvrDnazj/3i8kNaFhGrHKVYWrxQRoHWoRFpcsJfbeLCjNckJGJ0efQL8M5KExy17CaDctvtJELTvYeNFMj78sblBv786AS8ulHaIOLBiYfXYcrXNR2yvkaXMt1mJxNfET23opQVV+UlT9JEcPWZQu6p5XRqwgpQY7+HmR77A6h4XF8eX25nYi1+MwXj2u1gBxbM3A6Xv6wlqMWWy6/ntIWv4QssJ0E6YbbXUjAOd+pVhAIkjR/n9l/9rTHKQ=