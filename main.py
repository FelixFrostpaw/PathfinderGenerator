import json

def main():
    with open('input.json') as f:
        data = json.load(f)

    print(data)
    print(creature_ability_modifiers())

def valid_level(num):
  if -1 <= num <= 24:
    return True
  else:
    return False

def number_of_levels():
  return 26

def creature_ability_modifiers():
  low_abilities = [0, 0, 1, 1, 
                   1, 2, 2, 2, 
                   2, 3, 3, 3, 
                   3, 4, 4, 4, 
                   4, 5, 5, 5, 
                   5, 6, 6, 6, 6, 7]

  moderate_abilities = [2, 2, 3, 3, 
                        3, 3, 4, 4, 
                        4, 4, 4, 5, 
                        5, 5, 5, 5, 
                        6, 6, 6, 6, 
                        6, 7, 7, 8, 8, 9]

  high_abilities = [3, 3, 4, 4, 
                    4, 5, 5, 5, 
                    6, 6, 6, 7, 
                    7, 7, 8, 8, 
                    8, 9, 9, 9, 
                    10, 10, 10, 10, 10, 12]

  extreme_abilities = [5, 5, 5, 5, 
                       5, 6, 6, 7, 
                       7, 7, 7, 8, 
                       8, 8, 9, 9, 
                       9, 10, 10, 10, 
                       11, 11, 11, 11, 11, 13]

  creature_ability_modifiers = [
    low_abilities, 
    moderate_abilities, 
    high_abilities, 
    extreme_abilities]

  return creature_ability_modifiers

def creature_perceptions():
  terrible_perceptions = [0, 1, 2, 3, 
                          4, 6, 7, 8, 
                          10, 11, 12, 14, 
                          15, 16, 18, 19, 
                          20, 22, 23, 24, 
                          26, 27, 28, 30, 31, 32]
  
  low_perceptions = [2, 3, 4, 5, 
                     6, 8, 9, 11, 
                     12, 13, 15, 16, 
                     18, 19, 20, 22, 
                     23, 25, 26, 27, 
                     29, 30 , 32, 33, 34, 36]
  
  moderate_perceptions = [5, 6, 7, 8, 
                          9, 11, 12, 14, 
                          15, 16, 18, 19, 
                          21 ,22, 23, 25, 
                          26, 28, 29, 30, 
                          32, 33, 35, 36, 37, 38]
  
  high_perceptions = [8, 9, 10, 11, 
                      12, 14, 15, 17, 
                      18, 19, 21, 22, 
                      24, 25, 26, 28, 
                      29, 30, 32, 33, 
                      35, 36, 38, 39, 40, 42]
  
  extreme_perceptions = [9, 10, 11, 12, 
                         14, 15, 17, 18, 
                         20, 21, 23, 24, 
                         26, 27, 29, 30, 
                         32, 33, 35, 36, 
                         38, 39, 41, 43, 44, 46]

  creature_perceptions = [
    terrible_perceptions,
    low_perceptions,
    moderate_perceptions,
    high_perceptions,
    extreme_perceptions]

  return creature_perceptions

def creature_skills():
  terrible_skills = [1, 2, 3, 4,
                     5, 7, 8, 9,
                     11, 12, 13, 15,
                     16, 17, 19, 20,
                     21, 23, 24, 25,
                     27, 28, 29, 31, 32, 33]
  low_skills = [2, 3, 4, 5,
                7, 8, 10, 11,
                13, 14, 16, 17,
                19, 20, 22, 23,
                25, 26, 28, 29,
                31, 32, 34, 35, 36, 38]
  moderate_skills = [4, 5, 5, 7,
                     9, 10, 12, 13,
                     15, 16, 18, 19,
                     21, 22, 24, 25,
                     27, 26, 30, 31,
                     33, 34, 36, 37, 38, 40]
  high_skills = [5, 6, 7, 8,
                 10, 12, 13, 15,
                 17, 18, 20, 22,
                 23, 25, 27, 28,
                 30, 32, 33, 35,
                 37, 38, 40, 42, 43, 45]
  
  extreme_skills = [8, 9, 10, 11,
                    13, 15, 16, 18,
                    20, 21, 23, 25,
                    26, 28, 30, 31,
                    33, 35, 36, 38,
                    40, 41, 43, 45, 46, 48]
  
  creature_skills = [
    terrible_skills,
    low_skills,
    moderate_skills,
    high_skills,
    extreme_skills]
  
  return creature_skills

