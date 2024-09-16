# main.py

# Import the functions from their respective modules
from random_dirt import randomDirtOnTiles
from move_right import move_right
from move_left import move_left
from suck_dirt import suck_dirt
from calculate_performance import calculate_performance

# Main program
numOfTiles = 2
numSimulations = 1000

total_move_left = 0
total_move_right = 0
total_suck_dirt = 0
total_dirt_cleaned = 0

for _ in range(numSimulations):
    tiles = randomDirtOnTiles()  
    pos = 0  
    dirt_cleaned = 0

    # Clean the dirt at the starting position (tile 0) if necessary
    if suck_dirt(tiles, pos):
        dirt_cleaned += 1
        total_suck_dirt += 1  

    # Move to the other tile (tile 1) only if it has dirt
    if tiles[1] == 1:
        pos = move_right(pos)
        total_move_right += 1 

        # Clean the dirt at the new position (tile 1)
        if suck_dirt(tiles, pos):
            dirt_cleaned += 1
            total_suck_dirt += 1 

        # Move back to the starting position (tile 0)
        pos = move_left(pos)
        total_move_left += 1  

    total_dirt_cleaned += dirt_cleaned 

# Calculate total actions and performance using the new function
results = calculate_performance(total_move_left, total_move_right, total_suck_dirt, total_dirt_cleaned)

# Print the results
print(f"Total Actions (Move Left, Move Right, Suck Dirt): {results['total_actions']}")
print(f"Total Dirt Cleaned: {total_dirt_cleaned}")
print(f"Performance: {results['performance']}")
