import random
import math

from tables import creature_ability_modifiers
from tables import creature_area_damage
from tables import creature_armor_class
from tables import creature_hit_points
from tables import creature_perceptions
from tables import creature_resistances_and_weaknesses
from tables import creature_saves
from tables import creature_skills
from tables import creature_spell_attack_bonus
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


def level_index_lookup(level):
  return level + 1


def valid_types(input_type):
  return input_type == "creature" or input_type == "hazard"


def process_level(creature):
  if "level" not in creature:
    raise Exception("Missing Creature Level")

  level = creature['level']

  if not valid_level(level):
    raise Exception(f"Invalid Creature Level: {level}")

  return level


def process_ability_score(creature, ability_score):
  level = process_level(creature)
  level_index = level_index_lookup(level)

  if ability_score not in [
      "strength", "dexterity", "constitution", "intelligence", "wisdom",
      "charisma"
  ]:
    raise Exception("Invalid Ability Score")

  if ability_score not in creature:
    raise Exception(f"Missing {ability_score}")

  ability_score_input = creature[ability_score]

  if ability_score_input not in creature_ability_modifiers.table:
    raise Exception(f"Invalid Ability Score Descriptor: {ability_score}")

  ability_score_modifier = creature_ability_modifiers.table[
      ability_score_input][level_index]

  return ability_score_modifier


def process_perception(creature):
  level = process_level(creature)
  level_index = level_index_lookup(level)

  if "perception" not in creature:
    raise Exception("Missing Perception")

  perception_input = creature["perception"]

  if perception_input not in creature_perceptions.table:
    raise Exception(f"Invalid Perception Descriptor: {perception_input}")

  perception_modifier = creature_perceptions.table[perception_input][
      level_index]

  return perception_modifier


def process_skills(creature):
  level = process_level(creature)
  level_index = level_index_lookup(level)

  if "skills" not in creature:
    return {}

  skill_modifiers = {}

  for skill, skill_descriptor in creature["skills"].items():
    if skill_descriptor not in creature_skills.table:
      raise Exception(
          f"Invalid Skill Descriptor for {skill}: {skill_descriptor}")

    skill_modifier = creature_skills.table[skill_descriptor][level_index]

    skill_modifiers[skill] = skill_modifier

  return skill_modifiers


def process_armor_class(creature):
  level = process_level(creature)
  level_index = level_index_lookup(level)

  if "armor_class" not in creature:
    raise Exception("Missing Armor Class")

  armor_class_input = creature["armor_class"]

  if armor_class_input not in creature_armor_class.table:
    raise Exception(f"Invalid Armor Class Descriptor: {armor_class_input}")

  armor_class = creature_armor_class.table[armor_class_input][level_index]

  return armor_class


def process_saving_throw(creature, saving_throw):
  level = process_level(creature)
  level_index = level_index_lookup(level)

  if saving_throw not in ["fortitude", "reflex", "will"]:
    raise Exception(f"Invalid Saving Throw: {saving_throw}")

  if saving_throw not in creature:
    raise Exception(f"Missing Saving Throw: {saving_throw}")

  saving_throw_input = creature[saving_throw]

  if saving_throw_input not in creature_saves.table:
    raise Exception(f"Invalid Saving Throw Descriptor: {saving_throw_input}")

  saving_throw_modifier = creature_saves.table[saving_throw_input][level_index]

  return saving_throw_modifier


def process_hit_points(creature):
  level = process_level(creature)
  level_index = level_index_lookup(level)

  if "hp" not in creature:
    raise Exception("Missing Hit Points")

  if "hp_algorithm" not in creature:
    raise Exception("Missing Hit Points Algorithm")

  hp_input = creature["hp"]
  hp_algorithm_input = creature["hp_algorithm"]

  if hp_input not in creature_hit_points.table:
    raise Exception(f"Invalid HP Descriptor: {hp_input}")

  if hp_algorithm_input not in [
      "floor", "ceiling", "average", "range", "random"
  ]:
    raise Exception(f"Invalid HP Algorithm: {hp_algorithm_input}")

  hp_floor = creature_hit_points.table[hp_input]["floor"][level_index]
  hp_ceiling = creature_hit_points.table[hp_input]["ceiling"][level_index]

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
    raise Exception(f"Invalid HP Algorithm! {hp_algorithm_input}")

  return hp


