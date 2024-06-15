def process_type(item):
  if "type" not in item:
    raise Exception("Missing Type")

  return item["type"].lower()


def process_name(item):
  if "name" not in item:
    raise Exception("Missing Name")

  return item["name"]


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
