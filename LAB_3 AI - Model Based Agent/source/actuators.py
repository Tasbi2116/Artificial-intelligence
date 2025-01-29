# actuators.py

def move_up(x, y):
    return x - 1, y

def move_down(x, y):
    return x + 1, y

def move_left(x, y):
    return x, y - 1

def move_right(x, y):
    return x, y + 1

def collect_object(room, x, y):
    room[x][y] = "path"