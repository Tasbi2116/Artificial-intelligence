import unittest
from source.calculate_nearest_object import find_nearest_object

class TestCalculateNearestObject(unittest.TestCase):
    def test_find_nearest_object(self):
        room = [
            ["path", "path", "path", "path"],
            ["path", "object", "path", "path"],
            ["path", "path", "path", "object"],
            ["path", "path", "path", "path"]
        ]
        self.assertEqual(find_nearest_object(room, 0, 0), (1, 1))  # Nearest object is at (1, 1)

if __name__ == '__main__':
    unittest.main()