def process_resistances_or_weaknesses(creature, resistance_or_weakness):
  level = process_level(creature)
  level_index = level_index_lookup(level)

  if resistance_or_weakness not in ["resistances", "weaknesses"]:
    raise Exception(
        f"Invalid - Not a Resistance or Weakness: {resistance_or_weakness}")

  if resistance_or_weakness not in creature:
    return {}

  resistance_or_weakness_input = creature[resistance_or_weakness]

  resistances_or_weaknesses = {}

  for resistance_or_weakness_descriptor, resistance_or_weakness_value in resistance_or_weakness_input.items(
  ):
    if resistance_or_weakness_value not in ["minimum", "maximum", "average"]:
      raise Exception(
          f"Invalid Resistance or Weakness Descriptor: {resistance_or_weakness_value}"
      )

    resistance_or_weakness_minimum = creature_resistances_and_weaknesses.table[
        "minimum"][level_index]
    resistance_or_weakness_maximum = creature_resistances_and_weaknesses.table[
        "maximum"][level_index]

    resistance_or_weakness = 0

    if resistance_or_weakness_value == "minimum":
      resistance_or_weakness = resistance_or_weakness_minimum
    elif resistance_or_weakness_value == "maximum":
      resistance_or_weakness = resistance_or_weakness_maximum
    elif resistance_or_weakness_value == "average":
      resistance_or_weakness = int(
          (resistance_or_weakness_minimum + resistance_or_weakness_maximum) /
          2)
    else:
      raise Exception(
          f"Invalid Resistance or Weakness Value! {resistance_or_weakness_value}"
      )

    resistances_or_weaknesses[
        resistance_or_weakness_descriptor] = resistance_or_weakness

  return resistances_or_weaknesses


def process_strikes(creature):
  level = process_level(creature)
  level_index = level_index_lookup(level)

  if "strikes" not in creature:
    return {}

  strikes = {}

  for strike, strike_data in creature["strikes"].items():
    if "bonus" not in strike_data:
      raise Exception("Missing Strike Bonus")

    if strike_data["bonus"] not in creature_strike_attack_bonus.table:
      raise Exception(f"Invalid Bonus Descriptor: {strike_data['bonus']}")

    if "damage" not in strike_data:
      raise Exception("Missing Strike Damage")

    if strike_data["damage"] not in creature_strike_damage.table:
      raise Exception(f"Invalid Damage Descriptor: {strike_data['damage']}")

    if "damage_algorithm" not in strike_data:
      raise Exception("Missing Strike Damage Algorithm")

    if strike_data["damage_algorithm"] not in [
        "d4", "d6", "d8", "d10", "d12", "number"
    ]:
      raise Exception(
          f"Invalid Damage Algorithm: {strike_data['damage_algorithm']}")

    strike_bonus = creature_strike_attack_bonus.table[
        strike_data["bonus"]][level_index]

    strike_damage = creature_strike_damage.table[
        strike_data["damage"]][level_index]

    strike_damage_algorithm_input = strike_data["damage_algorithm"]

    strike_damage_algorithm = process_strike_damage_algorithm(
        strike_damage, strike_damage_algorithm_input, level)

    if strike_damage_algorithm_input == "number":
      strike_damage_algorithm = strike_damage

    strikes[strike] = {
        "bonus": strike_bonus,
        "damage": strike_damage_algorithm
    }

  return strikes


