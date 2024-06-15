from toolbox import general
from tables import creature_armor_class
from tables import creature_saves


def process_armor_class(creature):
  level = general.process_level(creature)
  level_index = general.level_index_lookup(level)

  if "armor_class" not in creature:
    raise Exception("Missing Armor Class")

  armor_class_input = creature["armor_class"]

  if armor_class_input not in creature_armor_class.table:
    raise Exception(f"Invalid Armor Class Descriptor: {armor_class_input}")

  armor_class = creature_armor_class.table[armor_class_input][level_index]

  return armor_class


def process_saving_throw(creature, saving_throw):
  level = general.process_level(creature)
  level_index = general.level_index_lookup(level)

  if saving_throw not in ["fortitude", "reflex", "will"]:
    raise Exception(f"Invalid Saving Throw: {saving_throw}")

  if saving_throw not in creature:
    raise Exception(f"Missing Saving Throw: {saving_throw}")

  saving_throw_input = creature[saving_throw]

  if saving_throw_input not in creature_saves.table:
    raise Exception(f"Invalid Saving Throw Descriptor: {saving_throw_input}")

  saving_throw_modifier = creature_saves.table[saving_throw_input][level_index]

  return saving_throw_modifier
