from environment import generate_environment, display_environment
from agent import agent_start, move_agent
from actions import grab_item, evaluate_performance
from boundary import check_boundary
from result import show_results

def run_agent_simulation():
    collected_items = 0
    moves_count = 0
    collection_count = 0
    total_actions_count = 0

    for round_num in range(100):
        print(f"Round {round_num + 1}")
        round_collected_items = 0
        current_moves = 0
        round_collections = 0
        round_actions = 0

        environment = generate_environment()
        agent_x, agent_y = agent_start()
        visited_positions = set()
        visited_positions.add((agent_x, agent_y))
        agent_path = [(agent_x, agent_y)]

        while True:
            if grab_item(environment, agent_x, agent_y):
                round_collected_items += 1
                collected_items += 1
                round_collections += 1
                display_environment(environment, agent_x, agent_y)

            if check_boundary(agent_x, agent_y):
                print(f"Items collected in this round: {round_collected_items}")
                break
            
            new_x, new_y = move_agent(agent_x, agent_y, visited_positions)
            round_actions += 1

            if (new_x, new_y) == (agent_x, agent_y):
                print("Agent has no valid moves left. Stopping this round.")
                break
            
            agent_x, agent_y = new_x, new_y
            visited_positions.add((agent_x, agent_y))
            current_moves += 1
            agent_path.append((agent_x, agent_y))
        
        print(f"Path taken in round {round_num + 1}: {agent_path}\n")
        moves_count += current_moves
        collection_count += round_collections
        total_actions_count += (current_moves + round_collections)  # Total actions = moves + collections

    # Performance Calculation
    final_performance = evaluate_performance(total_actions_count, collection_count)
    show_results(collected_items, moves_count, total_actions_count, collection_count, final_performance)

if __name__ == '__main__':
    run_agent_simulation()