def creature_armor_class():
  low_armor_class = [12, 13, 13, 15,
                     16, 18, 19, 21,
                     22, 24, 25, 27,
                     28, 30, 31, 33,
                     34, 36, 37, 39,
                     40, 42, 43, 45, 46, 48]
  moderate_armor_class = [14, 15, 15, 17,
                          18, 20, 21, 23,
                          24, 26, 27, 29,
                          30, 32, 33, 35,
                          36, 38, 39, 40,
                          42, 44, 45, 47, 48, 50]
  high_armor_class = [15, 16, 16, 18,
                      19, 20, 22, 24,
                      25, 27, 28, 30,
                      31, 33, 34, 36,
                      37, 39, 40, 42,
                      43, 45, 46, 48, 49, 51]
  extreme_armor_class = [18, 19, 19, 21,
                         22, 24, 25, 27,
                         28, 30, 31, 33,
                         34, 36, 37, 39,
                         40, 42, 43, 45,
                         46, 48, 49, 51, 52, 54]
  creature_armor_class = [
    low_armor_class,
    moderate_armor_class,
    high_armor_class,
    extreme_armor_class]
  return creature_armor_class

def creature_saves():
  terrible_saves = [0, 1, 2, 3,
                    4, 6, 7, 8,
                    10, 11, 12, 14,
                    15, 16, 18, 19,
                    20, 22, 23, 24,
                    26, 27, 28, 30, 31, 32]
  low_saves = [2, 3, 4, 5,
               6, 8, 9, 11,
               12, 13, 15, 16,
               18, 19, 20, 22,
               23, 25, 26, 27,
               29, 30, 32, 33, 34, 36]
  moderate_saves = [5, 6, 7, 8,
                    9, 11, 12, 14,
                    15, 16, 18, 19,
                    21, 22, 23, 25,
                    26, 28, 29, 30,
                    32, 33, 35, 36, 37, 38]
  high_saves = [8, 9, 10, 11,
                12, 14, 15, 17,
                18, 19, 20, 22,
                24, 25, 26, 28,
                29, 30, 32, 33,
                35, 36, 38, 39, 40, 42]
  extreme_saves = [9, 10, 11, 12,
                   14, 15, 17, 18,
                   20, 21, 23, 24,
                   26, 27, 29, 30,
                   32, 33, 35, 36,
                   38, 39, 40, 43, 44, 46]
  creature_saves = [
    terrible_saves,
    low_saves,
    moderate_saves,
    high_saves,
    extreme_saves]
  return creature_saves

def creature_health():
  low_health_floor = [5, 11, 14, 21,
                    31, 41, 53, 67,
                    82, 97, 112, 127,
                    142, 157, 172, 187,
                    202, 217, 232, 247,
                    262, 277, 295, 317, 339, 367]
  low_health_ceiling = [6, 13, 16, 25,
                        37, 48, 59, 75,
                        90, 105, 120, 135,
                        150, 165, 180, 195,
                        210, 225, 240, 255,
                        270, 285, 305, 329, 351, 383]
  moderate_health_floor = [7, 14, 19, 28,
                           42, 57, 72, 91,
                           111, 131, 151, 171,
                           191, 211, 231, 251,
                           271, 291, 311, 331,
                           351, 371, 395, 424, 454, 492]
  moderate_health_ceiling = [8, 16, 21, 32,
                             48, 63, 78, 99,
                             119, 139, 159, 179,
                             199, 219, 239, 259,
                             279, 299, 319, 339,
                             359, 379, 405, 436, 466, 508]
  high_health_floor = [9, 17, 24, 36,
                       53, 72, 91, 115,
                       140, 165, 190, 215,
                       240, 275, 290, 315,
                       340, 365, 390, 415,
                       440, 465, 495, 532, 569, 617]
  high_health_ceiling = [9, 20, 26, 40,
                         59, 78, 97, 123,
                         148, 173, 198, 223,
                         248, 273, 298, 323,
                         348, 373, 398, 423,
                         448, 479, 505, 544, 581, 633]
  creature_health = [
    low_health_floor, low_health_ceiling,
    moderate_health_floor, moderate_health_ceiling,
    high_health_floor, high_health_ceiling
    ]
  return creature_health

def creature_res_mod():
  res_mod_floor = [1, 1, 2, 2,
                   3, 4, 4, 5,
                   5, 6, 6, 7,
                   7, 8, 8, 9,
                   9, 9, 10, 10,
                   11, 11, 12, 12, 13, 13]
  res_mod_ceiling = [1, 3, 3, 5,
                     6, 7, 8, 9,
                     10, 11, 12, 13,
                     14, 15, 16, 17,
                     18, 19, 19, 20,
                     21, 22, 23, 24, 25, 26]
  creature_res_mod = [res_mod_floor, res_mod_ceiling]
  return creature_res_mod

