import json
from toolbox import toolbox


def main():
  with open('input.json') as f:
    data = json.load(f)

  items = data['items']
  # print(items)

  for item in items:
    output = ""

    item_type = item['type'].lower()

    if toolbox.valid_types(item_type) == False:
      raise Exception("Invalid Type")

    if item_type == "creature":
      # do creature stuff
      toolbox.process_creature(item)

    if item_type == "hazard":
      # do hazard stuff
      pass

    print(output)


if __name__ == '__main__':
  main()
