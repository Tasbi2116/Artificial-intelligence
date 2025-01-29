import tkinter as tk
import random
import time

# Define the grid dimensions and number of iterations
GRID_SIZE = 8
ITERATIONS = 5
robot_loc = (0, 0)  # Start robot at the top-left corner

# Initialize matrices for object counts and actual objects
object_counter = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
active_objects = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

# Initialize success and error counters
successful_collects = 0
failed_collects = 0

# Function to initialize or reset the objects in the grid
def reset_active_objects():
    global active_objects
    active_objects = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    
    # Randomly place objects based on calculated probabilities
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            if random.random() < (object_counter[x][y] / ITERATIONS):  # Use previous probability for placement
                active_objects[x][y] = '🥶'  # Use the ice cold emoji for the object

# Function to run the simulation and calculate probabilities
def execute_simulation():
    global object_counter, successful_collects, failed_collects
    
    # Reset object count matrix and stats
    object_counter = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    successful_collects = 0
    failed_collects = 0
    
    # Run object placement and counting
    for _ in range(ITERATIONS):
        grid = [['🥶' if random.random() < 0.3 else '0' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        for x in range(GRID_SIZE):
            for y in range(GRID_SIZE):
                if grid[x][y] == '🥶':
                    object_counter[x][y] += 1



    # Calculate probability matrix
    prob_matrix = [[object_counter[x][y] / ITERATIONS for y in range(GRID_SIZE)] for x in range(GRID_SIZE)]
    
    # Reset and display new objects based on calculated probabilities
    reset_active_objects()
    refresh_ui(prob_matrix)

    # Start automatic robot movement
    move_robot(prob_matrix)

    # After the simulation ends, calculate and display the success rate
    show_success_rate()

# Function to update the UI grid with probabilities or objects
def refresh_ui(prob_matrix):
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            if active_objects[x][y] == '🥶':
                grid_cells[x][y].config(text='🥶', bg="lightblue")  # Object represented by emoji
            else:
                cell_text = f"{prob_matrix[x][y]:.2f}"
                grid_cells[x][y].config(text=cell_text, bg="lightgray")  # Probability
    root.update()

# Function for the robot to move towards the highest probability cell automatically
def move_robot(prob_matrix):
    global robot_loc, successful_collects, failed_collects
    
    visited_positions = set()
    
    while True:
        highest_prob = -1
        target_position = None
        
        # Find the cell with the highest probability (greater than 0) that has not been visited
        for x in range(GRID_SIZE):
            for y in range(GRID_SIZE):
                if prob_matrix[x][y] > highest_prob and (x, y) not in visited_positions and prob_matrix[x][y] > 0:
                    highest_prob = prob_matrix[x][y]
                    target_position = (x, y)

        # Break if no more high-probability cells are left
        if target_position is None:
            break

        # Move robot to target cell
        robot_loc = target_position
        x, y = robot_loc
        visited_positions.add((x, y))  # Mark cell as visited
        
        # Check if the robot successfully collected an object
        if active_objects[x][y] == '🥶':
            successful_collects += 1
            active_objects[x][y] = 0  # Remove the object after collection
            grid_cells[x][y].config(bg="yellow", text="")  # Clear object display
        else:
            failed_collects += 1
        
        # Update the UI for the robot's current position
        grid_cells[x][y].config(bg="orange", text="🤖")  # Use a robot emoji to represent the robot
        success_label.config(text=f"Successful Collects: {successful_collects}")
        error_label.config(text=f"Failed Collects: {failed_collects}")
        
        # Pause for a moment to visually show movement
        root.update()
        time.sleep(0.2)
        
        # Clear robot display from the current cell after the pause
        grid_cells[x][y].config(bg="lightgray" if active_objects[x][y] == 0 else "lightblue", text="")

# Function to calculate and display the success rate
def show_success_rate():
    total_attempts = successful_collects + failed_collects
    if total_attempts > 0:
        success_rate = successful_collects / total_attempts
    else:
        success_rate = 0
    success_rate_label.config(text=f"🚩Success Rate = {success_rate:.2f}🚩")

# Create the main application window
root = tk.Tk()
root.title("Robot Collection Simulation")
root.config(bg="lightcyan")  # Set background color of the main window

# Create an 8x8 grid of labels to display probabilities or objects
grid_cells = []
for x in range(GRID_SIZE):
    row = []
    for y in range(GRID_SIZE):
        label = tk.Label(root, text="0.00", width=5, height=2, borderwidth=1, relief="solid", font=("Arial", 12), bg="lightcyan")
        label.grid(row=x, column=y, padx=5, pady=5)
        row.append(label)
    grid_cells.append(row)

# Initialize labels to show success and error rates
success_label = tk.Label(root, text="Successful Collects: 0", font=("Arial", 14), fg="green", bg="lightcyan")
error_label = tk.Label(root, text="Failed Collects: 0", font=("Arial", 14), fg="red", bg="lightcyan")
success_label.grid(row=GRID_SIZE, column=0, columnspan=4, pady=10)
error_label.grid(row=GRID_SIZE, column=4, columnspan=4, pady=10)

# Label to display success rate
success_rate_label = tk.Label(root, text="🚩Success Rate = 0.00🚩", font=("Arial", 14), bg="lightcyan")
success_rate_label.grid(row=GRID_SIZE+1, column=0, columnspan=8, pady=10)

# Create a button to start the simulation
start_button = tk.Button(root, text="Start Simulation", command=execute_simulation, font=("Arial", 14), bg="lightgreen")
start_button.grid(row=GRID_SIZE+2, column=0, columnspan=8, pady=10)

# Run the main event loop
root.mainloop()