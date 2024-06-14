#Spell DC is always 8 points higher than strike

moderate_spell_attack_bonus = [
    5, 5, 6, 7, 9, 10, 11, 13, 14, 15, 17, 18, 19, 21, 22, 23, 25, 26, 27, 29,
    30, 31, 33, 34, 35, 37
]
high_spell_attack_bonus = [
    8, 8, 9, 10, 12, 13, 14, 16, 17, 18, 20, 21, 22, 24, 25, 26, 28, 29, 30,
    32, 33, 34, 36, 37, 38, 40
]
extreme_spell_attack_bonus = [
    11, 11, 12, 14, 15, 17, 18, 19, 21, 22, 24, 25, 26, 28, 29, 31, 32, 33, 35,
    36, 38, 39, 40, 42, 43, 44
]

table = {
    "moderate": moderate_spell_attack_bonus,
    "high": high_spell_attack_bonus,
    "extreme": extreme_spell_attack_bonus
}
