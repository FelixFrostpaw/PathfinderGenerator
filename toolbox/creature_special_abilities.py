import math

from toolbox import general

from toolbox import creature_strikes

from tables import creature_spell_attack_bonus
from tables import creature_strike_damage
from tables import creature_area_damage


def process_special_abilities(creature):
  level = general.process_level(creature)
  level_index = general.level_index_lookup(level)

  spell_dc_adjustment = 8

  if "special_abilities" not in creature:
    return {}

  special_abilities = {}

  for special_ability, special_ability_data in creature[
      "special_abilities"].items():

    special_ability_entry = {}

    if "bonus" in special_ability_data:
      if special_ability_data[
          "bonus"] not in creature_spell_attack_bonus.table:
        raise Exception(
            f"Invalid Special Ability Bonus Descriptor: {special_ability_data['bonus']}"
        )

      special_ability_bonus = creature_spell_attack_bonus.table[
          special_ability_data['bonus']][level_index]
      special_ability_entry["bonus"] = special_ability_bonus

    if "dc" in special_ability_data:
      if special_ability_data["dc"] not in creature_spell_attack_bonus.table:
        raise Exception(
            f"Invalid Special Ability DC Descriptor: {special_ability_data['dc']}"
        )

      special_ability_dc = creature_spell_attack_bonus.table[
          special_ability_data["dc"]][level_index] + spell_dc_adjustment
      special_ability_entry["dc"] = special_ability_dc

    if "single_target_damage" in special_ability_data:
      if special_ability_data[
          "single_target_damage"] not in creature_strike_damage.table:
        raise Exception(
            f"Invalid Special Ability Single Target Damage Descriptor: {special_ability['single_target_damage']}"
        )

      if "damage_algorithm" not in special_ability_data:
        raise Exception("Missing Special Ability Damage Algorithm")

      single_target_damage = creature_strike_damage.table[
          special_ability_data["single_target_damage"]][level_index]

      single_target_damage_algorithm = creature_strikes.process_strike_damage_algorithm(
          single_target_damage, special_ability_data["damage_algorithm"],
          level)

      special_ability_entry[
          "single_target_damage"] = single_target_damage_algorithm

    if "area_damage" in special_ability_data:
      if special_ability_data["area_damage"] not in creature_area_damage.table:
        raise Exception(
            f"Invalid Special Ability Damage Descriptor: {special_ability_data['area_damage']}"
        )

      if "damage_algorithm" not in special_ability_data:
        raise Exception("Missing Special Ability Damage Algorithm")

      area_damage = creature_area_damage.table[
          special_ability_data["area_damage"]][level_index]

      area_damage_algorithm = process_area_damage_algorithm(
          area_damage, special_ability_data["damage_algorithm"])

      special_ability_entry["area_damage"] = area_damage_algorithm

    if "description" in special_ability_data:
      special_ability_entry["description"] = special_ability_data[
          "description"]

    special_abilities[special_ability] = special_ability_entry

  return special_abilities


def process_area_damage_algorithm(area_damage, area_damage_algorithm):
  if area_damage_algorithm == "number":
    return area_damage

  dice_conversion = 0

  if area_damage_algorithm == "d4":
    dice_conversion = 2.5
  elif area_damage_algorithm == "d6":
    dice_conversion = 3.5
  elif area_damage_algorithm == "d8":
    dice_conversion = 4.5
  elif area_damage_algorithm == "d10":
    dice_conversion = 5.5
  elif area_damage_algorithm == "d12":
    dice_conversion = 6.5
  else:
    raise Exception(f"Invalid Damage Algorithm: {area_damage_algorithm}")

  dice_average = int(math.floor(area_damage / dice_conversion))

  if dice_average < 1:
    return f"1{area_damage_algorithm}"
  else:
    return f"{dice_average}{area_damage_algorithm}"
