from datetime import datetime, timedelta
from zoneinfo import ZoneInfo


input_rows = open("input.txt").read().splitlines()


tz1 = ZoneInfo("America/Halifax")
tz2 = ZoneInfo("America/Santiago")
result = 0
for i, row in enumerate(input_rows, start=1):
    datetime_str, correct_min, wrong_min = row.split()
    dt = datetime.fromisoformat(datetime_str)
    tz = tz1 if tz1.utcoffset(dt) == dt.utcoffset() else tz2
    td = timedelta(minutes=int(correct_min) - int(wrong_min))
    correct_dt = (dt + td).astimezone(tz)
    result += correct_dt.hour * i
print(result)
