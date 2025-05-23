import itertools
import math
from aocd import get_data

input = get_data(day=21, year=2015).splitlines()


def fight_result(my_stat, boss_stat):
    boss_health, my_health = boss_stat["hp"], my_stat["hp"]
    my_damage = max(1, my_stat["damage"] - boss_stat["armor"])
    boss_damage = max(1, boss_stat["damage"] - my_stat["armor"])
    a = math.ceil(my_health / boss_damage)
    b = math.ceil(boss_health / my_damage)
    return a >= b


def get_game_data(data):
    # Taken from nitekat1124 because shop wasn't include into input data
    player = {
        "hp": 100,
        "damage": 0,
        "armor": 0,
    }
    boss = {
        "hp": int(data[0].split(": ")[1]),
        "damage": int(data[1].split(": ")[1]),
        "armor": int(data[2].split(": ")[1]),
    }
    weapons = {
        "dagger": {"cost": 8, "damage": 4, "armor": 0},
        "shortsword": {"cost": 10, "damage": 5, "armor": 0},
        "warhammer": {"cost": 25, "damage": 6, "armor": 0},
        "longsword": {"cost": 40, "damage": 7, "armor": 0},
        "greataxe": {"cost": 74, "damage": 8, "armor": 0},
    }
    armors = {
        "none": {"cost": 0, "damage": 0, "armor": 0},
        "leather": {"cost": 13, "damage": 0, "armor": 1},
        "chainmail": {"cost": 31, "damage": 0, "armor": 2},
        "splintmail": {"cost": 53, "damage": 0, "armor": 3},
        "bandedmail": {"cost": 75, "damage": 0, "armor": 4},
        "platemail": {"cost": 102, "damage": 0, "armor": 5},
    }
    rings = {
        "none1": {"cost": 0, "damage": 0, "armor": 0},
        "none2": {"cost": 0, "damage": 0, "armor": 0},
        "damage1": {"cost": 25, "damage": 1, "armor": 0},
        "damage2": {"cost": 50, "damage": 2, "armor": 0},
        "damage3": {"cost": 100, "damage": 3, "armor": 0},
        "defense1": {"cost": 20, "damage": 0, "armor": 1},
        "defense2": {"cost": 40, "damage": 0, "armor": 2},
        "defense3": {"cost": 80, "damage": 0, "armor": 3},
    }

    rings_combinations = list(itertools.combinations(rings.values(), 2))
    equipments = list(
        itertools.product(weapons.values(), armors.values(), rings_combinations)
    )

    return player, boss, equipments


def part_1(input):
    player, boss, equipments = get_game_data(input)

    costs = []
    for equipment in equipments:
        Weapon, Armor, (r1, r2) = equipment
        total_cost = Weapon["cost"] + Armor["cost"] + r1["cost"] + r2["cost"]
        player["damage"] = (
            Weapon["damage"] + Armor["damage"] + r1["damage"] + r2["damage"]
        )
        player["armor"] = Weapon["armor"] + Armor["armor"] + r1["armor"] + r2["armor"]

        if fight_result(player, boss):
            costs.append(total_cost)

    return min(costs)


def part_2(input):
    player, boss, equipments = get_game_data(input)

    costs = []
    for equipment in equipments:
        Weapon, Armor, (r1, r2) = equipment
        total_cost = Weapon["cost"] + Armor["cost"] + r1["cost"] + r2["cost"]
        player["damage"] = (
            Weapon["damage"] + Armor["damage"] + r1["damage"] + r2["damage"]
        )
        player["armor"] = Weapon["armor"] + Armor["armor"] + r1["armor"] + r2["armor"]

        if not fight_result(player, boss):
            costs.append(total_cost)

    return max(costs)


print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
