from collections import defaultdict
from datetime import datetime


input_rows = open("input.txt").read().splitlines()


persons = defaultdict(list)
for row in input_rows:
    date, names = row.split(": ")
    for name in names.split(", "):
        persons[name].append(date)

date_formats = [
    ("%y-%d-%m", "01-11-09"),
    ("%y-%m-%d", "01-09-11"),
    ("%m-%d-%y", "09-11-01"),
    ("%d-%m-%y", "11-09-01"),
]

names = []
for name, dates in persons.items():
    for date_format, nine_eleven in date_formats:
        try:
            _ = [datetime.strptime(date, date_format) for date in dates]
            if nine_eleven in dates:
                names.append(name)
        except ValueError:
            continue
print(" ".join(sorted(names)))
