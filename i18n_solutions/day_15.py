from collections import defaultdict
from datetime import datetime, timezone, timedelta, time
from zoneinfo import ZoneInfo


input_blocks = open("input.txt").read().split("\n\n")


def parse_line(line):
    parts = line.split("\t")
    return {
        "name": parts[0].split(" in ")[-1] if "in" in parts[0] else parts[0],
        "timezone": parts[1],
        "holidays": [
            datetime.strptime(hd, "%d %B %Y").date() for hd in parts[2].split(";")
        ],
    }


support_offices, customer_companies = input_blocks
support_offices = [parse_line(line) for line in support_offices.splitlines()]
customer_companies = [parse_line(line) for line in customer_companies.splitlines()]

base_dt = datetime(2022, 1, 1, tzinfo=timezone.utc)
complete_year = [base_dt + timedelta(hours=0.5 * i) for i in range(365 * 24 * 2)]

working_dts = set()
for office in support_offices:
    _, region, holidays = office.values()
    for dt in complete_year:
        if dt in working_dts:
            continue
        working_dt = dt.astimezone(ZoneInfo(region))
        if (
            0 <= working_dt.weekday() < 5
            and time(8, 30) <= working_dt.time() < time(17)
            and working_dt.date() not in holidays
        ):
            working_dts.add(working_dt)
overtime_dts = set(complete_year) - working_dts

school_overtime_count = defaultdict(int)
for company in customer_companies:
    school, region, holidays = company.values()
    for dt in overtime_dts:
        overtime_dt = dt.astimezone(ZoneInfo(region))
        if 0 <= overtime_dt.weekday() < 5 and overtime_dt.date() not in holidays:
            school_overtime_count[school] += 30
print(max(school_overtime_count.values()) - min(school_overtime_count.values()))
