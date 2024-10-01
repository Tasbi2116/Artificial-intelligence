import random

# Initialize agent's starting position
def agent_start():
    x_pos = random.randint(1, 3)
    y_pos = random.randint(1, 5)
    return x_pos, y_pos

# Move agent in different directions
def move_up_direction(agent_x, agent_y):
    return agent_x - 1, agent_y

def move_down_direction(agent_x, agent_y):
    return agent_x + 1, agent_y

def move_left_direction(agent_x, agent_y):
    return agent_x, agent_y - 1

def move_right_direction(agent_x, agent_y):
    return agent_x, agent_y + 1

# Move the agent randomly, ensuring it's within bounds and not revisiting positions
def move_agent(agent_x, agent_y, visited_positions):
    possible_directions = ['up', 'down', 'left', 'right']
    while possible_directions:
        direction = random.choice(possible_directions)
        if direction == 'up':
            new_x, new_y = move_up_direction(agent_x, agent_y)
        elif direction == 'down':
            new_x, new_y = move_down_direction(agent_x, agent_y)
        elif direction == 'left':
            new_x, new_y = move_left_direction(agent_x, agent_y)
        elif direction == 'right':
            new_x, new_y = move_right_direction(agent_x, agent_y)

        if (0 <= new_x < 5 and 0 <= new_y < 7) and (new_x, new_y) not in visited_positions:
            return new_x, new_y
        possible_directions.remove(direction)
    
    return agent_x, agent_y
