from toolbox import general
from tables import creature_perceptions


def process_perception(creature):
  level = general.process_level(creature)
  level_index = general.level_index_lookup(level)

  if "perception" not in creature:
    raise Exception("Missing Perception")

  perception_input = creature["perception"]

  if perception_input not in creature_perceptions.table:
    raise Exception(f"Invalid Perception Descriptor: {perception_input}")

  perception_modifier = creature_perceptions.table[perception_input][
      level_index]

  return perception_modifier
