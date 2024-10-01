import unittest
from source.actions import grab_item, evaluate_performance  # Ensure these functions are in the correct module

class TestAgentActions(unittest.TestCase):

    # Test case for the 'grab_item' function
    def test_grab_item_success(self):
        # Setup environment where the agent is on an object ('1')
        environment = [
            [0, 0, 0],
            [0, '1', 0],
            [0, 0, 0]
        ]
        agent_x, agent_y = 1, 1  # Agent is on the object

        result = grab_item(environment, agent_x, agent_y)
        
        # Assert the result is True (object grabbed)
        self.assertTrue(result)
        # Assert the object was removed from the environment
        self.assertEqual(environment[agent_x][agent_y], 0)

    def test_grab_item_failure(self):
        # Setup environment where there is no object in the agent's position
        environment = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        agent_x, agent_y = 1, 1  # Agent is on an empty cell

        result = grab_item(environment, agent_x, agent_y)
        
        # Assert the result is False (no object to grab)
        self.assertFalse(result)
        # Assert the environment remains unchanged
        self.assertEqual(environment[agent_x][agent_y], 0)

    # Test case for the 'evaluate_performance' function
    def test_evaluate_performance_valid(self):
        # Test a valid case where objects are collected
        total_actions = 10
        collections = 5
        performance = evaluate_performance(total_actions, collections)
        
        # Assert that the performance calculation is correct
        self.assertEqual(performance, 2.0)

    def test_evaluate_performance_zero_collections(self):
        # Test when there are no collections (to avoid division by zero)
        total_actions = 10
        collections = 0
        performance = evaluate_performance(total_actions, collections)
        
        # Assert that the performance is 0 when there are no collections
        self.assertEqual(performance, 0)

# If you want to run this test file directly
if __name__ == '__main__':
    unittest.main()