def process_strike_damage_algorithm(strike_damage, strike_damage_algorithm,
                                    level):

  if strike_damage_algorithm == "number":
    return strike_damage

  number_of_dice = 0

  if -1 <= level <= 3:
    number_of_dice = 1
  elif 4 <= level <= 11:
    number_of_dice = 2
  elif 12 <= level <= 18:
    number_of_dice = 3
  elif 19 <= level <= 24:
    number_of_dice = 4
  else:
    raise Exception(f"Invalid Level: {level}")

  dice_conversion = 0

  if strike_damage_algorithm == "d4":
    dice_conversion = 2.5
  elif strike_damage_algorithm == "d6":
    dice_conversion = 3.5
  elif strike_damage_algorithm == "d8":
    dice_conversion = 4.5
  elif strike_damage_algorithm == "d10":
    dice_conversion = 5.5
  elif strike_damage_algorithm == "d12":
    dice_conversion = 6.5
  else:
    raise Exception(f"Invalid Damage Algorithm: {strike_damage_algorithm}")

  dice_average = int(math.floor(number_of_dice * dice_conversion))

  if dice_average >= strike_damage:
    return f"{number_of_dice}{strike_damage_algorithm}"
  else:
    leftover = strike_damage - dice_average
    return f"{number_of_dice}{strike_damage_algorithm} + {leftover}"


def process_spell_attack_bonus(creature):
  level = process_level(creature)
  level_index = level_index_lookup(level)

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
  level = process_level(creature)
  level_index = level_index_lookup(level)

  spell_dc_adjustment = 8

  if "spell_attack_bonus" not in creature:
    return 0

  spell_attack_bonus_input = creature["spell_attack_bonus"]

  if spell_attack_bonus_input not in creature_spell_attack_bonus.table:
    raise Exception(
        f"Invalid Spell Attack Bonus Descriptor: {spell_attack_bonus_input}")

  spell_attack_bonus = creature_spell_attack_bonus.table[
      spell_attack_bonus_input][level_index]

  spell_dc = spell_attack_bonus + spell_dc_adjustment

  return spell_dc


def process_creature(creature):
  level = process_level(creature)

  strength_modifier = process_ability_score(creature, "strength")
  dexterity_modifier = process_ability_score(creature, "dexterity")
  constitution_modifier = process_ability_score(creature, "constitution")
  intelligence_modifier = process_ability_score(creature, "intelligence")
  wisdom_modifier = process_ability_score(creature, "wisdom")
  charisma_modifier = process_ability_score(creature, "charisma")

  perception_modifier = process_perception(creature)

  skill_modifiers = process_skills(creature)

  armor_class = process_armor_class(creature)

  fortitude = process_saving_throw(creature, "fortitude")
  reflex = process_saving_throw(creature, "reflex")
  will = process_saving_throw(creature, "will")

  hit_points = process_hit_points(creature)

  resistances = process_resistances_or_weaknesses(creature, "resistances")
  weaknesses = process_resistances_or_weaknesses(creature, "weaknesses")

  strikes = process_strikes(creature)

  spell_attack_bonus = process_spell_attack_bonus(creature)
  spell_dc = process_spell_dc(creature)

  print("level", level)
  print("strength", strength_modifier)
  print("dexterity", dexterity_modifier)
  print("constitution", constitution_modifier)
  print("intelligence", intelligence_modifier)
  print("wisdom", wisdom_modifier)
  print("charisma", charisma_modifier)

  print()

  print("perception", perception_modifier)
  print("skilss", skill_modifiers)

  print()

  print("armor_class", armor_class)

  print()

  print("fortitude", fortitude)
  print("reflex", reflex)
  print("will", will)

  print()

  print("hit_points", hit_points)

  print()

  print("resistances", resistances)
  print("weaknesses", weaknesses)

  print()

  print("strikes", strikes)

  print()

  print("spell_attack_bonus", spell_attack_bonus)
  print("spell_dc", spell_dc)
