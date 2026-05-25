import re
from math import ceil, prod

from aocd import get_data

input = get_data(day=19, year=2022)

BUILD_OPTIONS = [
    ("geode_robot", (0, 0, 0, 1)),
    ("obsidian_robot", (0, 0, 1, 0)),
    ("clay_robot", (0, 1, 0, 0)),
    ("ore_robot", (1, 0, 0, 0)),
]


# WRITE YOUR SOLUTION HERE
def parse_blueprints(text):
    blueprints = []
    for line in text.splitlines():
        _, ore_cost, clay_cost, obs_ore_cost, obs_clay_cost, geo_ore_cost, geo_obs_cost = map(
            int, re.findall(r"\d+", line)
        )
        blueprints.append(
            {
                "ore_robot": (ore_cost, 0, 0),
                "clay_robot": (clay_cost, 0, 0),
                "obsidian_robot": (obs_ore_cost, obs_clay_cost, 0),
                "geode_robot": (geo_ore_cost, 0, geo_obs_cost),
            }
        )
    return blueprints


def simulate_blueprint(blueprint, max_minutes):
    max_ore = max(c[0] for c in blueprint.values())
    max_clay = blueprint["obsidian_robot"][1]
    max_obs = blueprint["geode_robot"][2]
    best = 0

    def dfs(minute, ore_r, clay_r, obs_r, geo_r, ore, clay, obs, geo):
        nonlocal best
        time_left = max_minutes - minute
        best = max(best, geo + geo_r * time_left)

        if geo + geo_r * time_left + (time_left * (time_left - 1)) // 2 <= best:
            return

        for robot_type, (dr_ore, dr_clay, dr_obs, dr_geo) in BUILD_OPTIONS:
            ore_cost, clay_cost, obs_cost = blueprint[robot_type]
            if robot_type == "ore_robot" and ore_r >= max_ore:
                continue
            if robot_type == "clay_robot" and clay_r >= max_clay:
                continue
            if robot_type == "obsidian_robot" and (obs_r >= max_obs or clay_r == 0):
                continue
            if robot_type == "geode_robot" and obs_r == 0:
                continue
            wait = max(
                ceil((ore_cost - ore) / ore_r) if ore_cost > ore else 0,
                ceil((clay_cost - clay) / clay_r) if clay_cost > clay and clay_r > 0 else 0,
                ceil((obs_cost - obs) / obs_r) if obs_cost > obs and obs_r > 0 else 0,
            )
            t = wait + 1
            if minute + t >= max_minutes:
                continue
            dfs(
                minute + t,
                ore_r + dr_ore,
                clay_r + dr_clay,
                obs_r + dr_obs,
                geo_r + dr_geo,
                ore + ore_r * t - ore_cost,
                clay + clay_r * t - clay_cost,
                obs + obs_r * t - obs_cost,
                geo + geo_r * t,
            )

    dfs(0, 1, 0, 0, 0, 0, 0, 0, 0)
    return best


def solve(lines, part="part_1"):
    blueprints = parse_blueprints(lines)
    if part == "part_1":
        return sum(i * simulate_blueprint(bp, 24) for i, bp in enumerate(blueprints, 1))
    return prod(simulate_blueprint(bp, 32) for bp in blueprints[:3])


def part_1(lines):
    return solve(lines)


def part_2(lines):
    return solve(lines, "part_2")


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
