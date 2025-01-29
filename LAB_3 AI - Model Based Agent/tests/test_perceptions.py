import unittest
from source.perceptions import check_object, perceive_boundaries

class TestPerceptions(unittest.TestCase):
    def test_check_object(self):
        room = [["path"] * 8 for _ in range(8)]
        room[2][2] = "object"  # Place an object in the room
        self.assertTrue(check_object(room, 2, 2))
        self.assertFalse(check_object(room, 1, 1))  # No object at (1, 1)

    def test_perceive_boundaries(self):
        room = [["path"] * 8 for _ in range(8)]
        self.assertTrue(perceive_boundaries(0, 3, room))  # Top edge
        self.assertTrue(perceive_boundaries(7, 3, room))  # Bottom edge
        self.assertTrue(perceive_boundaries(3, 0, room))  # Left edge
        self.assertTrue(perceive_boundaries(3, 7, room))  # Right edge
        self.assertFalse(perceive_boundaries(3, 3, room))  # Inside

if __name__ == '__main__':
    unittest.main()