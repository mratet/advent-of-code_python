from collections import defaultdict
from datetime import datetime
import re
from aocd import get_data

input_lines = get_data(day=4, year=2018).splitlines()


def parse_input(lines):
    records = []
    for line in lines:
        date_str, event = line.split("] ")
        timestamp = datetime.strptime(date_str[1:], "%Y-%m-%d %H:%M")
        records.append((timestamp, event))
    return sorted(records)


def analyze_guard_sleep(records):
    guards = defaultdict(lambda: [0] * 60)
    current_guard = None
    asleep_minute = None

    for timestamp, event in records:
        minute = timestamp.minute
        if "Guard" in event:
            current_guard = int(re.search(r"#(\d+)", event).group(1))
        elif "falls asleep" in event:
            asleep_minute = minute
        elif "wakes up" in event:
            for m in range(asleep_minute, minute):
                guards[current_guard][m] += 1
    return guards


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    records = parse_input(lines)
    guards = analyze_guard_sleep(records)
    sleepiest_guard = max(guards, key=lambda gid: sum(guards[gid]))
    best_minute = guards[sleepiest_guard].index(max(guards[sleepiest_guard]))
    return sleepiest_guard * best_minute


def part_2(lines):
    records = parse_input(lines)
    guards = analyze_guard_sleep(records)
    most_frequent = max(
        (
            (gid, minute, count)
            for gid, minutes in guards.items()
            for minute, count in enumerate(minutes)
        ),
        key=lambda x: x[2],
    )
    guard_id, best_minute, _ = most_frequent
    return guard_id * best_minute


# END OF SOLUTION
print(f"My answer is {part_1(input_lines)}")
print(f"My answer is {part_2(input_lines)}")
