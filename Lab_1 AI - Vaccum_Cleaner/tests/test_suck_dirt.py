# test_suck_dirt.py

import unittest
from source.suck_dirt import suck_dirt

class TestSuckDirt(unittest.TestCase):
    def test_suck_dirt(self):
        tiles = [1, 0]
        # Test sucking dirt at position 0 (should clean the tile)
        self.assertTrue(suck_dirt(tiles, 0))
        self.assertEqual(tiles[0], 0)  # Tile 0 should now be clean
        
        # Test sucking dirt at position 1 (no dirt to clean)
        self.assertFalse(suck_dirt(tiles, 1))
        self.assertEqual(tiles[1], 0)  # Tile 1 should remain clean

if __name__ == '__main__':
    unittest.main()
