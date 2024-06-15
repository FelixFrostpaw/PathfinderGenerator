import pprint

from toolbox import general

from toolbox import creature_ability_scores
from toolbox import creature_perception
from toolbox import creature_skills
from toolbox import creature_defenses
from toolbox import creature_hit_points
from toolbox import creature_resistances_and_weaknesses
from toolbox import creature_strikes
from toolbox import creature_spells
from toolbox import creature_special_abilities


def process_creature(creature):
  name = general.process_name(creature)

  level = general.process_level(creature)

  strength_modifier = creature_ability_scores.process_ability_score(
      creature, "strength")
  dexterity_modifier = creature_ability_scores.process_ability_score(
      creature, "dexterity")
  constitution_modifier = creature_ability_scores.process_ability_score(
      creature, "constitution")
  intelligence_modifier = creature_ability_scores.process_ability_score(
      creature, "intelligence")
  wisdom_modifier = creature_ability_scores.process_ability_score(
      creature, "wisdom")
  charisma_modifier = creature_ability_scores.process_ability_score(
      creature, "charisma")

  perception_modifier = creature_perception.process_perception(creature)

  skill_modifiers = creature_skills.process_skills(creature)

  armor_class = creature_defenses.process_armor_class(creature)

  fortitude = creature_defenses.process_saving_throw(creature, "fortitude")
  reflex = creature_defenses.process_saving_throw(creature, "reflex")
  will = creature_defenses.process_saving_throw(creature, "will")

  hit_points = creature_hit_points.process_hit_points(creature)

  resistances = creature_resistances_and_weaknesses.process_resistances_or_weaknesses(
      creature, "resistances")
  weaknesses = creature_resistances_and_weaknesses.process_resistances_or_weaknesses(
      creature, "weaknesses")

  strikes = creature_strikes.process_strikes(creature)

  spell_attack_bonus = creature_spells.process_spell_attack_bonus(creature)
  spell_dc = creature_spells.process_spell_dc(creature)

  special_abilities = creature_special_abilities.process_special_abilities(
      creature)

  print("name", name)

  print()

  print("level", level)
  print("strength", strength_modifier)
  print("dexterity", dexterity_modifier)
  print("constitution", constitution_modifier)
  print("intelligence", intelligence_modifier)
  print("wisdom", wisdom_modifier)
  print("charisma", charisma_modifier)

  print()

  print("perception", perception_modifier)
  print("skills", skill_modifiers)

  print()

  print("armor_class", armor_class)

  print()

  print("fortitude", fortitude)
  print("reflex", reflex)
  print("will", will)

  print()

  print("hit_points", hit_points)

  print()

  print("resistances", resistances)
  print("weaknesses", weaknesses)

  print()

  print("strikes")
  pprint.pp(strikes)

  print()

  print("spell_attack_bonus", spell_attack_bonus)
  print("spell_dc", spell_dc)

  print()

  print("special_abilities")
  pprint.pp(special_abilities)


# def process_hazard(hazard):
# name = general.process_name(hazard)

# level = general.process_level(hazard)

# simple_or_complex = toolbox.hazard_type(hazard)
# hazard_type = toolbox.hazard_type(hazard)

# stealth = toolbox.hazard_stealth(hazard)
# stealth_modifier = stealth - 10

# disable = toolbox.hazard_disable(hazard)
