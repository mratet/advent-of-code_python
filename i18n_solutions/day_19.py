import shutil
import urllib.request
from pathlib import Path
import os


from itertools import chain
from collections import defaultdict
from datetime import datetime, timezone
from zoneinfo import ZoneInfo, reset_tzpath


input_rows = open("input.txt").read().splitlines()


def clean_files():
    for dir_path in chain(Path("").glob("tzdb-*"), Path("").glob("20*")):
        shutil.rmtree(dir_path)


def download_extract_and_compile_tzdb(tz_version):
    tz_files = [
        "africa",
        "antarctica",
        "asia",
        "australasia",
        "etcetera",
        "europe",
        "northamerica",
        "southamerica",
        "backward",
    ]
    tz_file_name = f"tzdb-{tz_version}.tar.lz"
    tz_url = f"https://data.iana.org/time-zones/releases/{tz_file_name}"
    urllib.request.urlretrieve(tz_url, tz_file_name)
    os.system(f"lzip -dc {tz_file_name} | tar xvf - ")
    for tz_file in tz_files:
        os.system(f"zic -d {tz_version} tzdb-{tz_version}/{tz_file}")
    os.remove(tz_file_name)


station_detections = defaultdict(set)
for tz_version in ["2018c", "2018g", "2021b", "2023d"]:
    download_extract_and_compile_tzdb(tz_version)
    ZoneInfo.clear_cache()
    reset_tzpath(to=[(Path(tz_version).resolve())])
    for row in input_rows:
        date_str, region = row.split("; ")
        dt = (
            datetime.fromisoformat(date_str)
            .replace(tzinfo=ZoneInfo(region))
            .astimezone(timezone.utc)
        )
        station_detections[region].add(dt)
clean_files()

(overlap_date,) = set.intersection(*station_detections.values())
print(overlap_date.strftime("%Y-%m-%dT%H:%M:%S+00:00"))
