import math

from toolbox import general
from tables import creature_strike_attack_bonus
from tables import creature_strike_damage


def process_strikes(creature):
  level = general.process_level(creature)
  level_index = general.level_index_lookup(level)

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
