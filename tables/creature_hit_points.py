low_hit_points_floor = [
    5, 11, 14, 21, 31, 41, 53, 67, 82, 97, 112, 127, 142, 157, 172, 187, 202,
    217, 232, 247, 262, 277, 295, 317, 339, 367
]
low_hit_points_ceiling = [
    6, 13, 16, 25, 37, 48, 59, 75, 90, 105, 120, 135, 150, 165, 180, 195, 210,
    225, 240, 255, 270, 285, 305, 329, 351, 383
]
moderate_hit_points_floor = [
    7, 14, 19, 28, 42, 57, 72, 91, 111, 131, 151, 171, 191, 211, 231, 251, 271,
    291, 311, 331, 351, 371, 395, 424, 454, 492
]
moderate_hit_points_ceiling = [
    8, 16, 21, 32, 48, 63, 78, 99, 119, 139, 159, 179, 199, 219, 239, 259, 279,
    299, 319, 339, 359, 379, 405, 436, 466, 508
]
high_hit_points_floor = [
    9, 17, 24, 36, 53, 72, 91, 115, 140, 165, 190, 215, 240, 275, 290, 315,
    340, 365, 390, 415, 440, 465, 495, 532, 569, 617
]
high_hit_points_ceiling = [
    9, 20, 26, 40, 59, 78, 97, 123, 148, 173, 198, 223, 248, 273, 298, 323,
    348, 373, 398, 423, 448, 479, 505, 544, 581, 633
]

table = {
    "low": {
        "floor": low_hit_points_floor,
        "ceiling": low_hit_points_ceiling
    },
    "moderate": {
        "floor": moderate_hit_points_floor,
        "ceiling": moderate_hit_points_ceiling
    },
    "high": {
        "floor": high_hit_points_floor,
        "ceiling": high_hit_points_ceiling
    }
}
