from datetime import datetime
from zoneinfo import ZoneInfo


input_blocks = open("input.txt").read().split("\n\n")


def parse_datetime(text):
    _, region, *date_parts = text.split()
    date_str = " ".join(date_parts)
    return datetime.strptime(date_str, "%b %d, %Y, %H:%M").replace(
        tzinfo=ZoneInfo(region)
    )


total_minutes = 0
for block in input_blocks:
    departure, arrival = block.split("\n", 1)
    dt_departure = parse_datetime(departure)
    dt_arrival = parse_datetime(arrival)
    total_minutes += int((dt_arrival - dt_departure).total_seconds()) // 60

print(total_minutes)
