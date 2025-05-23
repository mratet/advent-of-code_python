from aocd import get_data

input = get_data(day=16, year=2020)
import re
from math import prod


# WRITE YOUR SOLUTION HERE
def parse_input(data):
    fields_regex = r"([\w\s]+): (\d+)-(\d+) or (\d+)-(\d+)\n"
    fields = {}
    for match in re.finditer(fields_regex, data):
        field_name = match.group(1)
        ranges = [
            (int(match.group(2)), int(match.group(3))),
            (int(match.group(4)), int(match.group(5))),
        ]
        fields[field_name] = ranges

    your_ticket_regex = r"your ticket:\n([\d,]+)"
    your_ticket_match = re.search(your_ticket_regex, data)
    your_ticket = (
        list(map(int, your_ticket_match.group(1).split(",")))
        if your_ticket_match
        else []
    )

    nearby_tickets_regex = r"nearby tickets:\n((?:[\d,]+\n?)+)"
    nearby_tickets_match = re.search(nearby_tickets_regex, data)
    nearby_tickets = (
        [
            list(map(int, ticket.split(",")))
            for ticket in nearby_tickets_match.group(1).strip().split("\n")
        ]
        if nearby_tickets_match
        else []
    )

    return fields, nearby_tickets, your_ticket


def is_ticket_valid(value, fields):
    for [(a1, a2), (b1, b2)] in fields.values():
        if a1 <= value <= a2 or b1 <= value <= b2:
            return True
    return False


def part_1(lines):
    fields, nearby_tickets, your_ticket = parse_input(lines)
    return sum(
        [
            val
            for ticket in nearby_tickets
            for val in ticket
            if not is_ticket_valid(val, fields)
        ]
    )


def get_next_dict(candidates, assign_name, assign_col):
    new_candidates = {}
    for name, t in candidates.items():
        if name != assign_name:
            new_candidates[name] = [v for v in t if v != assign_col]
    return new_candidates


def part_2(lines):
    fields, nearby_ticket, your_ticket = parse_input(lines)
    valid_ticket = [
        ticket
        for ticket in nearby_ticket
        if all(is_ticket_valid(val, fields) for val in ticket)
    ]

    candidates = {}
    for field, [(a1, a2), (b1, b2)] in fields.items():
        tab = [
            [(a1 <= val <= a2 or b1 <= val <= b2) for val in ticket]
            for ticket in valid_ticket
        ]
        tab_transposed = list(map(list, zip(*tab)))
        candidates[field] = [i for i, t in enumerate(tab_transposed) if all(t)]

    assignment, next_candidates = {}, None
    while candidates:
        for name, tab in candidates.items():
            if len(tab) == 1:
                assignment[name] = tab[0]
                next_candidates = get_next_dict(candidates, name, tab[0])
                break
        candidates = next_candidates

    return prod(
        [
            your_ticket[field_pos]
            for field_name, field_pos in assignment.items()
            if field_name.startswith("departure")
        ]
    )


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
