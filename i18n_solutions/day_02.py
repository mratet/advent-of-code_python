from collections import Counter
from datetime import datetime, timezone

input_rows = open("input.txt").read().splitlines()

datetimes = [
    datetime.fromisoformat(day).astimezone(tz=timezone.utc).isoformat()
    for day in input_rows
]
print(Counter(datetimes).most_common(1)[0][0])
