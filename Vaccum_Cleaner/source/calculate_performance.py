# calculate_performance.py

def calculate_performance(total_move_left: int, total_move_right: int, total_suck_dirt: int, total_dirt_cleaned: int) -> dict:
    # Calculate total actions
    total_actions = total_move_left + total_move_right + total_suck_dirt
    
    # Calculate performance, ensure there's no division by zero
    performance = total_actions / total_dirt_cleaned if total_dirt_cleaned > 0 else 0

    return {
        'total_actions': total_actions,
        'performance': performance
    }
