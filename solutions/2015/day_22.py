from aocd import get_data

input = get_data(day=22, year=2015).splitlines()

boss_hp_init, boss_damage = (int(line.split(": ")[1]) for line in input)
least_mana_used: int = 10**9


def play(hp, mana, boss_hp, shield_t, poison_t, recharge_t, spent_mana, player_turn=True, hard=False):
    global least_mana_used

    if player_turn and hard:
        hp -= 1
        if hp <= 0:
            return

    # Apply effects
    armor = 7 if shield_t > 0 else 0
    if poison_t > 0:
        boss_hp -= 3
    if recharge_t > 0:
        mana += 101
    shield_t = max(0, shield_t - 1)
    poison_t = max(0, poison_t - 1)
    recharge_t = max(0, recharge_t - 1)

    if boss_hp <= 0:
        least_mana_used = min(least_mana_used, spent_mana)
        return

    if spent_mana >= least_mana_used:
        return

    if player_turn:
        # Missile
        if mana >= 53:
            play(hp, mana - 53, boss_hp - 4, shield_t, poison_t, recharge_t, spent_mana + 53, False, hard)
        # Drain
        if mana >= 73:
            play(hp + 2, mana - 73, boss_hp - 2, shield_t, poison_t, recharge_t, spent_mana + 73, False, hard)
        # Shield
        if mana >= 113 and shield_t == 0:
            play(hp, mana - 113, boss_hp, 6, poison_t, recharge_t, spent_mana + 113, False, hard)
        # Poison
        if mana >= 173 and poison_t == 0:
            play(hp, mana - 173, boss_hp, shield_t, 6, recharge_t, spent_mana + 173, False, hard)
        # Recharge
        if mana >= 229 and recharge_t == 0:
            play(hp, mana - 229, boss_hp, shield_t, poison_t, 5, spent_mana + 229, False, hard)
    else:
        hp -= max(1, boss_damage - armor)
        if hp > 0:
            play(hp, mana, boss_hp, shield_t, poison_t, recharge_t, spent_mana, True, hard)


def solve(hard=False):
    global least_mana_used
    least_mana_used = 10**9
    play(50, 500, boss_hp_init, 0, 0, 0, 0, True, hard)
    return least_mana_used


def part_1():
    return solve(hard=False)


def part_2():
    return solve(hard=True)


print(f"My answer is {part_1()}")
print(f"My answer is {part_2()}")
