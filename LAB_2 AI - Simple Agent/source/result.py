# Show the results of the simulation (performance and summary)
def show_results(total_objects, total_movements, all_agent_actions, collection_actions, performance_result):
    print("Simulation Summary")
    print(f"Total Collected Objects: {total_objects}")
    print(f"Total Movements: {total_movements}")
    print(f"Total Agent Actions (Movements + Collections): {all_agent_actions}")
    print(f"Performance (Actions / Collections): {performance_result:.2f}")