from functools import lru_cache

from aocd import get_data
from math import prod
import re

MAX_ROBOTS = 10
MAX_RESOURCES = 40

input = get_data(day=19, year=2022)


def parse_blueprints(text):
    blueprints = []

    blueprint_pattern = re.compile(
        r"Blueprint (\d+): "
        r"Each ore robot costs (\d+) ore\. "
        r"Each clay robot costs (\d+) ore\. "
        r"Each obsidian robot costs (\d+) ore and (\d+) clay\. "
        r"Each geode robot costs (\d+) ore and (\d+) obsidian\."
    )

    for line in text.splitlines():
        match = blueprint_pattern.match(line)
        (
            blueprint_id,
            ore_cost,
            clay_cost,
            obs_ore_cost,
            obs_clay_cost,
            geo_ore_cost,
            geo_obs_cost,
        ) = map(int, match.groups())

        blueprint = {
            "ore_robot": (ore_cost, 0, 0),
            "clay_robot": (clay_cost, 0, 0),
            "obsidian_robot": (obs_ore_cost, obs_clay_cost, 0),
            "geode_robot": (geo_ore_cost, 0, geo_obs_cost),
        }

        blueprints.append(blueprint)
    return blueprints


def simulate_blueprint(blueprint, max_minutes):
    max_geodes = 0

    @lru_cache(maxsize=None)
    def simulate(minute, ore_r, clay_r, obs_r, geo_r, ore, clay, obs, geo):
        nonlocal max_geodes

        if minute >= max_minutes:
            max_geodes = max(max_geodes, geo)
            return

        time_left = max_minutes - minute
        optimistic = geo + geo_r * time_left + (time_left * (time_left - 1)) // 2
        if optimistic <= max_geodes:
            return

        if any(resource > MAX_RESOURCES for resource in [ore, clay, obs]):
            return

        if any(robot > MAX_ROBOTS for robot in [ore_r, clay_r, obs_r]):
            return

        build_options = [
            ("geode_robot", (0, 0, 0, 1)),
            ("obsidian_robot", (0, 0, 1, 0)),
            ("clay_robot", (0, 1, 0, 0)),
            ("ore_robot", (1, 0, 0, 0)),
        ]

        for robot_type, (dr_ore, dr_clay, dr_obs, dr_geo) in build_options:
            ore_cost, clay_cost, obs_cost = blueprint[robot_type]
            if ore >= ore_cost and clay >= clay_cost and obs >= obs_cost:
                simulate(
                    minute + 1,
                    ore_r + dr_ore,
                    clay_r + dr_clay,
                    obs_r + dr_obs,
                    geo_r + dr_geo,
                    ore + ore_r - ore_cost,
                    clay + clay_r - clay_cost,
                    obs + obs_r - obs_cost,
                    geo + geo_r,
                )

        simulate(
            minute + 1,
            ore_r,
            clay_r,
            obs_r,
            geo_r,
            ore + ore_r,
            clay + clay_r,
            obs + obs_r,
            geo + geo_r,
        )

    simulate(0, 1, 0, 0, 0, 0, 0, 0, 0)
    return max_geodes


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    blueprints = parse_blueprints(lines)
    return sum(
        blueprint_id * simulate_blueprint(blueprint, max_minutes=24)
        for blueprint_id, blueprint in enumerate(blueprints, start=1)
    )


def part_2(lines):
    blueprints = parse_blueprints(lines)
    return prod(
        simulate_blueprint(blueprint, max_minutes=32) for blueprint in blueprints[:3]
    )


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
