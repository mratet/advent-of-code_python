import itertools, re, collections
from aocd import get_data

input = get_data(day=19, year=2015).splitlines()


class KMP:
    def partial(self, pattern):
        """Calculate partial match table: String -> [Int]"""
        ret = [0]

        for i in range(1, len(pattern)):
            j = ret[i - 1]
            while j > 0 and pattern[j] != pattern[i]:
                j = ret[j - 1]
            ret.append(j + 1 if pattern[j] == pattern[i] else j)
        return ret

    def search(self, T, P):
        """
        KMP search main algorithm: String -> String -> [Int]
        Return all the matching position of pattern string P in T
        """
        partial, ret, j = self.partial(P), [], 0

        for i in range(len(T)):
            while j > 0 and T[i] != P[j]:
                j = partial[j - 1]
            if T[i] == P[j]:
                j += 1
            if j == len(P):
                ret.append(i - (j - 1))
                j = partial[j - 1]

        return ret


def _parse(input):
    replacements = collections.defaultdict(list)
    molecude = input[-1]
    for line in input[:-2]:
        src, dest = line.split(" => ")
        replacements[src].append(dest)
    return replacements, molecude


def part_1(input):
    replacements, molecule = _parse(input)
    synthesis = set()
    kmp = KMP()

    for src in replacements.keys():
        indexes = kmp.search(molecule, src)
        for dest, i in itertools.product(replacements[src], indexes):
            new_molecule = molecule[:i] + dest + molecule[i + len(src) :]
            synthesis.add(new_molecule)

    return len(synthesis)


def part_2(input):
    # One letters always change into 2 letters
    # Rn, Ar always come in pair and can't be transform
    # Y can't be transform and is surround by two carac
    replacements, molecule = _parse(input)
    tokens = re.findall(r"[A-Z][a-z]*", molecule)
    return len(tokens) - 2 * tokens.count("Ar") - 2 * tokens.count("Y") - 1


print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
