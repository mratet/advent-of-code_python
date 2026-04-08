import re

from aocd import get_data

input = get_data(day=7, year=2016).splitlines()


def _parse_addr(addr):
    parts = re.split(r"\[|\]", addr)
    return parts[0::2], parts[1::2]


def find_patterns(word, size):
    for i in range(len(word) - size + 1):
        s = word[i : i + size]
        if s[0] == s[size - 1] and s[0] != s[1] and (size == 3 or s[1] == s[2]):
            yield s


def support_tls(addr):
    supernets, hypernets = _parse_addr(addr)
    has_abba = any(p for s in supernets for p in find_patterns(s, 4))
    abba_in_hyper = any(p for h in hypernets for p in find_patterns(h, 4))
    return has_abba and not abba_in_hyper


def support_ssl(addr):
    supernets, hypernets = _parse_addr(addr)
    for s in supernets:
        for aba in find_patterns(s, 3):
            bab = aba[1] + aba[0] + aba[1]
            if any(bab in h for h in hypernets):
                return True
    return False


def part_1(input):
    return sum(support_tls(addr) for addr in input)


def part_2(input):
    return sum(support_ssl(addr) for addr in input)


print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
