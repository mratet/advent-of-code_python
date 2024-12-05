from aocd import get_data, submit
input = get_data(day=5, year=2024).splitlines()
from collections import defaultdict

# WRITE YOUR SOLUTION HERE
def parse_input(lines):
    dict_rule = defaultdict(list)
    pages = []
    c = False
    for line in lines:
        if not line:
            c = True
            continue
        if not c:
            a, b = line.split('|')
            dict_rule[int(a)].append(int(b))
        else:
            pages.append([int(n) for n in line.split(',')])
    return dict_rule, pages

def is_valid_pages(dict_rule, pages):
    for i, p in enumerate(pages):
        if any([next_page in pages[:i] for next_page in dict_rule[p]]):
            return False
    return True

def part_1(lines):
    dict_rule, pages = parse_input(lines)
    return sum([page[len(page) // 2] for page in pages if is_valid_pages(dict_rule, page)])

def correct_1_error(page, dict_rules):
    for idx, p in enumerate(page):
        if any([next_page in page[:idx] for next_page in dict_rules[p]]):
            break
    idx -= 1

    while idx < len(page) and not is_valid_pages(dict_rules, page):
        wrong_page = page.pop(idx)
        page.insert(idx + 1, wrong_page)
        idx += 1
    return page

def part_2(lines):
    dict_rule, pages = parse_input(lines)

    cnt = 0
    for p in pages:
        if not is_valid_pages(dict_rule, p):
            while not is_valid_pages(dict_rule, p):
                p = correct_1_error(p, dict_rule)
            cnt += p[len(p) // 2]
    return cnt
# END OF SOLUTION
print(f'My answer is {part_1(input)}')
print(f'My answer is {part_2(input)}')

