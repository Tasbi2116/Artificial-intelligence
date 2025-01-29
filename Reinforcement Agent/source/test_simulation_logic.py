import unittest
import random

# Mock functions and data for the tests
matrix_size = 8
num_iterations = 10
object_count = [[0 for _ in range(matrix_size)] for _ in range(matrix_size)]
current_objects = [[0 for _ in range(matrix_size)] for _ in range(matrix_size)]
probability_matrix = [[0 for _ in range(matrix_size)] for _ in range(matrix_size)]

success_count = 0
error_count = 0
robot_position = (0, 0)

def reset_objects():
    global current_objects
    current_objects = [[0 for _ in range(matrix_size)] for _ in range(matrix_size)]
    
    for i in range(matrix_size):
        for j in range(matrix_size):
            if random.random() < probability_matrix[i][j]:  
                current_objects[i][j] = '🍔'

def run_simulation():
    global object_count, success_count, error_count, probability_matrix
    
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

    probability_matrix = [[object_count[i][j] / num_iterations for j in range(matrix_size)] for i in range(matrix_size)]
    
    reset_objects()

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

        if target_cell is None:
            break

        robot_position = target_cell
        i, j = robot_position
        visited_cells.add((i, j))

        if current_objects[i][j] == '🍔':
            success_count += 1
            current_objects[i][j] = 0
            if probability_matrix[i][j] >= 0.40:
                probability_matrix[i][j] = min(probability_matrix[i][j] + 0.05, 1.0)
        else:
            error_count += 1
            if probability_matrix[i][j] >= 0.40:
                probability_matrix[i][j] = max(probability_matrix[i][j] - 0.05, 0.0)

class TestSimulationFunctions(unittest.TestCase):
    
    def test_reset_objects(self):
        global current_objects, probability_matrix
        # Set a custom probability matrix for testing
        probability_matrix = [
            [0.1, 0.5, 0.3, 0.4, 0.6, 0.2, 0.9, 0.7],
            [0.4, 0.6, 0.7, 0.2, 0.1, 0.8, 0.5, 0.3],
            [0.3, 0.6, 0.4, 0.7, 0.8, 0.9, 0.1, 0.5],
            [0.7, 0.4, 0.5, 0.2, 0.6, 0.3, 0.8, 0.9],
            [0.2, 0.5, 0.6, 0.9, 0.3, 0.4, 0.7, 0.8],
            [0.6, 0.8, 0.7, 0.5, 0.2, 0.1, 0.3, 0.4],
            [0.1, 0.9, 0.5, 0.6, 0.7, 0.3, 0.4, 0.2],
            [0.4, 0.3, 0.2, 0.8, 0.6, 0.7, 0.5, 0.1]
        ]
        
        reset_objects()
        
        # Ensure some cells contain objects based on the probability matrix
        object_count = sum(1 for row in current_objects for cell in row if cell == '🍔')
        
        # Test that the object count is greater than 0
        self.assertGreater(object_count, 0, "Objects should be placed according to the probability matrix.")

    def test_run_simulation(self):
        global object_count, probability_matrix
        run_simulation()

        # Ensure the probability matrix is correctly calculated
        self.assertEqual(len(probability_matrix), matrix_size, "Probability matrix should have correct dimensions.")
        
        # Ensure all probabilities are within [0, 1]
        for row in probability_matrix:
            for prob in row:
                self.assertGreaterEqual(prob, 0, "Probability should be >= 0.")
                self.assertLessEqual(prob, 1, "Probability should be <= 1.")
        
    def test_move_robot_automatically(self):
        global robot_position, success_count, error_count, probability_matrix, current_objects
        current_objects = [
            ['🍔', 0, '🍔', 0, 0, 0, 0, '🍔'],
            [0, 0, 0, 0, 0, 0, 0, 0],
            ['🍔', 0, '🍔', 0, 0, '🍔', 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            ['🍔', 0, 0, 0, '🍔', 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, '🍔', 0, 0, 0, 0, 0, 0]
        ]
        probability_matrix = [
            [0.5, 0.3, 0.8, 0.2, 0.6, 0.7, 0.1, 0.9],
            [0.4, 0.5, 0.7, 0.3, 0.1, 0.6, 0.2, 0.4],
            [0.8, 0.9, 0.7, 0.5, 0.6, 0.4, 0.2, 0.3],
            [0.2, 0.6, 0.8, 0.3, 0.5, 0.7, 0.1, 0.9],
            [0.7, 0.2, 0.5, 0.4, 0.8, 0.6, 0.9, 0.3],
            [0.1, 0.4, 0.7, 0.9, 0.2, 0.8, 0.5, 0.6],
            [0.5, 0.3, 0.2, 0.6, 0.7, 0.9, 0.1, 0.8],
            [0.6, 0.9, 0.4, 0.5, 0.2, 0.3, 0.7, 0.8]
        ]
        run_simulation()

        # Simulate robot movement
        move_robot_automatically()

        # Check success and error counts after robot movement
        self.assertGreater(success_count, 0, "Robot should collect at least one object.")
        self.assertGreater(error_count, 0, "Robot should encounter at least one error.")
        
        # Ensure the robot position is within bounds
        self.assertTrue(0 <= robot_position[0] < matrix_size, "Robot position should be within the matrix bounds.")
        self.assertTrue(0 <= robot_position[1] < matrix_size, "Robot position should be within the matrix bounds.")

if __name__ == "__main__":
    unittest.main()

# python -m unittest test_simulation_logic.py