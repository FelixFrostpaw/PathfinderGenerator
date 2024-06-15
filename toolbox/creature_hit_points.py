from toolbox import general
from tables import creature_hit_points


def process_hit_points(creature):
  level = general.process_level(creature)
  level_index = general.level_index_lookup(level)

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
