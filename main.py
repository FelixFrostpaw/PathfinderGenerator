import json
from toolbox import process_types
from toolbox import general


def main():
  with open('input.json') as f:
    data = json.load(f)

  items = data['items']

  for item in items:
    output = ""

    item_type = general.process_type(item)

    if not general.valid_types(item_type):
      raise Exception("Invalid Type")

    if item_type == "creature":
      # do creature stuff
      process_types.process_creature(item)

    if item_type == "hazard":
      # do hazard stuff
      pass

    print(output)


if __name__ == '__main__':
  main()
