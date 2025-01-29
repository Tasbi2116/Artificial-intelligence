# perceptions.py

def check_object(room, x, y):
    return room[x][y] == "object"

def perceive_boundaries(x, y, room):
    return x == 0 or y == 0 or x == (len(room) - 1) or y == (len(room[0]) - 1)