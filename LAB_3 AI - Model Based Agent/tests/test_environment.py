import unittest
from source.environment import create_room

class TestEnvironment(unittest.TestCase):
    def test_create_room(self):
        room = create_room()
        self.assertEqual(len(room), 8)  # Check room size
        for row in room:
            self.assertEqual(len(row), 8)  # Each row should have 8 columns

if __name__ == '__main__':
    unittest.main()