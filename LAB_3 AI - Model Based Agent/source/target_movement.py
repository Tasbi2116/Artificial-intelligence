# target_movement.py
import random
from actuators import move_up, move_down, move_left, move_right

def move_towards_target(room, x, y, target):
    target_x, target_y = target

    if x > target_x and room[x - 1][y] != "hurdle":
        return move_up(x, y), 'up', True
    elif x < target_x and room[x + 1][y] != "hurdle":
        return move_down(x, y), 'down', True
    elif y > target_y and room[x][y - 1] != "hurdle":
        return move_left(x, y), 'left', True
    elif y < target_y and room[x][y + 1] != "hurdle":
        return move_right(x, y), 'right', True

    # Random fallback if blocked
    directions = ['up', 'down', 'left', 'right']
    random.shuffle(directions)
    for direction in directions:
        if direction == 'up' and room[x - 1][y] != "hurdle":
            return move_up(x, y), 'up', True
        elif direction == 'down' and room[x + 1][y] != "hurdle":
            return move_down(x, y), 'down', True
        elif direction == 'left' and room[x][y - 1] != "hurdle":
            return move_left(x, y), 'left', True
        elif direction == 'right' and room[x][y + 1] != "hurdle":
            return move_right(x, y), 'right', True

    return (x, y), None, False  # No move possible