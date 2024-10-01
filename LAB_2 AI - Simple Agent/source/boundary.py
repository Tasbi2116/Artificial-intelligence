# Check if the agent has reached the boundary of the grid
def check_boundary(agent_x, agent_y):
    return agent_x == 0 or agent_y == 0 or agent_x == 4 or agent_y == 6