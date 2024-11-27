from aocd import get_data
input = get_data(day=7, year=2020).splitlines()
from functools import lru_cache
import re

# WRITE YOUR SOLUTION HERE
def parse_bag_rules(lines):
    bag_rules = {}
    for line in lines:
        main_bag, contents = line.split(" bags contain ")
        if "no other bags" in contents:
            bag_rules[main_bag] = {}
        else:
            content_matches = re.findall(r"(\d+) ([a-z ]+) bag", contents)
            bag_rules[main_bag] = {bag_color: int(quantity) for quantity, bag_color in content_matches}
    return bag_rules

def part_1(lines):
    bag_rules = parse_bag_rules(lines)
    valid_bag = ['shiny gold']
    for _ in range(50):
        for bag, luggage in bag_rules.items():
            for bag_v in valid_bag:
                if bag_v in luggage and bag not in valid_bag:
                    valid_bag.append(bag)
    return len(valid_bag) - 1

def part_2(lines):
    bag_rules = parse_bag_rules(lines)
    @lru_cache(maxsize=None)
    def bag_weight(bag):
        if not bag_rules[bag]:
            return 0
        return sum([v * (bag_weight(b) + 1) for b, v in bag_rules[bag].items()])
    return bag_weight('shiny gold')

# END OF SOLUTION
print(f'My answer is {part_1(input)}')
print(f'My answer is {part_2(input)}')
