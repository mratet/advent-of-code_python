import itertools, re, collections
from aocd import get_data

input = get_data(day=7, year=2016).splitlines()


def get_abbas(word):
    abbas = []
    for i in range(0, len(word) - 3):
        slc = word[i : i + 4]
        if slc[0] == slc[3] and slc[1] == slc[2] and slc[0] != slc[1]:
            abbas.append(slc)
    return abbas


def support_tls(addr):
    pattern = r".*\[([a-z]+)\].*"
    while True:
        m = re.match(pattern, addr)
        if not m:
            break
        inner = m.groups()[0]
        if get_abbas(inner):
            return False
        addr = addr.replace(inner, "")

    return 1 if get_abbas(addr) else 0


def get_abas(word):
    abas = []
    for i in range(0, len(word) - 2):
        slc = word[i : i + 3]
        if slc[0] == slc[2] and slc[0] != slc[1]:
            abas.append(slc)
    return abas


def support_ssl(addr):
    pattern = r".*\[([a-z]+)\].*"
    hypernets = []
    while True:
        m = re.match(pattern, addr)
        if not m:
            break
        inner = m.groups()[0]
        hypernets.append(inner)
        addr = addr.replace(inner, "")

    abas = get_abas(addr)
    for aba in abas:
        a, b = aba[0], aba[1]
        bab = "".join([b, a, b])
        for h in hypernets:
            if bab in h:
                return True
    return False


def part_1(input):
    return sum([support_tls(addr) for addr in input])


def part_2(input):
    return sum([support_ssl(addr) for addr in input])


print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
