# test_move_right.py

import unittest
from source.move_right import move_right

class TestMoveRight(unittest.TestCase):
    def test_move_right(self):
        self.assertEqual(move_right(0), 1)  # Should move from 0 to 1
        self.assertEqual(move_right(1), 1)  # Should stay at 1 if already there

if __name__ == '__main__':
    unittest.main()
# to test this case the command is "python -m unittest tests.test_move_right"
# to test all the cases the command is "python -m unittest discover -s tests"