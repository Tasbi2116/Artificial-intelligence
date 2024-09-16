# test_random_dirt.py

import unittest
from source.random_dirt import randomDirtOnTiles

class TestRandomDirtOnTiles(unittest.TestCase):
    def test_random_dirt(self):
        tiles = randomDirtOnTiles()
        # Check if the result is a list of two elements
        self.assertEqual(len(tiles), 2)
        # Check if each element is either 0 or 1
        for tile in tiles:
            self.assertIn(tile, [0, 1])

if __name__ == '__main__':
    unittest.main()