def creature_strike_hit():
  low_strike = [4, 4, 5, 7,
                8, 9, 11, 12,
                13, 15, 16, 17,
                19, 20, 21, 23,
                24, 25, 27, 28,
                29, 30, 32, 33, 35, 36]
  moderate_strike = [6, 6, 7, 9,
                     10, 12, 13, 15,
                     16, 18, 19, 21,
                     22, 24, 25, 27,
                     28, 30, 31, 33,
                     34, 36, 37, 39, 40, 42]
  high_strike = [8, 8, 9, 11,
                 12, 14, 15, 17,
                 18, 20, 21, 23,
                 24, 26, 27, 29,
                 30, 32, 33, 35,
                 36, 38, 39, 41, 42, 44]
  extreme_strike = [10, 10, 11, 13,
                    14, 16, 17, 19,
                    20, 22, 23, 25,
                    27, 28, 29, 31,
                    32, 34, 35, 37,
                    38, 40, 41, 43, 44, 46]
  creature_strike_hit = [
    low_strike,
    moderate_strike,
    high_strike,
    extreme_strike
  ]
  return creature_strike_hit

def creature_strike_damage():
  low_strike_damage = [2, 3, 4, 6,
                       8, 9, 11, 12,
                       13, 15, 16, 17,
                       19, 20, 21, 23,
                       24, 25, 26, 27,
                       28, 29, 31, 32, 33, 35]
  moderate_strike_damage = [3, 4, 5, 8,
                            10, 12, 13, 15,
                            17, 18, 20, 22,
                            23, 25, 27, 28,
                            30, 31, 32, 33,
                            35, 37, 38, 40, 42, 44]
  high_strike_damage = [3, 5, 6, 9,
                        12, 14, 16, 18,
                        20, 22, 24, 26,
                        28, 30, 32, 34,
                        36, 37, 38, 40,
                        42, 44, 46, 48, 50, 52]
  extreme_strike_damage = [4, 6, 8, 11,
                           15, 18, 20, 23,
                           25, 28, 30, 33,
                           35, 38, 40, 43,
                           45, 48, 50, 53,
                           55, 58, 60, 63, 65, 68]
  creature_strike_damage = [
    low_strike_damage,
    moderate_strike_damage,
    high_strike_damage,
    extreme_strike_damage]
  return creature_strike_damage

def creature_spell_hit():
  #Spell DC is always 8 points higher than strike
  moderate_spell_hit = [5, 5, 6, 7,
                        9, 10, 11, 13,
                        14, 15, 17, 18,
                        19, 21, 22, 23,
                        25, 26, 27, 29,
                        30, 31, 33, 34, 35, 37]
  high_spell_hit = [8, 8, 9, 10,
                    12, 13, 14, 16,
                    17, 18, 20, 21,
                    22, 24, 25, 26,
                    28, 29, 30, 32,
                    33, 34, 36, 37, 38, 40]
  extreme_spell_hit = [11, 11, 12, 14,
                       15, 17, 18, 19,
                       21, 22, 24, 25,
                       26, 28, 29, 31,
                       32, 33, 35, 36,
                       38, 39, 40, 42, 43, 44]
  creature_spell_hit = [
    moderate_spell_hit,
    high_spell_hit,
    extreme_spell_hit]
  return creature_spell_hit

def creature_area_damage():
  at_will_damage = [2, 4, 5, 7,
                    9, 11, 12, 14,
                    15, 17, 18, 20,
                    21, 23, 24, 26,
                    27, 28, 29, 30,
                    32, 33, 35, 36, 38, 39]
  limited_damage = [4, 6, 7, 11,
                    14, 18, 21, 25,
                    28, 32, 35, 39,
                    42, 46, 49, 53,
                    56, 60, 63, 67,
                    70, 74, 77, 81, 84, 88]
  creature_area_damage = [
    at_will_damage,
    limited_damage
  ]
  return creature_area_damage

def hazard_stealth_and_disable_dc():
  #Complex Hazards reduce this DC by 10
  extreme_dcs = [18, 19, 20, 21,
                 23, 25, 26, 28,
                 30, 31, 33, 35,
                 36, 38, 40, 41,
                 43, 45, 46, 48,
                 50, 51, 53, 55, 56, 58]
  high_dcs = [15, 16, 17, 18,
              20, 22, 23, 25,
              27, 28, 30, 32,
              33, 35, 37, 38,
              40, 42, 43, 45,
              47, 48, 50, 52, 53, 55]
  low_dcs = [12, 13, 14, 15,
             17, 18, 20, 21,
             23, 24, 26, 27,
             29, 30, 32, 33,
             35, 36, 38, 39,
             40, 42, 44, 45, 46, 48]
  terrible_dcs = [11, 12, 13, 14,
                  15, 17, 18, 19,
                  21, 22, 23, 25,
                  26, 27, 29, 30,
                  31, 33, 34, 35,
                  37, 38, 39, 40, 42, 43]

