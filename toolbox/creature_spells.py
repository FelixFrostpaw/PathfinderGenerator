from toolbox import general
from tables import creature_spell_attack_bonus


def process_spell_attack_bonus(creature):
  level = general.process_level(creature)
  level_index = general.level_index_lookup(level)

  if "spell_attack_bonus" not in creature:
    return 0

  spell_attack_bonus_input = creature["spell_attack_bonus"]

  if spell_attack_bonus_input not in creature_spell_attack_bonus.table:
    raise Exception(
        f"Invalid Spell Attack Bonus Descriptor: {spell_attack_bonus_input}")

  spell_attack_bonus = creature_spell_attack_bonus.table[
      spell_attack_bonus_input][level_index]

  return spell_attack_bonus


def process_spell_dc(creature):
  level = general.process_level(creature)
  level_index = general.level_index_lookup(level)

  spell_dc_adjustment = 8

  if "spell_attack_bonus" not in creature:
    return 0

  spell_attack_bonus_input = creature["spell_attack_bonus"]

  if spell_attack_bonus_input not in creature_spell_attack_bonus.table:
    raise Exception(f"Invalid Spell DC Descriptor: {spell_attack_bonus_input}")

  spell_attack_bonus = creature_spell_attack_bonus.table[
      spell_attack_bonus_input][level_index]

  spell_dc = spell_attack_bonus + spell_dc_adjustment

  return spell_dc
