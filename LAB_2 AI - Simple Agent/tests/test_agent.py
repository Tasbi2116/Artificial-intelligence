import unittest
from source.actions import (
    agent_start,
    move_up_direction,
    move_down_direction,
    move_left_direction,
    move_right_direction,
    move_agent,
)

class TestAgentActions(unittest.TestCase):

    def test_agent_start(self):
        x, y = agent_start()
        # The agent's starting position should be between (1,1) and (3,5)
        self.assertGreaterEqual(x, 1)
        self.assertLessEqual(x, 3)
        self.assertGreaterEqual(y, 1)
        self.assertLessEqual(y, 5)

    def test_move_up_direction(self):
        new_x, new_y = move_up_direction(2, 3)
        self.assertEqual((new_x, new_y), (1, 3))

    def test_move_down_direction(self):
        new_x, new_y = move_down_direction(2, 3)
        self.assertEqual((new_x, new_y), (3, 3))

    def test_move_left_direction(self):
        new_x, new_y = move_left_direction(2, 3)
        self.assertEqual((new_x, new_y), (2, 2))

    def test_move_right_direction(self):
        new_x, new_y = move_right_direction(2, 3)
        self.assertEqual((new_x, new_y), (2, 4))

    def test_move_agent_within_bounds(self):
        visited_positions = [(1, 2), (2, 3)]
        new_x, new_y = move_agent(2, 2, visited_positions)

        # The new position should not be in visited_positions
        self.assertNotIn((new_x, new_y), visited_positions)

        # Check that the new position is within the valid range
        self.assertGreaterEqual(new_x, 0)
        self.assertLessEqual(new_x, 4)  # since the maximum x is 4
        self.assertGreaterEqual(new_y, 0)
        self.assertLessEqual(new_y, 6)  # since the maximum y is 6

    def test_move_agent_no_revisit(self):
        visited_positions = [(0, 0), (1, 1), (2, 2)]
        # Move from (2, 2) with visited positions
        new_x, new_y = move_agent(2, 2, visited_positions)

        # Ensure the new position is not a visited position
        self.assertNotIn((new_x, new_y), visited_positions)

# If you want to run this test file directly
if __name__ == '__main__':
    unittest.main()
