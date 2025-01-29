import unittest
from source.actuators import move_up, move_down, move_left, move_right, collect_object

class TestActuators(unittest.TestCase):
    def test_move_up(self):
        self.assertEqual(move_up(3, 3), (2, 3))

    def test_move_down(self):
        self.assertEqual(move_down(3, 3), (4, 3))

    def test_move_left(self):
        self.assertEqual(move_left(3, 3), (3, 2))

    def test_move_right(self):
        self.assertEqual(move_right(3, 3), (3, 4))

    def test_collect_object(self):
        room = [["path"] * 8 for _ in range(8)]
        room[2][2] = "object"  # Place an object to collect
        collect_object(room, 2, 2)
        self.assertEqual(room[2][2], "path")  # Check if the object was collected

if __name__ == '__main__':
    unittest.main()

# python -m unittest discover -s tests
