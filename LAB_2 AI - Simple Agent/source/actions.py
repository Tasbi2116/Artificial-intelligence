# Grab object if the agent is on a cell with an object
def grab_item(environment, agent_x, agent_y):
    if environment[agent_x][agent_y] == '1':
        environment[agent_x][agent_y] = 0
        return True
    return False

# Evaluate the performance of the agent based on actions and collections
def evaluate_performance(total_agent_actions, object_collection_actions):
    return total_agent_actions / object_collection_actions if object_collection_actions > 0 else 0