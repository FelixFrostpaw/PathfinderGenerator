from toolbox import general
from tables import creature_skills


def process_skills(creature):
  level = general.process_level(creature)
  level_index = general.level_index_lookup(level)

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
