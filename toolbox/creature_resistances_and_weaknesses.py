from toolbox import general
from tables import creature_resistances_and_weaknesses


def process_resistances_or_weaknesses(creature, resistance_or_weakness):
  level = general.process_level(creature)
  level_index = general.level_index_lookup(level)

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
