import unittest
from io import StringIO
import sys
from source.environment import generate_environment, display_environment

class TestEnvironment(unittest.TestCase):

    # Test case for 'generate_environment' function
    def test_generate_environment(self):
        environment = generate_environment()

        # Ensure the environment is a 5x7 grid
        self.assertEqual(len(environment), 5)  # 5 rows
        self.assertTrue(all(len(row) == 7 for row in environment))  # 7 columns in each row
        
        # Ensure there are exactly 10 objects (marked as '1') in the environment
        total_objects = sum(row.count('1') for row in environment)
        self.assertEqual(total_objects, 10)

    # Test case for 'display_environment' function
    def test_display_environment(self):
        # Capture the printed output using StringIO
        captured_output = StringIO()
        sys.stdout = captured_output

        # Mock environment and agent position
        environment = [
            [0, 0, '1', 0, 0, 0, 0],
            [0, 0, 0, 0, 0, '1', 0],
            ['1', 0, 0, 0, 0, 0, 0],
            [0, '1', 0, 0, 0, 0, 0],
            [0, 0, 0, '1', 0, 0, 0]
        ]
        agent_x, agent_y = 2, 2  # Agent is at position (2, 2)

        # Call display_environment
        display_environment(environment, agent_x, agent_y)

        # Expected output
        expected_output = (
            "0 0 1 0 0 0 0 \n"
            "0 0 0 0 0 1 0 \n"
            "1 0 A 0 0 0 0 \n"
            "0 1 0 0 0 0 0 \n"
            "0 0 0 1 0 0 0 \n\n"
        )

        # Check if the output matches the expected output
        self.assertEqual(captured_output.getvalue(), expected_output)

        # Reset stdout to default
        sys.stdout = sys.__stdout__

# If you want to run this test file directly
if __name__ == '__main__':
    unittest.main()
