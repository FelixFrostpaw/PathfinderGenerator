from tables import creature_ability_modifiers
from tables import creature_area_damage
from tables import creature_armor_class
from tables import creature_hit_points
from tables import creature_perceptions
from tables import creature_resistances_and_weaknesses
from tables import creature_saves
from tables import creature_skills
from tables import creature_spell_hit
from tables import creature_strike_attack_bonus
from tables import creature_strike_damage
from tables import dc_adjustments
from tables import hazard_armor_class
from tables import hazard_attack_bonus
from tables import hazard_damage
from tables import hazard_hardness
from tables import hazard_hit_points
from tables import hazard_saves
from tables import hazard_stealth_and_disable_dc
from tables import level_dcs
from tables import spell_dcs


def valid_level(num, is_level_dc=False):
  if is_level_dc:
    return -1 <= num <= 24
  else:
    return -1 <= num <= 25


def level_index(level):
  return level + 1


def valid_types(input_type):
  if input_type == "creature" or input_type == "hazard":
    return True
  else:
    return False


def process_level(creature):
  if "level" not in creature:
    raise Exception("Missing Creature Level")

  level_input = creature['level']

  if not valid_level(level_input):
    raise Exception("Invalid Creature Level")

  return level_input


def process_ability_score(creature, level_input, ability_score):
  if ability_score not in [
      "strength", "dexterity", "constitution", "intelligence", "wisdom",
      "charisma"
  ]:
    raise Exception("Invalid Ability Score")

  if ability_score not in creature.keys():
    raise Exception(f"Missing {ability_score}")

  ability_score_input = creature[ability_score]

  if ability_score_input not in creature_ability_modifiers.table.keys():
    raise Exception(f"Invalid {ability_score} Descriptor")

  ability_score_modifier = creature_ability_modifiers.table[
      ability_score_input][level_index(level_input)]

  return ability_score_modifier

def process_perception(creature, level_input):
  if "perception" not in creature.keys():
    raise Exception("Missing Perception")

  perception_input = creature["perception"]

  if perception_input not in creature_perceptions.table.keys():
    raise Exception("Invalid Perception Descriptor")

  perception_modifier = creature_perceptions.table[perception_input][
      level_index(level_input)]

  return perception_modifier

def process_skills(creature, level_input):
  if "skills" not in creature.keys():
    return []

  skill_modifiers = []

  for skill in creature["skills"].items():
    

  return skill_modifiers

def process_creature(creature):
  level_input = process_level(creature)

  strength_modifier = process_ability_score(creature, level_input, "strength")
  dexterity_modifier = process_ability_score(creature, level_input, "dexterity")
  constitution_modifier = process_ability_score(creature, level_input, "constitution")
  intelligence_modifier = process_ability_score(creature, level_input, "intelligence")
  wisdom_modifier = process_ability_score(creature, level_input, "wisdom")
  charisma_modifier = process_ability_score(creature, level_input, "charisma")

  perception_modifier = process_perception(creature, level_input)

  skill_modifiers = process_skills(creature, level_input)
  print(skill_modifiers)


