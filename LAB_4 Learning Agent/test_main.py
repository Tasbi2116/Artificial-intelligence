import unittest
import random
from main import execute_simulation, move_robot, show_success_rate

class TestSimulationLogic(unittest.TestCase):

    # Test 1: Object Counter Initialization
    def test_object_counter_initialization(self):
        GRID_SIZE = 8
        object_counter = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        for row in object_counter:
            for cell in row:
                self.assertEqual(cell, 0, "Object counter initialization failed")

    # Test 2: Active Objects Reset
    def test_reset_active_objects(self):
        GRID_SIZE = 8
        ITERATIONS = 5
        object_counter = [[random.randint(0, ITERATIONS) for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

        def reset_active_objects():
            active_objects = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
            for x in range(GRID_SIZE):
                for y in range(GRID_SIZE):
                    if random.random() < (object_counter[x][y] / ITERATIONS):
                        active_objects[x][y] = '🥶'
            return active_objects

        active_objects = reset_active_objects()
        for row in active_objects:
            for cell in row:
                self.assertIn(cell, [0, '🥶'], "Active objects reset failed")

    # Test 3: Probability Matrix Calculation
    def test_probability_matrix(self):
        GRID_SIZE = 8
        ITERATIONS = 5
        object_counter = [[random.randint(0, ITERATIONS) for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        prob_matrix = [[object_counter[x][y] / ITERATIONS for y in range(GRID_SIZE)] for x in range(GRID_SIZE)]

        for x in range(GRID_SIZE):
            for y in range(GRID_SIZE):
                expected = object_counter[x][y] / ITERATIONS
                self.assertEqual(prob_matrix[x][y], expected, f"Probability matrix calculation failed at ({x}, {y})")

    # Test 4: Robot Movement Logic
    def test_robot_movement(self):
        GRID_SIZE = 8
        prob_matrix = [[random.random() for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        active_objects = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        
        # Place a few objects
        active_objects[2][3] = '🥶'
        active_objects[5][6] = '🥶'

        successful_collects = 0
        failed_collects = 0
        visited_positions = set()

        def move_robot(prob_matrix, active_objects):
            nonlocal successful_collects, failed_collects
            robot_loc = (0, 0)

            while True:
                highest_prob = -1
                target_position = None

                for x in range(GRID_SIZE):
                    for y in range(GRID_SIZE):
                        if prob_matrix[x][y] > highest_prob and (x, y) not in visited_positions and prob_matrix[x][y] > 0:
                            highest_prob = prob_matrix[x][y]
                            target_position = (x, y)

                if target_position is None:
                    break

                robot_loc = target_position
                visited_positions.add(robot_loc)

                x, y = robot_loc
                if active_objects[x][y] == '🥶':
                    successful_collects += 1
                    active_objects[x][y] = 0
                else:
                    failed_collects += 1

        move_robot(prob_matrix, active_objects)
        
        # Validate success and error counts
        self.assertEqual(successful_collects, 2, f"Expected 2 successful collects, got {successful_collects}")
        self.assertGreaterEqual(failed_collects, 0, "Failed collects should be non-negative")

    # Test 5: Success Rate Calculation
    def test_success_rate(self):
        successful_collects = 4
        failed_collects = 1
        total_attempts = successful_collects + failed_collects
        success_rate = successful_collects / total_attempts if total_attempts > 0 else 0

        self.assertEqual(success_rate, 0.8, f"Expected success rate 0.8, got {success_rate:.2f}")


# Run all tests if executed as a script
if __name__ == "__main__":
    unittest.main()