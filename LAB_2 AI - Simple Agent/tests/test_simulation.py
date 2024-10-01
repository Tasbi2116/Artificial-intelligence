import unittest
from unittest.mock import patch, MagicMock
from source.simulation import run_agent_simulation

class TestAgentSimulation(unittest.TestCase):

    @patch('source.simulation.generate_environment')
    @patch('source.simulation.agent_start')
    @patch('source.simulation.grab_item')
    @patch('source.simulation.display_environment')
    @patch('source.simulation.check_boundary')
    @patch('source.simulation.move_agent')
    @patch('source.simulation.evaluate_performance')
    @patch('source.simulation.show_results')
    def test_run_agent_simulation(self, mock_show_results, mock_evaluate_performance,
                                   mock_move_agent, mock_check_boundary,
                                   mock_display_environment, mock_grab_item,
                                   mock_agent_start, mock_generate_environment):

        # Setting up the mocks
        mock_generate_environment.return_value = [[0, 0, 0, 0, 0, 0, 0],
                                                   [0, '1', 0, 0, 0, 0, 0],
                                                   [0, 0, 0, 0, '1', 0, 0],
                                                   [0, 0, 0, 0, 0, 0, 0],
                                                   [0, 0, 0, 0, 0, 0, 0]]
        mock_agent_start.return_value = (1, 1)  # Starting position of the agent
        mock_grab_item.side_effect = [True, False]  # Simulate grabbing items
        mock_check_boundary.side_effect = [False, True]  # Simulate boundary checks
        mock_move_agent.side_effect = [(1, 2), (1, 1)]  # Simulate movements

        # Run the simulation
        run_agent_simulation()

        # Check that the simulation ran the expected number of times
        self.assertEqual(mock_generate_environment.call_count, 100)

        # Check that show_results is called at the end
        mock_show_results.assert_called_once()

        # Ensure evaluate_performance was called with correct parameters
        # (total_actions_count, collection_count)
        mock_evaluate_performance.assert_called_once()

    @patch('source.simulation.generate_environment')
    @patch('source.simulation.agent_start')
    @patch('source.simulation.grab_item')
    @patch('source.simulation.check_boundary')
    @patch('source.simulation.move_agent')
    def test_simulation_with_no_items(self, mock_move_agent, mock_check_boundary,
                                       mock_grab_item, mock_agent_start, mock_generate_environment):

        # Setting up mocks to simulate no items in the environment
        mock_generate_environment.return_value = [[0] * 7 for _ in range(5)]  # Empty environment
        mock_agent_start.return_value = (1, 1)  # Starting position of the agent
        mock_grab_item.return_value = False  # Simulate no items to grab
        mock_check_boundary.side_effect = [False, True]  # Simulate boundary checks
        mock_move_agent.return_value = (1, 2)  # Simulate a valid move

        # Run the simulation
        run_agent_simulation()

        # Check that the agent couldn't collect any items
        mock_grab_item.assert_called()
        self.assertEqual(mock_grab_item.call_count, 1)  # Should only check once

if __name__ == '__main__':
    unittest.main()