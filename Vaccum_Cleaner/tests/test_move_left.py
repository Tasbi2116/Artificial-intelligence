# test_move_left.py

import unittest
from source.move_left import move_left

class TestMoveLeft(unittest.TestCase):
    def test_move_left(self):
        self.assertEqual(move_left(1), 0)  # Should move from 1 to 0
        self.assertEqual(move_left(0), 0)  # Should stay at 0 if already there

if __name__ == '__main__':
    unittest.main()
