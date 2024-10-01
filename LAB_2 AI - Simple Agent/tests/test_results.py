import unittest
from unittest.mock import patch
from io import StringIO
from source.result import show_results  # Import the function from the correct module

class TestShowResults(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_show_results(self, mock_stdout):
        # Define the inputs for the function
        total_objects = 5
        total_movements = 10
        all_agent_actions = 15
        collection_actions = 5
        performance_result = 3.0
        
        # Call the function with the test inputs
        show_results(total_objects, total_movements, all_agent_actions, collection_actions, performance_result)
        
        # Define the expected output (as a multi-line string)
        expected_output = (
            "Simulation Summary\n"
            "Total Collected Objects: 5\n"
            "Total Movements: 10\n"
            "Total Agent Actions (Movements + Collections): 15\n"
            "Performance (Actions / Collections): 3.00\n"
        )

        # Compare the captured output with the expected output
        self.assertEqual(mock_stdout.getvalue(), expected_output)

# If you want to run this test file directly
if __name__ == '__main__':
    unittest.main()
