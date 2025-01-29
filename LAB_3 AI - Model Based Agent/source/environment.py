# environment.py
import random

def create_room():
    room = []
    for _ in range(8):
        row = []
        for _ in range(8):
            value = random.choice(["path", "path", "object", "hurdle"])
            row.append(value)
        room.append(row)
    return room

def start():
    x = random.randint(1, 6)
    y = random.randint(1, 6)
    return x, y