from toolbox import general
from tables import creature_ability_modifiers


def process_ability_score(creature, ability_score):
  level = general.process_level(creature)
  level_index = general.level_index_lookup(level)

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
