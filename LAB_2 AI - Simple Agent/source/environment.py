import random

# Generate the environment (grid with random objects)
def generate_environment():
    environment = []
    for _ in range(5):
        row = [0] * 7
        environment.append(row)
    for _ in range(10):
        while True:
            x = random.randint(0, 4)
            y = random.randint(0, 6)
            if environment[x][y] == 0:
                environment[x][y] = '1'
                break
    return environment

# Display the environment and the agent's position
def display_environment(environment, agent_x, agent_y):
    for i, row in enumerate(environment):
        for j, cell in enumerate(row):
            if i == agent_x and j == agent_y:
                print("A", end=" ")
            else:
                print(cell if cell != 0 else '0', end=" ")
        print()
    print("\n")
