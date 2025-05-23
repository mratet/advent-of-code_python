from collections import defaultdict

from aocd import get_data

aoc_input = get_data(day=14, year=2019).splitlines()
from math import ceil

aoc_input = """9 ORE => 2 A
8 ORE => 3 B
7 ORE => 5 C
3 A, 4 B => 1 AB
5 B, 7 C => 1 BC
4 C, 1 A => 1 CA
2 AB, 3 BC, 4 CA => 1 FUEL""".splitlines()


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    reactions = defaultdict(list)
    chemicals = set()
    out_mul = {}
    for line in lines:
        in_chem, out_chem = line.split(" => ")
        w_out, out_comp = out_chem.split(" ")
        out_mul[out_comp] = int(w_out)
        for chem in in_chem.split(", "):
            w, comp = chem.split(" ")
            reactions[out_comp].append((comp, int(w)))
            chemicals.add(comp)

    out_mul["ORE"] = 1

    def find_decomposition(chem, quantity_wanted):
        if quantity_wanted == 0:
            return {}
        cnt = ceil(quantity_wanted / out_mul[chem])
        if chem == "ORE":
            return {"ORE": quantity_wanted}
        decomp = defaultdict(int)
        for comp, w in reactions[chem]:
            d = find_decomposition(comp, w * cnt)
            for c, c_w in d.items():
                decomp[c] += c_w
        return decomp

    print(find_decomposition("FUEL", 1))

    return


def part_2(lines):
    return


# END OF SOLUTION
print(f"My answer is {part_1(aoc_input)}")
# submit(part_1(aoc_input), part="a", day=14, year=2019)
print(f"My answer is {part_2(aoc_input)}")
# submit(part_2(aoc_input), part="b", day=14, year=2019)
