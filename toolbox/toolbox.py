import random

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

  level = creature['level']

  if not valid_level(level):
    raise Exception("Invalid Creature Level")

  return level

def process_ability_score(creature, level, ability_score):
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
      ability_score_input][level_index(level)]

  return ability_score_modifier

def process_perception(creature, level):
  if "perception" not in creature.keys():
    raise Exception("Missing Perception")

  perception_input = creature["perception"]

  if perception_input not in creature_perceptions.table.keys():
    raise Exception("Invalid Perception Descriptor")

  perception_modifier = creature_perceptions.table[perception_input][
      level_index(level)]

  return perception_modifier

def process_skills(creature, level):
  if "skills" not in creature.keys():
    return {}

  skill_modifiers = {}

  for skill, skill_descriptor in creature["skills"].items():
    if skill_descriptor not in creature_skills.table.keys():
      raise Exception(f"Invalid {skill} Descriptor")

    skill_modifier = creature_skills.table[skill_descriptor][level_index(
        level)]

    skill_modifiers[skill] = skill_modifier

  return skill_modifiers

def process_armor_class(creature, level):
  if "armor_class" not in creature.keys():
    raise Exception("Missing Armor Class")

  armor_class_input = creature["armor_class"]

  if armor_class_input not in creature_armor_class.table.keys():
    raise Exception("Invalid Armor Class Descriptor")

  armor_class = creature_armor_class.table[armor_class_input][
      level_index(level)]

  return armor_class

def process_saving_throw(creature, level, saving_throw):
  if saving_throw not in ["fortitude", "reflex", "will"]:
    raise Exception("Invalid Saving Throw")

  if saving_throw not in creature.keys():
    raise Exception(f"Missing {saving_throw} Saving Throw")

  saving_throw_input = creature[saving_throw]

  saving_throw_modifier = creature_saves.table[saving_throw_input][level_index(level)]

  return saving_throw_modifier

def process_hit_points(creature, level):
  if "hp" not in creature.keys():
    raise Exception("Missing Hit Points")

  if "hp_algorithm" not in creature.keys():
    raise Exception("Missing Hit Points Algorithm")

  hp_input = creature["hp"]
  hp_algorithm_input = creature["hp_algorithm"]

  if hp_input not in creature_hit_points.table.keys():
    raise Exception(f"Invalid {hp_input} Descriptor")

  if hp_algorithm_input not in ["floor", "ceiling", "average", "range", "random"]:
    raise Exception(f"Invalid Algorithm: {hp_algorithm_input}")

  hp_floor = creature_hit_points.table[hp_input]["floor"][level_index(level)]
  hp_ceiling = creature_hit_points.table[hp_input]["ceiling"][level_index(level)]

  hp = 0

  if hp_algorithm_input == "floor":
    hp = hp_floor
  elif hp_algorithm_input == "ceiling":
    hp = hp_ceiling
  elif hp_algorithm_input == "average":
    hp = int((hp_floor + hp_ceiling) / 2)
  elif hp_algorithm_input == "range":
    hp = f"{hp_ceiling} - {hp_floor}"
  elif hp_algorithm_input == "random":
    hp = random.randint(hp_floor, hp_ceiling)
  else:
    raise Exception(f"Invalid Algorithm! {hp_algorithm_input}")

  return hp

def process_resistances_or_weaknesses(creature, level, resistance_or_weakness):
  if resistance_or_weakness not in ["resistances", "weaknesses"]:
    raise Exception("Invalid - Not a Resistance or Weakness")

  if resistance_or_weakness not in creature.keys():
    return {}

  resistance_or_weakness_input = creature[resistance_or_weakness]

  resistances_or_weaknesses = {}

  for resistance_or_weakness_descriptor, resistance_or_weakness_value in resistance_or_weakness_input.items():
    if resistance_or_weakness_value not in ["minimum", "maximum", "average"]:
      raise Exception("Invalid Resistance or Weakness Descriptor")

    resistance_or_weakness_minimum = creature_resistances_and_weaknesses.table["minimum"][level_index(level)]
    resistance_or_weakness_maximum = creature_resistances_and_weaknesses.table["maximum"][level_index(level)]

    resistance_or_weakness = 0
    
    if resistance_or_weakness_value == "minimum":
      resistance_or_weakness = resistance_or_weakness_minimum
    elif resistance_or_weakness_value == "maximum":
      resistance_or_weakness = resistance_or_weakness_maximum
    elif resistance_or_weakness_value == "average":
      resistance_or_weakness = int((resistance_or_weakness_minimum + resistance_or_weakness_maximum) / 2)
    else:
      raise Exception(f"Invalid Resistance or Weakness Value! {resistance_or_weakness_value}")

    resistances_or_weaknesses[resistance_or_weakness_descriptor] = resistance_or_weakness

  return resistances_or_weaknesses

def process_creature(creature):
  level = process_level(creature)

  strength_modifier = process_ability_score(creature, level, "strength")
  dexterity_modifier = process_ability_score(creature, level,
                                             "dexterity")
  constitution_modifier = process_ability_score(creature, level,
                                                "constitution")
  intelligence_modifier = process_ability_score(creature, level,
                                                "intelligence")
  wisdom_modifier = process_ability_score(creature, level, "wisdom")
  charisma_modifier = process_ability_score(creature, level, "charisma")

  perception_modifier = process_perception(creature, level)

  skill_modifiers = process_skills(creature, level)

  armor_class = process_armor_class(creature, level)

  fortitude = process_saving_throw(creature, level, "fortitude")
  reflex = process_saving_throw(creature, level, "reflex")
  will = process_saving_throw(creature, level, "will")

  hit_points = process_hit_points(creature, level)

  resistances = process_resistances_or_weaknesses(creature, level, "resistances")
  weaknesses = process_resistances_or_weaknesses(creature, level, "weaknesses")

  print("level", level)
  print("strength", strength_modifier)
  print("dexterity", dexterity_modifier)
  print("constitution", constitution_modifier)
  print("intelligence", intelligence_modifier)
  print("wisdom", wisdom_modifier)
  print("charisma", charisma_modifier)

  print("perception", perception_modifier)
  print("skilss", skill_modifiers)

  print("armor_class", armor_class)

  print("fortitude", fortitude)
  print("reflex", reflex)
  print("will", will)
  
  print("hit_points", hit_points)

  print("resistances", resistances)
  print("weaknesses", weaknesses)

