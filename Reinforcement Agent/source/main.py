import tkinter as tk
import random
import time

matrix_size = 8
num_iterations = 10
robot_position = (0, 0)  

object_count = [[0 for _ in range(matrix_size)] for _ in range(matrix_size)]
current_objects = [[0 for _ in range(matrix_size)] for _ in range(matrix_size)]
probability_matrix = [[0 for _ in range(matrix_size)] for _ in range(matrix_size)]

success_count = 0
error_count = 0

def reset_objects():
    global current_objects
    current_objects = [[0 for _ in range(matrix_size)] for _ in range(matrix_size)]
    
    for i in range(matrix_size):
        for j in range(matrix_size):
            if random.random() < probability_matrix[i][j]:  
                current_objects[i][j] = '🍔'

# Function to run the simulation and calculate probabilities
def run_simulation():
    global object_count, success_count, error_count, probability_matrix
    
    # Reset object count matrix and stats
    object_count = [[0 for _ in range(matrix_size)] for _ in range(matrix_size)]
    success_count = 0
    error_count = 0
    
    # Run object placement and counting for initial setup
    for _ in range(num_iterations):
        matrix = [['#' if random.random() < 0.3 else '0' for _ in range(matrix_size)] for _ in range(matrix_size)]
        for i in range(matrix_size):
            for j in range(matrix_size):
                if matrix[i][j] == '#':
                    object_count[i][j] += 1

    # Calculate initial probability matrix
    global probability_matrix
    probability_matrix = [[object_count[i][j] / num_iterations for j in range(matrix_size)] for i in range(matrix_size)]
    
    reset_objects()
    update_ui(probability_matrix)
    move_robot_automatically()

# Function to update the UI grid with probabilities or objects
def update_ui(probability_matrix):
    for i in range(matrix_size):
        for j in range(matrix_size):
            if current_objects[i][j] == '🍔':
                cells[i][j].config(text="🍔", bg="lightgreen")
            else:
                cell_text = f"{probability_matrix[i][j]:.2f}"
                cells[i][j].config(text=cell_text, bg="lightpink")
    root.update()

# Function for the robot to move towards the highest probability cell automatically
def move_robot_automatically():
    global robot_position, success_count, error_count, probability_matrix
    
    visited_cells = set()
    
    while True:
        max_prob = -1
        target_cell = None
        
        # Find the cell with the highest probability (greater than 0.40) that has not been visited
        for i in range(matrix_size):
            for j in range(matrix_size):
                if probability_matrix[i][j] > max_prob and (i, j) not in visited_cells and probability_matrix[i][j] >= 0.40:
                    max_prob = probability_matrix[i][j]
                    target_cell = (i, j)

        # Break if no more high-probability cells are left
        if target_cell is None:
            break

        robot_position = target_cell
        i, j = robot_position
        visited_cells.add((i, j))
        # Check if the robot successfully collected an object
        if current_objects[i][j] == '🍔':
            success_count += 1
            current_objects[i][j] = 0

            # Only adjust probability if it's above 0.40
            if probability_matrix[i][j] >= 0.40:
                probability_matrix[i][j] = min(probability_matrix[i][j] + 0.05, 1.0)  # Increase probability
            cells[i][j].config(bg="yellow", text="")
        else:
            error_count += 1
            if probability_matrix[i][j] >= 0.40:
                probability_matrix[i][j] = max(probability_matrix[i][j] - 0.05, 0.0)
            cells[i][j].config(bg="gray", text="")  # Mark cell as visited without object
        
        # Update the UI for the robot's current position
        cells[i][j].config(bg="blue", text="😍")
        
        # Calculate and display the success rate
        total_attempts = success_count + error_count
        success_rate = (success_count / total_attempts) * 100 if total_attempts > 0 else 0
        success_count_label.config(text=f"Success Count: {success_count}")
        error_count_label.config(text=f"Error Count: {error_count}")
        success_rate_label.config(text=f"Success Rate: {success_rate:.2f}%")
        

        root.update()
        time.sleep(.2)
        
        cells[i][j].config(bg="lightpink" if current_objects[i][j] == 0 else "lightgreen", text="")

    reset_objects()
    update_ui(probability_matrix)

# Create the main application window
root = tk.Tk()
root.title("Robot Object Collection Simulation")

# Create a frame for the grid and labels
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

# Create an 8x8 grid of labels to display probabilities or objects
cells = []
for i in range(matrix_size):
    row = []
    for j in range(matrix_size):
        label = tk.Label(frame, text="0.00", width=5, height=2, borderwidth=1, relief="solid", font=("Arial", 12))
        label.grid(row=i, column=j, padx=2, pady=2)
        row.append(label)
    cells.append(row)

# Add labels for success count, error count, and success rate on top of the grid
header_frame = tk.Frame(root)
header_frame.pack(padx=10, pady=10)

success_count_label = tk.Label(header_frame, text="Success Count: 0", font=("Arial", 14), fg="green")
error_count_label = tk.Label(header_frame, text="Error Count: 0", font=("Arial", 14), fg="red")
success_rate_label = tk.Label(header_frame, text="Success Rate: 0%", font=("Arial", 14), fg="blue")

success_count_label.grid(row=0, column=0, padx=10)
error_count_label.grid(row=0, column=1, padx=10)
success_rate_label.grid(row=0, column=2, padx=10)

# Create a button to start the simulation
run_button = tk.Button(root, text="Run Simulation", command=run_simulation, font=("Arial", 14), bg="lightblue", width=20)
run_button.pack(pady=10)

# Run the main event loop
root.mainloop()