def hazard_ac():
  extreme_acs = [18, 19, 19, 21,
                 22, 24, 25, 27,
                 28, 30, 31, 33,
                 34, 36, 37, 39,
                 40, 42, 43, 45,
                 46, 48, 49, 51, 52, 54]
  high_acs = [15, 16, 16, 18,
              19, 21, 22, 24,
              25, 27, 28, 30,
              31, 33, 34, 36,
              37, 39, 40, 42,
              43, 45, 46, 48, 49, 51]
  low_acs = [12, 13, 13, 15,
             16, 18, 19, 21, 
             22, 24, 25, 27,
             28, 30, 31, 33, 
             34, 36, 37, 39,
             40, 42, 43, 45, 46, 48]

def hazard_save():
  extreme_saves = [9, 10, 11, 15,
                   14, 15, 17, 18,
                   20, 21, 23, 24,
                   26, 27, 29, 30,
                   32, 33, 35, 36,
                   38, 39, 41, 43, 44, 46]
  high_saves = [8, 9, 10, 11,
                12, 14, 15, 17,
                18, 19, 21, 22,
                24, 25, 26, 28,
                29, 30, 32, 33,
                35, 36, 38, 39, 40, 42]
  low_saves = [2, 3, 4, 5,
               6, 8, 9, 11,
               12, 13, 15, 16,
               18, 19, 20, 22,
               23, 25, 26, 27,
               29, 30, 32, 33, 34, 36]

def hazard_hardness():
  low_hardness = [2, 3, 5, 7,
                  10, 11, 12, 13,
                  14, 15, 16, 17,
                  19, 20, 21, 22,
                  23, 25, 27, 29,
                  31, 33, 36, 39, 44, 46]
  high_hardness = [4, 5, 7, 9,
                   12, 13, 14, 15,
                   16, 17, 18, 19,
                   21, 22, 23, 24,
                   25, 27, 29, 31,
                   33, 35, 38, 41, 46, 50]
  
def hazard_hp():
  low_hp = [11, 15, 23, 30,
            42, 46, 50, 54,
            58, 62, 66, 70,
            78, 82, 86, 90,
            94, 101, 109, 117,
            125, 133, 144, 156, 168, 180]
  high_hp = [13, 17, 25, 34,
             46, 50, 54, 58,
             62, 66, 70, 78,
             82, 84, 90, 94,
             98, 107, 115, 123,
             131, 139, 152, 164, 176, 188]

def hazard_attack_hit():
  simple_attack_hit = [10, 11, 13, 14,
                       16, 17, 19, 20,
                       22, 23, 25, 26,
                       28, 29, 31, 32,
                       34, 35, 37, 38,
                       40, 41, 43, 44, 46, 47]
  complex_attack_hit = [8, 8, 9, 11,
                        12, 14, 15, 17,
                        18, 20, 21, 23,
                        24, 26, 27, 29,
                        30, 32, 33, 35,
                        36, 38, 39, 41, 42, 44]

def hazard_damage():
  simple_attack_damage = [6, 10, 12, 18,
                          24, 28, 32, 36,
                          40, 44, 48, 52,
                          56, 60, 64, 68,
                          72, 74, 76, 80,
                          84, 88, 92, 96, 100, 104]
  complex_attack_damage = [3, 5, 6, 9,
                           12, 14, 16, 18,
                           20, 22, 24, 26,
                           28, 30, 32, 34,
                           36, 37, 38, 40,
                           42, 44, 46, 48, 50, 52]

def level_dcs():
  dc_by_level = [13, 14, 15, 16, 
                       18, 19, 20, 22, 
                       23, 24, 26, 27, 
                       28, 30, 31, 32, 
                       34, 35, 36, 38, 
                       39, 40, 42, 44, 46, 48, 
                       50]

  return dc_by_level 

def spell_dcs():
  
  levelled_spell_dcs = [15, 18, 20, 23, 
                       26, 28, 31, 34, 36, 39]

  return levelled_spell_dcs

def dc_adjustments():
  dc_adjustments = [-10, -5, -2, 2, 5, 10]

  return dc_adjustments

if __name__ == '__main__':
    main()