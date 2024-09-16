# random_dirt.py

import random

def randomDirtOnTiles() -> list:
    # Randomly assign dirt (0 or 1) to two tiles
    return [random.choice([0, 1]), random.choice([0, 1])]
